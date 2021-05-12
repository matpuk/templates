FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir wheel && pip install --no-cache-dir -r requirements.txt

COPY restsvc /app/restsvc

ENV PYTHONPATH="$PYTHONPATH:/app"
ENV FLASK_ENV="development"

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "restsvc.main:app"]
