# pull official base image
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# create a working directory
RUN mkdir /app

# set working directory
WORKDIR /app

# copy project to working directory
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
