FROM python:3.10

WORKDIR /app

RUN pip install pipenv

COPY server.py utils.py router.py ./Pipfile* /app/

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "server.py"]
