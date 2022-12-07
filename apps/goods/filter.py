from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte', help_text='最低价格')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    top_category = filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value)).order_by('id')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'top_category', 'is_hot', 'is_new']
