FROM python:3.12-slim-bookkworm
WORKDIR /app
COPY hello.py /app/hello.py
CMD ["python", "/app/hello.py"]
