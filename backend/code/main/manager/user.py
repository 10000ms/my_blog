import uuid

from django.contrib.auth.models import UserManager
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError as BaseValidationError
from django.contrib.auth import (
    authenticate,
    login,
)

from rest_framework.exceptions import ValidationError

from ..validator.auth import (
    validate_name,
    validate_username_password,
    validate_phone,
)


class CustomUserManager(UserManager):

    def demo_login(self, request):
        u = self.filter(is_demo_user=True)
        if u.exists():
            u = u[0]
        else:
            u = self.create_user(
                username=uuid.uuid4().hex[:6],
                password=uuid.uuid4().hex[:6],
                first_name='user',
                last_name='demo',
                phone=uuid.uuid4().hex[:12],
                email='{}@demo-user.com'.format(uuid.uuid4().hex),
                is_demo_user=True,
            )
            u.save()
        login(request, u)
        return True

    def create_superuser(self, username, email, password, **extra_fields):
        """
        重写改方法，使得superuser自动成为author
        """
        r = super().create_superuser(username, email, password, **extra_fields)
        r.is_author = True
        r.save()
        return r

    @staticmethod
    def custom_login(request):
        """
        登陆功能
        """
        if 'username' not in request.data or 'password' not in request.data:
            raise ValidationError('必须含有username, password')
        # 验证一下
        u = request.data['username']
        p = request.data['password']
        try:
            validate_username_password(u)
            validate_username_password(p)
        except BaseValidationError as e:
            raise ValidationError(e.messages)
        if not request.user.is_authenticated:
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
            else:
                raise ValidationError('用户名或密码错误')
        return True

    def custom_register(self, request):
        """
        注册功能
        """
        need_list = ['username', 'email', 'password', 'first_name', 'last_name', 'phone']
        if list(filter(lambda a: a not in request.data, need_list)):
            raise ValidationError('必须含有{}'.format(','.join(need_list)))
        # 验证一下
        try:
            validate_username_password(request.data['username'])
            validate_username_password(request.data['password'])
            EmailValidator()(request.data['email'])
            validate_phone(request.data['phone'])
            validate_name(request.data['first_name'])
            validate_name(request.data['last_name'])
        except BaseValidationError as e:
            raise ValidationError(e.messages)
        # 重复性检测
        username_user = len(self.filter(username=request.data['username']))
        email_user = len(self.filter(email=request.data['email']))
        phone_user = len(self.filter(phone=request.data['phone']))
        if username_user or email_user or phone_user:
            raise ValidationError('用户名或email或电话重复')
        user = self.create_user(
            username=request.data['username'],
            email=request.data['email'],
            phone=request.data['phone'],
            password=request.data['password'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
        )
        user.save()
        login(request, user)
        return True
