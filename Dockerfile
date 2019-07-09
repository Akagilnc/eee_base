FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
RUN pip install pipenv
COPY Pipfile ./
RUN pipenv install --system --deploy
COPY . .

EXPOSE 8000
CMD ["pipenv run", "python manage.py", "runserver", "0.0.0.0:8000"]