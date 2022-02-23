FROM python:3.9.10-alpine3.15

RUN pip install requests

ADD . /src

# UDP
EXPOSE 1812/UDP

CMD ["python", "/src/foxpass-radius-proxy.py"]
