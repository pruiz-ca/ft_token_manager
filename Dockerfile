FROM python:3.10

WORKDIR /intra_token_validator

RUN pip install pipenv

COPY ./Pipfile* /intra_token_validator/

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "server.py"]
