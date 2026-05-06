from sqlalchemy.orm import Session
from .schemas import AddressCreate, AddressUpdate
from .models import Address

def create_address(db: Session, address: AddressCreate):
    obj = Address(**address.model_dump())
    db.add(obj) 
    db.commit()
    db.refresh(obj)
    return obj

def get_all_addresses(db: Session):
    return db.query(Address).all()

def get_address(db: Session, id: int):
    return db.query(Address).filter(Address.id == id).first()

def update_address(db: Session, id: int, data: AddressUpdate):
    obj = get_address(db, id)

    if not obj:
        return None

    obj.latitude = data.latitude
    obj.longitude = data.longitude

    db.commit()
    db.refresh(obj)
    return obj

def delete_address(db: Session, id: int):
    obj = get_address(db, id)

    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj