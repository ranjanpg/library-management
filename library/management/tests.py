from rest_framework.test import APIRequestFactory
from typing import List, Dict

from .models import *

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

factory = APIRequestFactory()