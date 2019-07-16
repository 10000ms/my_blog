from django.db import models
from django.db import transaction

from ..middleware.current_user import get_current_user
from ..manager import blog
from utils.model_str import str_for_model
from utils.es import ESControl


class Blog(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.PROTECT, default=get_current_user)
    author = models.CharField('作者', max_length=256)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    last_change_time = models.DateTimeField('最后修改', auto_now=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    tabs = models.ManyToManyField('Tab')
    brief = models.CharField('简介', max_length=256)
    content = models.TextField('正文')
    read_count = models.IntegerField('阅读数', default=0)
    like_count = models.IntegerField('喜欢数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)

    objects = blog.BlogManager()

    def set_now_value(self):
        """
        把旧值记录起来，方便es更新时确定
        :return:
        """
        self._title = self.title
        self._author = self.author
        self._brief = self.brief
        self._content = self.content

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)
        self.set_now_value()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        重写save方法，支持es搜索功能
        """
        # 区分创建和修改
        if not self.pk:
            create_mode = True
        else:
            create_mode = False
        with transaction.atomic():
            res = super().save(
                force_insert=force_insert,
                force_update=force_update,
                using=using,
                update_fields=update_fields
            )
            es = ESControl()
            es_body = {
                'title': self.title,
                'author': self.author,
                'brief': self.brief,
                'content': self.content,
            }
            if create_mode:
                es.create('blog', id=self.id, body=es_body)
            elif self._title != self.title \
                    or self._author != self.author \
                    or self._brief != self.brief \
                    or self._content != self.content:
                # 只有这些值改变才进行es数据库的修改
                # 根据文档，增加格式
                es_body = {'doc': es_body}
                es.update('blog', id=self.id, body=es_body)
        self.set_now_value()
        return res

    def delete(self, using=None, keep_parents=False):
        """
        重写delete方法，支持es搜索功能
        """
        i = self.id
        es = ESControl()
        with transaction.atomic():
            res = super().delete(using=using, keep_parents=keep_parents)
            es.delete('blog', id=i, ignore=404)
        return res

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-create_time']
