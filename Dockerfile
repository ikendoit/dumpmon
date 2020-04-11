FROM python:2.7

WORKDIR /code

#COPY . .

# Install Pip dependencies
RUN pip install beautifulsoup4 requests pymongo
