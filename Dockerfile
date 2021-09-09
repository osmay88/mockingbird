FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN python3 -m venv venv
ENV PATH="$venv/bin:$PATH"

RUN ./venv/bin/pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "./" ]

CMD venv/bin/python3 web_runner/main_app.py