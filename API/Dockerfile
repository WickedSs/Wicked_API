FROM python:3.10-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

EXPOSE 3115
CMD ["python", "main.py"]