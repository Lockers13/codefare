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
from rest_framework.views import APIView




class CodeValidation(APIView):
    def get(self, request):
        return Response("hello", status=status.HTTP_200_OK)

    def post(self, request):

        file_obj = request.FILES['file-upload']
        resp = 'Valid'

        for line in file_obj:
            cleaned_line = line.decode("utf-8").strip('\n')
            if cleaned_line.startswith("#include <stdlib.h>"):
                resp = 'Invalid: use of unavailable library'
                return Response(resp, status=status.HTTP_200_OK)
            if cleaned_line.startswith("int main"):
                break

        # do some stuff with uploaded file
        return Response(resp, status=status.HTTP_200_OK)
    



