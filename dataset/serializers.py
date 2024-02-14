import csv
from io import TextIOWrapper
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Dataset


class DatasetSwaggerRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['category', 'firstname', 'lastname', 'email', 'gender', 'birthDate']


class InsertDatasetSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    http_methods = ["post"]

    def validate_file(self, value):
        if not value.name.endswith('.csv'):
            raise ValidationError("Only CSV files are allowed.")
        return value

    def create(self, validated_data):
        csv_file = TextIOWrapper(validated_data['csv_file'].file, encoding='utf-8')
        reader = csv.DictReader(csv_file)

        datasets = []
        try:
            for row in reader:
                gender = Dataset.Gender.UNKNOWN  # Default to UNKNOWN if gender is not specified
                if row['gender'].lower() == 'female':
                    gender = Dataset.Gender.FEMALE
                elif row['gender'].lower() == 'male':
                    gender = Dataset.Gender.MALE

                dataset = Dataset(
                    category=row.get('category'),
                    firstname=row.get('firstname'),
                    lastname=row.get('lastname'),
                    email=row.get('email'),
                    gender=gender,
                    birthDate=row.get('birthDate'),
                )
                datasets.append(dataset)
        except:
            return {"error": f"file corrupted"}

        try:
            Dataset.objects.bulk_create(datasets)
        except:
            return {"error": f"something went wrong"}

        return {"response": f"{reader.line_num} rows were processed"}

    def to_representation(self, instance):
        return self.instance
