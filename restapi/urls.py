from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('view/', views.view_blog),
    path('view/<str:pk>', views.blog_detail),
    path('create/', views.create_blog),
]