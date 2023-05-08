FROM python:3.10

WORKDIR /intra_token_validator

RUN pip install pipenv

COPY . /intra_token_validator/

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "server.py"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
