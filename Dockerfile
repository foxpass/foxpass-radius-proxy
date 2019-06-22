FROM python:3.6-alpine3.8

RUN pip install requests

ADD . /src

# UDP
EXPOSE 1812/UDP

CMD ["python", "/src/foxpass-radius-proxy.py"]
