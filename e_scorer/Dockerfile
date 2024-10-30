
FROM python:3.9-slim
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

WORKDIR /e_scorer

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "system_monitor.wsgi:application"]
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
