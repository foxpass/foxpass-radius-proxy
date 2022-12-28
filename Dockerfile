FROM python:alpine3.17

RUN pip install requests

ADD . /src

# UDP
EXPOSE 1812/UDP

CMD ["python", "/src/foxpass-radius-proxy.py"]
