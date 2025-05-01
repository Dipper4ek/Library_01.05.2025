from sqlalchemy.orm import Session

from . import models, schemas
def get_all_authors(db:Session):
    """SELECT * FROM AUTHOR"""

    return db.query(models.Author).all()

def get_author(db:Session, author_id: int):
    """SELECT * FROM author WHERE author.id == author_id"""
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def create_author(db: Session, new_author_info: schemas.AuthorCreate):
    new_author = models.Author(name=new_author_info.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author

