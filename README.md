# US Visa Approval Prediction MLOps Production Pipeline

## Introduction

This project aims to develop a machine learning model capable of predicting the approval status of US visa applications. By implementing a comprehensive MLOps pipeline, the project ensures efficient model development, deployment, and monitoring, resulting in a robust and scalable solution.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Project Structure

The repository is organized as follows:
- `.github/workflows/`: Contains GitHub Actions workflows for CI/CD.
- `config/`: Configuration files for the project.
- `notebook/`: Jupyter notebooks for data exploration and analysis.
- `static/css/`: CSS files for the web interface.
- `templates/`: HTML templates for the web interface.
- `us_visa/`: Core package containing modules for data ingestion, validation, transformation, and model training.
- `.dockerignore`: Specifies files and directories to ignore in Docker builds.
- `.gitignore`: Specifies files and directories to ignore in Git.
- `Dockerfile`: Instructions to build the Docker image.
- `LICENSE`: License information.
- `README.md`: Project documentation.
- `app.py`: Entry point for the web application.
- `demo.py`: Script for demonstrating the model.
- `requirements.txt`: Python dependencies.
- `setup.py`: Setup script for the Python package.
- `template.py`: Template script for various utilities.

## Installation

To set up the project locally, follow these steps:
1. Clone the repository: 
git clone https://github.com/vijaybalamahalingam US-Visa-Approval-Prediction-MLOps-Production-Pipeline.git
cd US-Visa-Approval-Prediction-MLOps-Production-Pipeline
2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies:
pip install -r requirements.txt

## Usage

To run the web application:

python app.py

## Features
- **Data Ingestion:** Fetches and stores visa application data.
- **Data Validation:** Ensures data integrity and quality.
- **Data Transformation:** Preprocesses data for model training.
- **Model Training:** Trains machine learning models to predict visa approval.
- **Model Evaluation:** Assesses model performance using various metrics.
- **Model Deployment:** Deploys the model as a web service.
- **CI/CD Pipeline:** Automates testing, building, and deployment processes.

## Dependencies

The project relies on the following key technologies:
- **Python:** Core programming language for development.
- **Jupyter Notebook:** For data exploration and analysis.
- **MongoDB:** Database for storing application data.
- **Evidently AI:** For monitoring and analyzing data drift, concept drift, and other model performance metrics.
- **FastAPI:** Web framework for building the API.
- **Docker:** Containerization platform for deployment.
- **AWS Services:** Including S3 for storage and EC2 for hosting.
- **GitHub Actions:** For continuous integration and deployment.

## Configuration

Before running the application, ensure that the following environment variables are set:
- `MONGODB_URL`: Connection string for MongoDB.
- `AWS_ACCESS_KEY_ID`: AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: AWS secret access key.
- `AWS_DEFAULT_REGION`: AWS region.

## Troubleshooting

If you encounter issues during installation or execution, consider the following steps:
- Ensure all dependencies are installed correctly.
- Verify that environment variables are set appropriately.
- Check the configuration files for any missing or incorrect settings.
- Consult the logs for error messages and stack traces.

## Contributors
- [Vijay Bala Mahalingam](https://github.com/vijaybalamahalingam)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.