from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderTagListView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order_id = kwargs['order_id']
        tag_id_list = Order.objects.get(id=order_id).select_related('tags').values_list('tags__id')
        order_tags = self.queryset.filter(id__in=tag_id_list)
        serializer = self.serializer_class(order_tags)

        return Response(serializer.data, status=200)