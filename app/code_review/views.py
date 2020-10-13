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
from django.contrib.staticfiles.storage import staticfiles_storage
import subprocess


dummyQ_dict = {'l20': {
    'p1': {'desc': 'Build a Web Server',
            'languages': {
                'py': {'keyword': 'import', 'score': 10, 'libs':['os', 'sys', 'urllib', 'json', 'requests']},
                'c': {'keyword': '#include', 'score': 50, 'libs': ['<stdio.h>', '<stdlib.h>']},
                'cpp': {'keyword': '', 'score': 40, 'libs': []}, 
                'rb': {'keyword': 'require', 'score': 20, 'libs': []}, 
                'java': {'keyword': 'import', 'score': 30, 'libs': []}
            }
        }
    }
}

def check_libs(file_obj, ext, ql_info_obj):
    allowed_libs = ql_info_obj[ext]['libs']
    imp_kword = ql_info_obj[ext]['keyword']

    for line in file_obj:
        cleaned_line = line.decode("utf-8").strip('\n')
        print(cleaned_line)
        if cleaned_line.startswith(imp_kword):
            if cleaned_line.split(" ")[1] not in allowed_libs:
                return False
        elif cleaned_line != '\n':
            break
    return True




class CodeValidation(APIView):
    def get(self, request):
        
        path = os.path.join(settings.BASE_DIR, 'static/json/dql.json')
        print(path)
        with open(path, 'r') as f:
            dummy_json_string = f.read()
        return Response(dummy_json_string, status=status.HTTP_200_OK)

    def post(self, request):
        path = os.path.join(settings.BASE_DIR, 'static/uploaded_progs/')


        l20p1info = dummyQ_dict['l20']['p1']['languages']
        form = app_forms.UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file_obj = request.FILES['upload_file']
            path = os.path.join(settings.BASE_DIR, 'static/uploaded_progs/', file_obj.name)
            print("PATH =", path)
            basename, ext = file_obj.name.split('.')
            resp = 'Congratulations, your submission was valid...!'
            if not check_libs(file_obj, ext, l20p1info):
                resp = 'Invalid sumbission: use of unavailable library'
                return Response(resp, status=status.HTTP_200_OK)
            with open(path, 'w') as f:
                for line in file_obj:
                    cleaned_line = line.decode("utf-8")
                    f.write(cleaned_line)
            sp1 = subprocess.Popen(["gcc {0}".format(path)], shell=True)
            sp1.wait()
            sp2 = subprocess.Popen(["./a.out > {0}".format(path)], shell=True)
            sp2.wait()
            return Response(resp, status=status.HTTP_200_OK)
        else:
            form = app_forms.UploadFileForm()
            return render(request, 'index.html', {'form': form})



