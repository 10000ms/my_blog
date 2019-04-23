使用新的思路进行blog制作

1. 前后端分离：前端vue，后端django
2. 使用更多的其他技术增加blog功能


# 返回码定义

1. 200：成功
2. 400：错误请求（错误参数等）
3. 403：没有对应请求权限
4. 404：未找到对应请求资源
5. 500：服务器内部错误

# 后端model防止错误的循环引用

1. model类的ForeignKey内的使用字符串
2. manager类不要引用model类，要使用自身model类的relation field的时候，使用self.relation_field.model来获取相关联的model
