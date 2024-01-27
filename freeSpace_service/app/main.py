import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
from database.base import engine, SessionLocal
from sqlalchemy.orm import Session
from database import base as database
import smtplib
from email.mime.text import MIMEText

from parking_service.app.database.carDB import CarDB

app = FastAPI()
database.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/alive", status_code=status.HTTP_200_OK)
async def car_alive():
    return {'message' : 'service alive'}


@app.post("/add_car")
async def add_car(car: int, db: db_dependency):
    db_car = CarDB(number=car.number,
                   time=car.time,
                   price=car.price)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return "Машина на парковке"

@app.get("/get_place")
async def get_place(place_id: int, db: db_dependency):
    try:
        result = db.query(CarDB).filter(CarDB.id == place_id).first()
    except Exception:
        raise HTTPException(status_code=404, detail='Place not found')
    return result



