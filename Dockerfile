FROM tiangolo/uvicorn-gunicorn:python3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]