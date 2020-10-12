from django.urls import path, include
from app import views as index_views
from . import views as cr_views

urlpatterns = [
	path('validate/', cr_views.CodeValidation.as_view(), name="code_validation"),
]

