FROM python:3.10-slim

WORKDIR /app

COPY TodosApp/app/requirements.txt .

RUN pip3 install -r requirements.txt

COPY TodosApp/app/ .

EXPOSE 8000

CMD ["sh", "-c", "python wait_for_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]