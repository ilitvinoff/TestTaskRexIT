from django.urls import path

from dataset.views import ExportCSVView, PushDatasetView

urlpatterns = [
    path('push/', PushDatasetView.as_view(), name='push-csv'),
    path('pull/', ExportCSVView.as_view(), name='pull-csv'),
]
