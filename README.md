# E-commerce Backend

## Description

### Project Setup

1. First, clone the project to your local machine:
```bash
git clone git@github.com:HalilPamukk/e-commerce.git
```

2. Navigate to the project directory

3. Create a virtual environment:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
```bash
source venv/bin/activate
```

5. Copy `.env.example` file as `.env` and fill in the required information

### Docker Setup

1. If Docker Desktop is not installed, download and install it from:
* [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. Open Docker Desktop

3. Navigate to the project directory in terminal and run the project using one of these commands:

```bash
# For first time setup (might take some time):
docker-compose up --build

# If you've run the project before:
docker-compose up

# To run the project in background:
docker-compose up -d
```

### Testing

Once the project is running, you can test the API by visiting:
* http://localhost:8000/docs
