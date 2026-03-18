# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn pydantic

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "src.git_day_practice.api:app", "--host", "0.0.0.0", "--port", "8000"]
