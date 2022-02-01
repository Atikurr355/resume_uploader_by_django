from django.urls import path

from .import views

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('candidate/<str:pk>/', views.CandidateView.as_view(), name='candidate'),
]