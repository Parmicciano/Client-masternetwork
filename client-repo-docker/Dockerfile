FROM python:3.8-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

RUN pip install --upgrade pip
ENV DISPLAY=:99
COPY .env /tmp
COPY requirements.txt /tmp
COPY client.py /tmp
WORKDIR /tmp
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "client.py"]

#docker run --name=client -e PYTHONUNBUFFERED=1 -d client
#docker build --tag client .