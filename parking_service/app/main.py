import os

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
from database.carDB import CarDB
from database.database import engine, SessionLocal
from sqlalchemy.orm import Session
from model.car import Car
import database.database as database

app = FastAPI()
database.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/health", status_code=status.HTTP_200_OK)
async def station_alive():
    return {'message': 'service alive'}


@app.get("/car")
async def fetch_trains(db: db_dependency):
    result = db.query(Car).all()
    return result


@app.post("/add_car")
async def add_trains(car: Car, db: db_dependency):
    db_car = CarDB(number=car.number,
                   time=car.time,
                   price=car.price)

    db.add(db_car)
    db.commit()
    db.refresh(db_car)


@app.post("/delete_car")
async def delete_car(car_id: int, db: db_dependency):
    try:
        car = db.query(CarDB).filter(
            CarDB.id == car_id,
        ).first()
        db.delete(car)
        db.commit()
    except Exception as _ex:
        raise HTTPException(status_code=404, detail='Car not found')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
