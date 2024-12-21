from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict-crop/', views.predict_crop, name='predict_crop'),
]
