import csv
from io import TextIOWrapper
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Dataset


class DatasetValidatorSerializer(serializers.ModelSerializer):
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
        reader = csv.DictReader(csv_file, fieldnames=DatasetValidatorSerializer.Meta.fields)

        datasets = []
        saved = 0
        i = 0
        try:
            for row in reader:
                if i == 0 and set(list(row.values())).issubset(set(reader.fieldnames)):
                    i += 1
                    continue
                i += 1

                gender = Dataset.Gender.UNKNOWN  # Default to UNKNOWN if gender is not specified
                if row.get('gender'):
                    if row.get('gender').lower() == Dataset.Gender.FEMALE.label.lower():
                        gender = Dataset.Gender.FEMALE
                    elif row.get('gender').lower() == Dataset.Gender.MALE.label.lower():
                        gender = Dataset.Gender.MALE

                datasetSerializer = DatasetValidatorSerializer(data={"category": row.get('category'),
                                                                     "firstname": row.get('firstname'),
                                                                     "lastname": row.get('lastname'),
                                                                     "email": row.get('email'),
                                                                     "gender": gender,
                                                                     "birthDate": row.get('birthDate'), }
                                                               )

                if datasetSerializer.is_valid():
                    dataset = Dataset(**datasetSerializer.validated_data)
                    datasets.append(dataset)
                    saved += 1

        except:
            raise serializers.ValidationError("file corrupted")

        try:
            Dataset.objects.bulk_create(datasets)
        except:
            raise serializers.ValidationError("something went wrong")

        return {"response": f"{i} rows were processed.{saved} data rows parsed and saved successfully."}

    def to_representation(self, instance):
        return self.instance
