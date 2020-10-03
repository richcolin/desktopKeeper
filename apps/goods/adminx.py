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
from .models import Goods, GoodsCategory, GoodsCategoryBrand


class GoodsAdmin(object):
    list_display = ["name","employee","office","goods_brief", "is_new",  "add_time","brand"]
    search_fields = ['name', ]
    list_filter = ["name", "employee", "office","is_new", "add_time", "category__name","brand"]







class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "add_time"]
    list_filter = ["category_type",  "name"]
    search_fields = ['name', ]


class GoodsBrandAdmin(object):
    list_display = ["category", "name","brand_image"]

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)

xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
