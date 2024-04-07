## Project: Python Tooling Assessment

This project serves as an assessment for a Python Developer role. It demonstrates my ability to develop a Tool that scrape Company and the person Data From (apollo.io) website, It is very helpful in generating important user data.

### Tech Stack

- Programming Language(s): Python 3.11
- Frameworks/Libraries: FastApi, Celery, requests
- Other Tools: vscode,

**Installation**

1. **Prerequisites:** Ensure you have the following installed on your system:

- python 3.8+
- Docker Engine (for running a rabbitmq server)
- Poetry (dependency management tool)
  ```
  pip install poetry
  ```

2. **Clone the Repository:**

```
git clone https://github.com/ashwinam/Magicpitch-Assessment.git
```

3. **Dependencies:**

```
poetry install
```

4. **start a fast api server**

```
uvicorn main:app --reload
```

5. **start rabbitmq server**

```
docker run -d -p 5672:5672 rabbitmq
```

6. **start celery**

```
celery -A tasks worker --loglevel=INFO
```

### Additional Notes

Note: Use a fastapi docs endpoint for testing the apis
