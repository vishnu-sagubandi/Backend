from .test_setup import TestSetUp
from user.models import User, Profile
from django.urls import reverse
from rest_framework.test import APIClient
from lists.models import Solved
from problem.models import Problem


class TestViews(TestSetUp):

    #anon checking of list of all ladders and list endpoints
    def test_check_topicwise_list_all_lists_view(self):
        test_url = reverse('topicwise-list')
        res = self.client.get(test_url)
        self.assertEqual(res.status_code, 200)

    def test_check_topicwise_ladder_all_ladders_view(self):
        test_url = reverse('topicwise-ladder')
        res = self.client.get(test_url)
        self.assertEqual(res.status_code, 200)

    def test_check_levelwise_list_all_lists_view(self):
        test_url = reverse('levelwise-list')
        res = self.client.get(test_url)
        self.assertEqual(res.status_code, 200)

    def test_check_levelwise_ladder_all_ladder_view(self):
        test_url = reverse('levelwise-ladder')
        res = self.client.get(test_url)
        self.assertEqual(res.status_code, 200)


#checking lists with an authenticated user

    def test_auth_check_topicwise_list_view(self):
        test_url = reverse('topicwise-list') + "testinglist_topicwise"
        here = User.objects.get(username="testing")
        here.set_password(self.user_data['password'])
        here.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        token = res.data['tokens']['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = client.get(test_url, format="json")
        ok = True
        for ele in res.data['result']:
            if list(ele.values())[12]:
                prob_id = list(ele.values())[2]
                problem = Problem.objects.get(prob_id=prob_id)
                if not Solved.objects.filter(user=here,
                                             problem=problem).exists():
                    ok = False
                    break
        self.assertEqual(res.status_code, 200) and self.assertEqual(ok, True)

    def test_auth_check_topicwise_ladder_view(self):
        test_url = reverse('topicwise-ladder') + "testinglist_topicwise"
        here = User.objects.get(username="testing")
        here.set_password(self.user_data['password'])
        here.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        token = res.data['tokens']['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = client.get(test_url, format="json")
        ok = True
        for ele in res.data['result']:
            if list(ele.values())[12]:
                prob_id = list(ele.values())[2]
                problem = Problem.objects.get(prob_id=prob_id)
                if not Solved.objects.filter(user=here,
                                             problem=problem).exists():
                    ok = False
                    break
        self.assertEqual(res.status_code, 200) and self.assertEqual(ok, True)

    def test_auth_check_levelwise_list_view(self):
        test_url = reverse('levelwise-list') + "testinglist_levelwise"
        here = User.objects.get(username="testing")
        here.set_password(self.user_data['password'])
        here.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        token = res.data['tokens']['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = client.get(test_url, format="json")
        ok = True
        for ele in res.data['result']:
            if list(ele.values())[12]:
                prob_id = list(ele.values())[2]
                problem = Problem.objects.get(prob_id=prob_id)
                if not Solved.objects.filter(user=here,
                                             problem=problem).exists():
                    ok = False
                    break
        self.assertEqual(res.status_code, 200) and self.assertEqual(ok, True)

    def test_auth_check_levelwise_ladder_view(self):
        test_url = reverse('levelwise-ladder') + "testinglist_levelwise"
        here = User.objects.get(username="testing")
        here.set_password(self.user_data['password'])
        here.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        token = res.data['tokens']['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = client.get(test_url, format="json")
        ok = True
        for ele in res.data['result']:
            if list(ele.values())[12]:
                prob_id = list(ele.values())[2]
                problem = Problem.objects.get(prob_id=prob_id)
                if not Solved.objects.filter(user=here,
                                             problem=problem).exists():
                    ok = False
                    break
        self.assertEqual(res.status_code, 200) and self.assertEqual(ok, True)

    def test_auth_check_userlists_view(self):
        slug = "testinglist_levelwise"
        test_url = reverse('userlist-edit', kwargs={'slug': slug})
        here = User.objects.get(username="testing")
        here.set_password(self.user_data['password'])
        here.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        token = res.data['tokens']['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = client.get(test_url, format="json")
        ok = True
        for ele in res.data['result']:
            if list(ele.values())[12]:
                prob_id = list(ele.values())[2]
                problem = Problem.objects.get(prob_id=prob_id)
                if not Solved.objects.filter(user=here,
                                             problem=problem).exists():
                    ok = False
                    break
        self.assertEqual(res.status_code, 200) and self.assertEqual(ok, True)
