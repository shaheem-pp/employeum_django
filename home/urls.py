from django.urls import include, path
from home.views import home

urlpatterns = [
		path('', home.index),
]
