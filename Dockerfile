FROM python:3.13-bookworm
WORKDIR /app

ENV SERVE_HOST=0.0.0.0
ENV SERVE_PORT=80

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["sh", "-c", "uvicorn src.app:app --host \"$SERVE_HOST\" --port \"$SERVE_PORT\""]
