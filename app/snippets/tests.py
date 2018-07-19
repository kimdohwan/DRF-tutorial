import json

from django.test import TestCase

# Create your tests here.
from django.utils.crypto import random
from rest_framework import status, request
from rest_framework.test import APITestCase

from .models import Snippet
from .views import snippet_list


class SnippetListTest(APITestCase):
    """
    Snippet List요청에 대한 테스트
    """

    def test_status_code(self):
        """
        요청 결과의 HTTP 상태코드가 200인지 확인
        :return:
        """
        response = self.client.get('/snippets/django_view/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_snippet_list_count(self):
        """
        Snippet List를 요청시 DB에 있는 자료수와 같은 갯수가 리턴되는지 테스트
        :return:
        """
        Snippet.objects.create(code="it's test time")

        for i in range(random.randint(5, 10)):
            Snippet.objects.create(code=f"a = {i}")

        response = self.client.get('/snippets/django_view/snippets/')
        data = json.loads(response.content)

        self.assertEqual(len(data), Snippet.objects.count())

    def test_snippet_list_order_by_created_descending(self):
        """
        Snippet List의 결과가 생성일자 내림차순인지 확인
        :return:
        """
        for i in range(random.randint(5, 10)):
            Snippet.objects.create(code=f'a= {i}')
        response = self.client.get('/snippets/django_view/snippets/')
        data = json.loads(response.content)

        # 리스트 컴프리헨션을 통해서 간략화한 코드 쓰자
        # snippets = list(Snippet.objects.order_by('-created'))

        # data_pk_list = []
        # for item in data:
        #     data_pk_list.append(item['id'])
        #
        # snippets_pk_list = []
        # for snippet in snippets:
        #     snippets_pk_list.append(snippet.pk)

        self.assertEqual(
            # json 으로 전달받은 데이터에서 pk만 꺼낸 리스트
            [item['id'] for item in data],
            # DB에서 created 역순으로 pk값만 가져온 QuerySet으로 만든 리스트
            list(Snippet.objects.order_by('-created').values_list('pk', flat=True))
        )


class SnippetCreateTest(APITestCase):
    def test_snippet_create_status_code(self):
        """
        201이 돌아오는지
        :return:
        """
        pass

    def test_snippet_create_save_db(self):
        """
        요청후 실제 DB에 잘 저장되어있는지, 필드값이 저장되는
        :return:
        """
        pass

    def test_snippet_create_missing_code_r지aise_exception(self):
        """
        'code'데이터가 주어지지 않을 경우 적절한 Exception이 발생하는지
        :return:
        """
        pass
