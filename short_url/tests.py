from django.test import TestCase
from .models import URL
from collections import OrderedDict
from rest_framework import status
from hashlib import md5


class GDUURLViewTest(TestCase):
    def setUp(self):
        self.client.login(username='test', password='1234test')

    def test_get_correct_url(self):
        self.url = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url.save()
        response = self.client.get(
            '/{0}'.format(md5(self.url.base_url.encode()).hexdigest()[:10]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_get_wrong_url(self):
        self.url = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url.save()
        response = self.client.get(
            '/{0}'.format(md5(self.url.base_url.encode()).hexdigest()[:10] + '1'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_correct_url(self):
        self.url = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url.save()
        response = self.client.delete(
            '/{0}'.format(md5(self.url.base_url.encode()).hexdigest()[:10]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_wrong_url(self):
        self.url = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url.save()
        response = self.client.delete(
            '/{0}'.format(md5(self.url.base_url.encode()).hexdigest()[:10] + '1'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GPURLsViewTest(TestCase):
    def setUp(self):
        self.client.login(username='test', password='1234test')

    def test_no_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.data, [])

    def test_one_url(self):
        self.url = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url.save()
        response = self.client.get('/')
        self.assertEqual(response.data, [OrderedDict(
            [('id', 1), ('base_url', 'https://www.pinterest.ru/pin/755901118684940658/')]
        )])

    def test_two_url(self):
        self.url_1 = URL(
            base_url='https://www.pinterest.ru/pin/755901118684940658/'
        )
        self.url_1.save()
        self.url_2 = URL(
            base_url='https://www.youtube.com/watch?v=8YWTW9YLJW0'
        )
        self.url_2.save()
        response = self.client.get('/')
        self.assertEqual(response.data, [
            OrderedDict(
                [('id', 1), ('base_url', 'https://www.pinterest.ru/pin/755901118684940658/')]
            ),
            OrderedDict(
                [('id', 2), ('base_url', 'https://www.youtube.com/watch?v=8YWTW9YLJW0')]
            ),
        ]
        )

    def test_true_full_url(self):
        response = self.client.post(
            '', {'base_url': 'http://mapandwordsstartingwithj.appspot.com/index.php?a=jrek'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_full_url(self):
        response = self.client.post(
            '', {'base_url': 'www.youtube.com/watch?v=8YWTW9YLJW0'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
