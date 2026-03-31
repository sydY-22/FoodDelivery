from fastapi import FastAPI
from Routes.auth import auth_router
from Routes.orders import order_router

app=FastAPI()

app.include_router(auth_router)
app.include_router(order_router)

