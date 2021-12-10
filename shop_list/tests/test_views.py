from django.test import Client
from shop_list.tests.base_test import BaseTest


class ShopListTest(BaseTest):
    def setUp(self):
        shop_list = self.models.ShopList.objects.create(name='Test shop')
        for i in range(1, 1001):
            self.models.Item.objects.create(name=f'Test item {i} from Test shop', shop_list=shop_list)

        self.client = Client()

    def tearDown(self) -> None:
        self.models.Item.objects.all().delete()
        self.models.ShopList.objects.all().delete()

    def test_index(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['sizes']), 3)
        self.assertEqual(len(response.context['shop_lists']), 100)
