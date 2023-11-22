from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    course_name: str
    text_course: str
    course_image: str
    date: datetime
    type: str
