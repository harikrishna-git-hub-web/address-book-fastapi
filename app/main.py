from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import models, schemas, crud
from .utils import calculate_distance

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)


@app.get("/addresses", response_model=list[schemas.AddressResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_addresses(db)


@app.put("/addresses/{id}")
def update(id: int, data: schemas.AddressUpdate, db: Session = Depends(get_db)):
    result = crud.update_address(db, id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return result


@app.delete("/addresses/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    result = crud.delete_address(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Deleted"}


@app.get("/addresses/nearby")
def nearby(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    addresses = crud.get_all_addresses(db)

    result = []
    for addr in addresses:
        dist = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance:
            result.append(addr)

    return result