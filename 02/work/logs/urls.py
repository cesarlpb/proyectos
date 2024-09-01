from django.urls import path
from logs.views import WorkLogCreateView, WorkLogListView 

urlpatterns = [
    path('', WorkLogListView.as_view(), name='log_list'),
    path('create/', WorkLogCreateView.as_view(), name='log_create'),
]
