FROM python:3.9-bullseye
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install --requirement requirements.txt
COPY . .

