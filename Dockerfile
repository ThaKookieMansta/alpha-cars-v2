FROM python:3.10-bullseye
LABEL authors="chrismukirae"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
# Set environment variables
ENV DBUSER='alphacarsadmin'
ENV DBPASSWORD='Password@1'
ENV DBNAME='alphacars254'

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Create the database
RUN service postgresql start && \
    su postgres -c "psql -c \"CREATE DATABASE ${DBNAME};\""

# Copy the Django project into the container
COPY . .


# Expose the default Django port
EXPOSE 8000

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
