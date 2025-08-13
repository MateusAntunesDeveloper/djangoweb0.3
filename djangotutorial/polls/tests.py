from django.test import TestCase, Client
from django.utils import timezone
import selenium.webdriver
from .models import Quest
import datetime
from django.urls import reverse
import time
import selenium


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Quest(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_publishedOld(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Quest(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_publishedNew(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Quest(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
    def test_client(self):
        self.client = Client()
        time = timezone.now() - datetime.timedelta(hours=1)
        recentQ = Quest(pub_date=time)
        test_clients = self.assertIs(recentQ.was_published_recently(), time)
        self.assertIs(test_clients, True)


    def urlsTest(self):
        self.response = self.client.get("/")
        self.response.status_code
        self.response.content
        self.response.context["latest_question_list"]
        

class HerderByClass(QuestionModelTest):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
    def start(self):
        self.browser = selenium.webdriver
        return self.browser


    






