from fastapi import FastAPI, Header, HTTPException

from git_day_practice.settings import settings

app = FastAPI(title=settings.APP_NAME)


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "OK"}


# Config endpoint
@app.get("/config")
def get_config():
    return {"app_name": settings.APP_NAME, "api_key": settings.API_KEY}


# Secure data endpoint with API key check
@app.get("/secure-data")
def secure_data(x_api_key: str | None = Header(default=None)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"data": "This is secure data!"}
