from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

# from goods.models import Goods
# Create your models here.
User = get_user_model()

from DjangoUeditor.models import UEditorField
class Office(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="处室名称", help_text="处室名称",unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "处室"
        verbose_name_plural = verbose_name

class Employee(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="教师名", help_text="教师名",unique=True)
    phone=models.CharField(verbose_name="电话号码", help_text="电话号码", max_length=11, default='', blank=True, null=True)
    # office = models.ForeignKey(Office, null=True, blank=True, verbose_name="处室名称",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# class UserFav(models.Model):
#     """
#     用户收藏
#     """
#     employee=models.ForeignKey(Employee, verbose_name="用户",null=True, blank=True)
#     # user = models.ForeignKey(User, verbose_name="用户",null=True, blank=True,)
#     goods = models.ForeignKey(Goods, verbose_name="电脑", help_text="电脑SN")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#     contract_image = models.ImageField(upload_to="user_operation/images/", null=True, blank=True, verbose_name="协议书")
#     class Meta:
#         verbose_name = '使用登记'
#         verbose_name_plural = verbose_name
#         unique_together = ("employee", "goods")
#
#     def __str__(self):
#         return str(self.goods)

