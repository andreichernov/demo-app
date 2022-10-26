FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app
ENV DEBUG_MODE=1
COPY static/ ./static/
COPY templates/ ./templates/
COPY app.py .
EXPOSE 5100
CMD flask run -p 5100