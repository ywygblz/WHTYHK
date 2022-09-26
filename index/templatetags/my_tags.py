from datetime import datetime
import time
from django import template

# 下面代码会直接使用register
register = template.Library()

# @register.filter
def time_format(value):
    """时间格式化"""
    if type(value)==datetime:
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value

register.filter(time_format)