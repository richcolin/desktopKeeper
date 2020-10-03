#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from .models import Employee,Office
from goods.models import Goods



class EmployeeAdmin(object):
    list_display=['name','phone']
class OfficeAdmin(object):
    list_display=['name']
xadmin.site.register(Employee,EmployeeAdmin)
xadmin.site.register(Office,OfficeAdmin)
