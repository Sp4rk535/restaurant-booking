from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Reservation
from app.schemas import Reservation as ReservationSchema, ReservationCreate
from app.database import get_db
from app.services import check_reservation_conflict

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[ReservationSchema])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

@router.post("/", response_model=ReservationSchema)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    if check_reservation_conflict(db, reservation.table_id, reservation.reservation_time, reservation.duration_minutes):
        raise HTTPException(status_code=400, detail="Table is already reserved for this time slot")
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.delete("/{id}")
def delete_reservation(id: int, db: Session = Depends(get_db)):
    db_reservation = db.query(Reservation).filter(Reservation.id == id).first()
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(db_reservation)
    db.commit()
    return {"message": "Reservation deleted"}