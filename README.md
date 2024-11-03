E-commerce Backend
Description
Project Setup

First, clone the project to your local machine:

bashCopygit clone git@github.com:HalilPamukk/e-commerce.git

Navigate to the project directory
Create a virtual environment:

bashCopypython3 -m venv venv

Activate the virtual environment:

bashCopysource venv/bin/activate

Copy .env.example file as .env and fill in the required information

Docker Setup

If Docker Desktop is not installed, download and install it from:


Docker Desktop


Open Docker Desktop
Navigate to the project directory in terminal and run the project using one of these commands:

bashCopy# For first time setup (might take some time):
docker-compose up --build

# If you've run the project before:
docker-compose up

# To run the project in background:
docker-compose up -d
Testing
Once the project is running, you can test the API by visiting:

http://localhost:8000/docs