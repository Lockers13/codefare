from django.shortcuts import render
from . import forms as index_forms
import datetime
import requests
import json
import os

def index(request):
	
	form = index_forms.UploadFileForm(initial={'title': 'C_level1'})
	
	context = {'title': 'Codefare | Home',
				'form': form}


	return render(request, 'index.html', context)