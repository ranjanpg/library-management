from rest_framework.test import APIRequestFactory
from typing import List, Dict

from .models import *
from csv import reader

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class BookTests(APITestCase):
    def test_add_book(self):
        """
        Ensure we can create a new book object.
        """
        url = reverse('book-list')
        print(url)
        author = Author.objects.get(name='test-author')
        data = {'title': 'test-book', 'author': author}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()

def test_addBooks():
    with open('data/Library_Books.csv', 'r') as fh:
        r = reader(fh)
        for row in r:
            data = {'title': row[0], 'author': row[1]}
            factory.post('/books/', data=data)

def test_addAuthors():
    with open('data/Library_Authors.csv', 'r') as fh:
        r = reader(fh)
        for row in r:
            factory.post('/authors/', data={'name': row[0]})

def test_addMembers():
    with open('data/Library_Members.csv', 'r') as fh:
        r = reader(fh)
        for row in r:
            factory.post('/members/', data={'name': row[0]})

test_addBooks()
test_addAuthors()
test_addMembers()