FROM python:3.8 as builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim
WORKDIR /code

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:/root/.local:$PATH


#CMD ["python", "./main.py"]
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "main:app"]
