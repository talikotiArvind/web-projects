FROM python:3.9

WORKDIR /src
COPY src/ src/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]