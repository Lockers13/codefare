from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
#from . import forms as cr_forms
import os
import os.path
import json
from rest_framework import status
from rest_framework.response import Response
#from django.contrib.staticfiles.storage import staticfiles_storage
import sys
import requests
#from sqlalchemy import create_engine, event
#import pymysql
#from sqlalchemy.sql import text
#import datetime
# from datetime import datetime
from app import settings

class CodeValidation(generics.RetrieveAPIView):
    queryset = ''

    def get(self, request):
        return Response("hello", status=status.HTTP_200_OK)

