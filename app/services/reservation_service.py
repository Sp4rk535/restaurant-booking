from sqlalchemy.orm import Session
from app.models import Reservation
from datetime import timedelta, datetime

def check_reservation_conflict(db: Session, table_id: int, start_time: datetime, duration: int):
    end_time = start_time + timedelta(minutes=duration)
    existing = db.query(Reservation).filter(
        Reservation.table_id == table_id,
        Reservation.reservation_time < end_time,
        (Reservation.reservation_time + timedelta(minutes=Reservation.duration_minutes)) > start_time
    ).first()
    return existing is not None