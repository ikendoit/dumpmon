FROM python:2.7

WORKDIR /code

# Using volume for easier patching
#COPY . .

# Install Pip dependencies
RUN pip install beautifulsoup4 requests pymongo mysql-connector-python tenacity
