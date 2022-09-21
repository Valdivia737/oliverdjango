from django.urls import path
from webapp_2 import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('harry1', views.harry1, name = 'harry1'),
    path('harry2', views.harry2, name = 'harry2'),
    path('harry3', views.harry3, name = 'harry3'),
    path('harry4', views.harry4, name = 'harry4'),
    path('harry5', views.harry5, name = 'harry5'),
    path('harry6', views.harry6, name = 'harry6'),
]