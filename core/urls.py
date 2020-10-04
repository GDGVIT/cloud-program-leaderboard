from django.urls import path
from . import views
urlpatterns = [
    path('', views.GetAllUserList.as_view()),
]