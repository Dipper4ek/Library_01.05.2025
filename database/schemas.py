from pydantic import BaseModel, Field
from typing import Annotated



class AuthorBase(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=30, description="Name Author von 3 bis 30 Symbols")]

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class Author(AuthorBase):
    book:list["Book"]



