from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.controllers.order_controller import router as order_router


app = FastAPI(title="Order System API", version="0.1.0")

app.include_router(order_router)

@app.exception_handler(Exception)
def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"detail": "Connection Error."},
    )
