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


# 备注
## 后端机密信息
后端机密信息信息存放在后端根目录下的`secret.py`文件里，这个文件不会被git同步，需要自行添加。

机密信息内容包括：
```
# django秘钥
SECRET_KEY = 

# 数据库用户及密码
DATABASE_ACCOUNT = 
DATABASE_PASSWORD = 
```

## 前端机密信息
后端机密信息信息存放在后端根目录下的`secret.py`文件里，这个文件不会被git同步，需要自行添加。

```
export default {
	// 百度地图ak
    baiduMapAK: 
}
```