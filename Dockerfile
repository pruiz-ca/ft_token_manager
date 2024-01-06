FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY server.py utils.py router.py poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev

CMD ["poetry", "run", "python", "server.py"]
