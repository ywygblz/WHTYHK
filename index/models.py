from django.db import models


# Create your models here.

class AirlineUser(models.Model):
    """航司账号"""
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 使用时间
    state = models.CharField(max_length=50)  # 状态
    remark = models.CharField(max_length=50)  # 备注
    proxy = models.CharField(max_length=50)  # 代理
    source = models.CharField(max_length=50)  # 来源
    admin = models.CharField(max_length=20)  # 操作人

