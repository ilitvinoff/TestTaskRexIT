### Task Description:
```

You need to upload the project to a public repository in gitlab
The test project must be run in docker
You need to create a readme page about starting and using the project

Develop a service for working with a dataset

Initial data:
.csv dataset
     'category', // client's favorite category
     'firstname',
     'lastname',
     'email',
     'gender',
     'birthDate'

Without using third party libraries:
Read csv file.

Write the received data to the database.

Use a simple json api with Swagger

Implement filters by values:
     category
     gender
     Date of Birth
     age
     age range (for example, 25 - 30 years)

Implement data export (in csv) according to the specified filters.
```

# Dataset Service
This project is a Django-based service for working with a dataset. It allows users to upload a CSV dataset, parse it, and save the data to a database. Additionally, it provides a simple JSON API with Swagger documentation for accessing and filtering the dataset.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ilitvinoff/TestTaskRexIT.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Test_Task_rexIT
    ```

3. Build and run the Docker container:

    ```bash
    docker-compose up --build
    ```

4. Access the API documentation and interact with the service by visiting:

    ```bash
    http://localhost:8000/swagger/
    ```

## Usage

### Uploading a Dataset

To upload a dataset, send a POST request to the `  push/` endpoint with the CSV file as the request body.

### Filtering Data and Exporting Data

The API allows filtering the dataset by various criteria, including:

- Category
- Firstname
- Lastname
- Email
- Gender
- Age
- Age Range
- Date of Birth
- Date of Birth Range

Send GET requests to the `pull/` endpoint with query parameters to apply filters.

## Dependencies

The project relies on the following technologies and frameworks:

- Django: Web framework for building the backend
- Django Rest Framework (DRF): Toolkit for building RESTful APIs
- Swagger: Documentation tool for describing and visualizing the API
- Docker: Containerization platform for easy deployment and scalability
- 

