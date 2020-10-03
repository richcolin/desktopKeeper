from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# from .models import UserFav
from goods.serializers import GoodsSerializer

#
# class UserFavDetailSerializer(serializers.ModelSerializer):
#     goods = GoodsSerializer()
#
#     class Meta:
#         model = UserFav
#         fields = ("goods", "id")


# class UserFavSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#
#     class Meta:
#         model = UserFav
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=UserFav.objects.all(),
#                 fields=('user', 'goods'),
#                 message="已经收藏"
#             )
#         ]
#
#         fields = ("user", "goods", "id")
#
