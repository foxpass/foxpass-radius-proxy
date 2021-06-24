FROM python:3.7-alpine3.12

RUN pip install requests

ADD . /src

# UDP
EXPOSE 1812/UDP

CMD ["python", "/src/foxpass-radius-proxy.py"]
