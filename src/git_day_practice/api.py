from fastapi import FastAPI, Header, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from git_day_practice.settings import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)

# Pydantic model for /items
class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    in_stock: bool

# Validation error handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error_type": "validation_error", "detail": exc.errors()},
    )

# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Config endpoint
@app.get("/config")
def get_config():
    return {"app_name": settings.app_name, "environment": settings.environment, "debug": settings.debug}

# Secure data endpoint
@app.get("/secure-data")
def secure_data(x_api_key: str | None = Header(default=None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"secret_data": "approved"}

# Items endpoint
@app.post("/items")
def create_item(item: ItemCreate):
    return {"message": "item created", "item": item.model_dump()}
