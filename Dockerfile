FROM kennethreitz/pipenv

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY Pipfile /app
RUN pipenv install
RUN pipenv shell
COPY . .



EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]