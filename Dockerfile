FROM python:alpine 

LABEL maintainer="Brando ZHANG <zhang@brando.dev>"

RUN pip install flask

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]