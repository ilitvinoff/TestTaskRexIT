import csv


def dataset_to_csv(queryset, file):
    fields = ['category', 'firstname', 'lastname', 'email', 'gender', 'birthDate']
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    for dataset in queryset:
        writer.writerow({
            'category': dataset.category if dataset.category else "",
            'firstname': dataset.firstname if dataset.firstname else "",
            'lastname': dataset.lastname if dataset.lastname else "",
            'email': dataset.email if dataset.email else "",
            'gender': dataset.get_gender_display() if dataset.get_gender_display() else "",
            'birthDate': dataset.birthDate if dataset.birthDate else "",
        })

