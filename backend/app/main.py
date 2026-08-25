from fastapi import FastAPI
from app.controllers.order_controller import router as order_router


app = FastAPI(title="Order System API", version="0.1.0")

app.include_router(order_router)
