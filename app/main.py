from fastapi import FastAPI
from app.routers import tables, reservations

app = FastAPI(title="Restaurant Booking API")
app.include_router(tables)
app.include_router(reservations)