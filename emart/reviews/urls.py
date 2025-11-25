from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_home, name='review_home'),
]
