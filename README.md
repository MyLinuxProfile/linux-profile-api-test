# [linux-profile-api]

## 🚀 Technologies

- [Python](https://www.python.org/) 
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)

# Help
## Linux - Running the Project [PIP]

 - Create a new Python virtual environment
```bash
virtualenv -p python3.9 venv
```
 - Activate the virtual environment
```bash
source venv/bin/activate
```
 - Install requirements with PIP
```bash
pip install -r requirements.txt --no-cache-dir
```
 - Run the application
```
uvicorn app.main:app --host 0.0.0.0 --reload
```

## Linux - Running the Project [Docker]

 - Building the Docker image

```bash
sudo docker build --tag linux-profile/dev --file docker/Dockerfile .
```

 - Starting the Docker container

```bash
sudo docker run --name my_profile -d -p 80:80 linux-profile/dev
```
