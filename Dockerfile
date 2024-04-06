FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV NAME SSL_Check
ENTRYPOINT ["python", "ssl_check.py"]
