
from .serializers import GoodsSerializer,CategorySerializer
from rest_framework import filters
from .models import Goods,GoodsCategory
from rest_framework import mixins
from .filters import GoodsFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    ceshiyixia
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class=GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields=('sold_num','shop_price')
class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1).order_by('id')
    serializer_class = CategorySerializer
