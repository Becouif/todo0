from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Todo(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    todo: so.Mapped[str] = so.mapped_column(sa.String(140),index=True)

    def __repr__(self):
        return '<Todo {}>'.format(self.todo)



