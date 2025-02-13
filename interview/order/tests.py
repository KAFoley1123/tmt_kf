from rest_framework.test import APITestCase
from order.models import Order, OrderTag
from django.urls import reverse

class TestOrderTagListView(APITestCase):
    def setUp(self):
        # create sample order/order tag models here
        self.list_url = reverse('url for endpoint')
        self.sample_order_tag = OrderTag.objects.create()
        self.sample_order = Order.objects.create(tags=self.sample_order_tag)

    def test(self):
        data = {'order_id': self.sample_order.id}
        response = self.client.get(self.list_url, data, format='json')
        # assert response contains expected order_tags

    # test case for invalid data entry
    # test case for no orders found
    # test case for no order tags associated with the order
    # test case for multiple tags found for order