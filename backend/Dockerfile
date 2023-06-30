FROM python:3.9-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
#RUN mkdir back
WORKDIR /usr/src/app
 RUN apk add --no-cache --update \
     python3 python3-dev gcc \
     gfortran musl-dev g++ \
     libffi-dev openssl-dev \
     libxml2 libxml2-dev \
     libxslt libxslt-dev \
     libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY  . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]