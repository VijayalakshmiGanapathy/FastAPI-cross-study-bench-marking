FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DATABASE_URL=mysql+pymysql://root:root@host.docker.internal:3306/sdtm_db

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]