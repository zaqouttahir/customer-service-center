from django.urls import path

from llm import views

urlpatterns = [
    path('tool-calls/', views.ToolCallLogListView.as_view(), name='toolcalllog-list'),
]
