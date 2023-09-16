FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD ./requirements.txt /config
ADD ./docker-entrypoint.sh /config
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /config/requirements.txt
WORKDIR /src
COPY . /src