from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from .models import Snippet
# Create your tests here.


class SnippetTestCase(TestCase):
    '''
    Class to test the Snippet Model
    '''

    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create_user(username='name1')
        self.user2 = User.objects.create_user(username='name2')
        self.snippet1 = Snippet(owner=self.user1)
        self.snippet2 = Snippet(owner=self.user2)

    def test_can_model_create_snippet(self):
        ''' test whether the model actually creates a snippet '''
        old_count = Snippet.objects.count()
        self.snippet1.save()
        new_count = Snippet.objects.count()
        self.assertEqual(old_count + 1, new_count)

    def test_created_snippet_equals_api_delivered_snippet(self):
        ''' test whether the created snippet and a snippet retrieved
        from the api has the same value
        '''
        snippet = Snippet(owner=self.user1)
        api_get = self.client.get('/snippets/', kwargs={'pk': snippet.id})
        print(snippet.title)
    
    def test_pull_request_to_learn_github(self):
        ''' this just passes '''
        pass
        
