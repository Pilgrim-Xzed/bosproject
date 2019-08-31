from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('documents/',views.documents),
    path('works/',views.works),
    path('publications/',views.publications),
    path('download/<docid>',views.downloads),
    path('budget/<year>',views.budgetyr)
]