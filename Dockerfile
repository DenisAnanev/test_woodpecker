FROM python:3.7

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY hello_world.py /app/

WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hello_world:app"]
