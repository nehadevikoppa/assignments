FROM python:3.11-slim
WORKDIR /app
COPY delivery_metrics.py .
RUN pip install --no-cache-dir prometheus-client
CMD ["python", "delivery_metrics.py"]
