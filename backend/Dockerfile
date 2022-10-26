FROM python:3.10-slim
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app
ADD app.py .
EXPOSE 5200
CMD flask run -p 5200