from django.http import HttpResponse
from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from dataset.filters import DatasetFilter
from dataset.models import Dataset
from dataset.serializers import InsertDatasetSerializer
from dataset.utils import dataset_to_csv


class PushDatasetView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = InsertDatasetSerializer


class ExportCSVView(generics.ListAPIView):
    queryset = Dataset.objects.all()
    filterset_class = DatasetFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="dataset.csv"'},
        )

        dataset_to_csv(queryset, response)
        return response


