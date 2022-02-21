FROM tiangolo/uvicorn-gunicorn:python3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app/app