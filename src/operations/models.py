from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from database import metadata

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("course_name", String),
    Column("text_course", String),
    Column("course_image", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)
