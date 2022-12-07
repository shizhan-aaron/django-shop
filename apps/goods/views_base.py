import json

from django.core.serializers import serialize
from django.views.generic.base import View
from django.http import JsonResponse

from goods.models import Goods


class GoodListView(View):
    def get(self, request):
        """
        商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
