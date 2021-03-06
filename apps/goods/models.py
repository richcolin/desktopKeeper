from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
from user_operation.models import Employee,Office
from users.models import UserProfile
class GoodsCategory(models.Model):
    """
    设备类别
    """
    CATEGORY_TYPE = (
        (1, "台式机"),
        (2, "笔记本电脑"),
        (3, "平板设备"),
        (4,"路由器"),
        (5,"交换机"),
        (6,"其他")
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")

    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别",blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "设备类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="物品类目",on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="品牌", help_text="品牌",blank=True, null=True)
    brand_image = models.ImageField(upload_to="brand/images/", null=True, blank=True, verbose_name="实物图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌" 
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    设备
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="类目",on_delete=models.CASCADE)
    brand=models.ForeignKey(GoodsCategoryBrand,verbose_name="设备品牌",on_delete=models.CASCADE,blank=True, null=True)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="设备唯一SN号")
    name = models.CharField(max_length=100, verbose_name="设备名")
    employee=models.ForeignKey(Employee, verbose_name="使用教师",null=True, blank=True)
    office=models.ForeignKey(Office,verbose_name='处室名称',null=True,blank=True)
    goods_brief = models.TextField(max_length=500, verbose_name="设备简短描述")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="协议书")
    is_new = models.BooleanField(default=False, verbose_name="是否正在使用")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0},sn({1})".format(self.name,self.goods_sn)
class GoodsImage(models.Model):
    """
    设备轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="设备", related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '设备图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
