# Listify_App
FastAPI project that implements CRUD operations, REST API, and include authentication and authorization using OAuth token barrier.

## FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance, batteries-included Python web framework that's perfect for building RESTful APIs.


## Resources to Learn FastAPI
We all have preferred method of learning so choose the format that works for you:

**1. [Video format](https://youtube.com/playlist?list=PLaNsxqNgctlM0CEzKBidDbYVmNsoBK8Ss) (YouTube playlist by Sumanshu Nankana)**

The YouTube playlist "FastAPI" explains the FastAPI framework from the basics by building a CRUD application with authentication and authorization using JWT. The playlist includes 47 videos, each of which covers a different aspect of FastAPI. The videos are well-organized and easy to follow, and they provide a comprehensive overview of the framework.

<img width="817" alt="image" src="https://fastapi.tiangolo.com/img/vscode-completion.png">

**2. [Blog format](https://fastapi.tiangolo.com/lo/tutorial/) (FastAPI Documentation)**

## Preconditions:

- Python 3

## Running the App locally
If you wish to download the project, follow these instructions.

### Clone the project

```
git clone https://github.com/marciovrl/fastapi-example.git
```
After you clone the project, cd into the Listify directory.

### Virtual environmnet with venv
You can create a virtual environment in a directory using Python's venv module:

```
python -m venv env
```
That will create a directory ./env/ with the Python binaries and then you will be able to install packages for that isolated environment.

### Activate the environment
Activate the new environment with:

For Linux, macOS
```
source ./env/bin/activate
```

For Windows PowerShell
```
.\env\Scripts\Activate.ps1
```

If it shows the pip binary at env/bin/pip then it worked. 🎉
Make sure you have the latest pip version on your virtual environment to avoid errors on the next steps:
```
python -m pip install --upgrade pip
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run server
```
uvicorn app.main:app --reload
```

### Run test
```
pytest app/test.py
```
## API documentation (provided by Swagger UI)
```
http://127.0.0.1:8000/docs
```

### Don't forget!
This project requires POSTGRES credentials and JWT SECRET_KEY to `Listify/config.py` file.


:sparkles:**When running the project be sure to update the `Listify/config.py` file with your POSTGRES credentials and JWT SECRET_KEY before running the project!**:sparkles: