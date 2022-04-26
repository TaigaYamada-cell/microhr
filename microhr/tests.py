from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.test import TestCase, RequestFactory

from microhr.views import company

UserModel = get_user_model()

class WorkCreateViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='t-aiga', is_company=True, is_worker=False, email='taiga@example.com', password='secret'
        )

    def test_should_return_200_if_sending_get_request(self):
        request = self.factory.get("/endpoint/of/work_new")
        request.user = self.user
        response = company.work_new(request)
        self.assertEqual(response.status_code, 200)

    def test_should_redirect_if_user_does_not_login(self):
        request = self.factory.get("/endpoint/of/work_new")
        request.user = AnonymousUser()
        response = company.work_new(request)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_should_return_302_if_sending_valid_post_request(self):
        request = self.factory.post("/endpoint/of/work_new", data={
            'title': 'test, test, test!',
            'company': self.user,
            'salary_max': 15,
            'salary_min': 10,
            'text': 'テストの求人',
        })
        request.user = self.user
        response = company.work_new(request)
        self.assertEqual(response.status_code, 302)