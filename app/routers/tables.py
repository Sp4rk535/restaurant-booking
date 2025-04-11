from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Table
from app.schemas import Table as TableSchema, TableCreate
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[TableSchema])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.post("/", response_model=TableSchema)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/{id}")
def delete_table(id: int, db: Session = Depends(get_db)):
    db_table = db.query(Table).filter(Table.id == id).first()
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(db_table)
    db.commit()
    return {"message": "Table deleted"}