FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory   
WORKDIR /code

COPY pyproject.toml poetry.lock ./
RUN pip install poetry

# Create the venv inside the project directory
RUN poetry config virtualenvs.in-project true --local

# Install dependencies (no dev dependencies for production)
RUN poetry install --no-root --only main

# Add venv to PATH
ENV PATH="/code/.venv/bin:$PATH"

COPY . .

# Set the working directory to your Django project
WORKDIR /code/src/website

# Collect static files and run migrations as part of the entrypoint or command
CMD python manage.py collectstatic --noinput && python manage.py migrate && gunicorn website.wsgi:application --bind 0.0.0.0:8000
