FROM python:3.10-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the 'src' folder instead of 'app'
COPY ./src /code/src

# Start Uvicorn pointing to 'src.main'
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]