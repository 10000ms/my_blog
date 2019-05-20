使用新的思路进行blog制作

1. 前后端分离：前端vue，后端django
2. 使用更多的其他技术增加blog功能

# 运行说明

1. 启动后端
```
python manage.py runserver 8000
```
2. 后端目录下启动celery
```
celery -A my_blog worker -l info -P eventlet
```



# 返回码定义

1. 200：成功
2. 400：错误请求（错误参数等）
3. 403：没有对应请求权限
4. 404：未找到对应请求资源
5. 500：服务器内部错误

其他错误码参考django rest framework的错误码：[官方文档地址](https://www.django-rest-framework.org/api-guide/status-codes/)

# 后端model防止错误的循环引用

1. model类的ForeignKey内的使用字符串
2. manager类不要引用model类，要使用自身model类的relation field的model的时候，使用self.model.{{relation field}}.field.remote_field.model获得对应model类

# mysql数据库

建表语句
```
CREATE DATABASE  `my_blog` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

# 备注
## 百度地图AK
直接百度地图开发者中心注册帐号，创建应用即可获得AK

## 后端机密信息
后端机密信息信息存放在后端根目录下的`secret.py`文件里，这个文件不会被git同步，需要自行添加。

机密信息内容包括：
```
# django秘钥
SECRET_KEY = 

# 数据库用户及密码
DATABASE_ACCOUNT = 
DATABASE_PASSWORD = 

# 百度AK密匙，用于获取IP的经纬度
BAIDU_AK = 
```

## ip与位置
1. ~~ ip搜索比较消耗时间，所以可以选择关闭 ~~ 使用celery改为异步处理
2. ip对应地址使用本地搜索，提高效率
3. 城市经纬度使用baidu map的api进行，获取匹配前端百度地图的结果
4. TODO：使用异步任务拆分这部分功能

## 前端机密信息
后端机密信息信息存放在后端根目录下的`secret.py`文件里，这个文件不会被git同步，需要自行添加。

```
export default {
	// 百度地图ak
    baiduMapAK: 
}
```
