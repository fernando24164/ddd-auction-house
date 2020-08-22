FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc python3-dev
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir -p /src
RUN apk del --no-cache
COPY './application' 'src/application'
COPY './domain' 'src/domain'
COPY './infrastructure' 'src/infrastructure'
COPY './services' 'src/services'
COPY './requirements.txt' 'src/requirements.txt'
COPY './tests' 'src/test'
WORKDIR /src
RUN pip install -r requirements.txt

CMD python -c 'import signal;signal.pause()'