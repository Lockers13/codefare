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
from app import forms as app_forms




class CodeValidation(APIView):
    def get(self, request):
        return Response("hello", status=status.HTTP_200_OK)

    def post(self, request):
        form = app_forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['upload_file']
            resp = 'Valid'
            for line in file_obj:
                cleaned_line = line.decode("utf-8").strip('\n')
                print(cleaned_line)
                if cleaned_line.startswith("#include <stdlib.h>"):
                    resp = 'Invalid: use of unavailable library'
                    return Response(resp, status=status.HTTP_200_OK)
                if cleaned_line.startswith("int main"):
                    break
            return Response(resp, status=status.HTTP_200_OK)
        else:
            form = UploadFileForm()
            return render(request, 'index.html', {'form': form})



