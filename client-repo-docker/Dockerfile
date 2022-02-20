FROM python:3.8-slim-buster
COPY .env /tmp
COPY requirements.txt /tmp
COPY client.py /tmp
WORKDIR /tmp
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "client.py"]