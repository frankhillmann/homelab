FROM python:3.12-alpine
WORKDIR /app
RUN pip install flask requests
COPY proxy.py .
CMD ["python", "proxy.py"]
