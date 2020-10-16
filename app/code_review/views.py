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
import hashlib


def check_libs(file_obj, ext, ql_info_obj):
    allowed_libs = ql_info_obj[ext]['libs']
    imp_kword = ql_info_obj[ext]['keyword']

    for line in file_obj:
        cleaned_line = line.decode("utf-8").strip('\n')
        if cleaned_line.startswith(imp_kword):
            if cleaned_line.split(" ")[1] not in allowed_libs:
                return False
        elif cleaned_line != '\n':
            break
    return True


class CodeValidation(APIView):

    def run_prog(request, ext, inpath, outpath, samplepath):
        def check_output(samplepath, outpath):
            with open(outpath, 'r') as f1:
                stripped_sub = f1.read().replace('\n', '').replace(" ", "")

            hash_sub = hashlib.md5(stripped_sub.encode()).hexdigest()
            
            with open(samplepath, 'r') as f2:
                hash_samp = f2.read()  
            
            return hash_samp == hash_sub
            

        def run_c():
            try:
                subprocess.Popen(["gcc {0}".format(inpath)], shell=True).wait()
            except Exception as e:
                print(str(e))
                return False
            try: 
                subprocess.Popen(["./a.out > {0}".format(outpath)], shell=True).wait()
            except Exception as e:
                print(str(e))
                return False

            return check_output(samplepath, outpath)

            
        def run_py():
            try: 
                subprocess.Popen(["python {0} > {1}".format(inpath, outpath)], shell=True).wait()
            except Exception as e:
                print(str(e))
                return False
            
            return check_output(samplepath, outpath)

        def run_rb():
            pass
        def run_java():
            pass
        def run_cpp():
            pass

        ext_case = {'c': run_c, 'py': run_py, 'java': run_java, 'rb': run_rb, 'cpp': run_cpp}
        return ext_case[ext]()


    def get(self, request):
        
        infopath = os.path.join(settings.BASE_DIR, 'static/json/dql.json')
        with open(infopath, 'r') as f:
            dummy_json_string = f.read()
        return Response(dummy_json_string, status=status.HTTP_200_OK)

    def post(self, request):

        infopath = os.path.join(settings.BASE_DIR, 'static/json/dql.json')
        with open(infopath, 'r') as f:
            dummy_json = json.loads(f.read())

        l20p1info = dummy_json['20']['p1']['languages']
        form = app_forms.UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            
            file_obj = request.FILES['upload_file']
            inpath = os.path.join(settings.BASE_DIR, 'static/uploaded_progs/', file_obj.name)
            basename, ext = file_obj.name.split('.')
            resp = 'Congratulations, your submission was valid...!'
            if not check_libs(file_obj, ext, l20p1info):
                resp = 'Invalid sumbission: use of unavailable library'
                return Response(resp, status=status.HTTP_200_OK)
            with open(inpath, 'w') as f:
                for line in file_obj:
                    cleaned_line = line.decode("utf-8")
                    f.write(cleaned_line)
            outpath = os.path.join(settings.BASE_DIR, 'static/uploaded_progs/output/', basename + ext + '.txt')
            samplepath = os.path.join(settings.BASE_DIR, 'static/sample_outputs/', basename + '_hash.txt')

            if self.run_prog(ext, inpath, outpath, samplepath):
                return Response(resp, status=status.HTTP_200_OK)
            else:
                resp = 'Oops! Incorrect output, please try again'
                return Response(resp, status=status.HTTP_200_OK)
        else:
            form = app_forms.UploadFileForm()
            return render(request, 'index.html', {'form': form})



