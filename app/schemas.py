from datetime import datetime

from pydantic import BaseModel


class DataRecordCreate(BaseModel):
    site_code: str
    metric_name: str
    value: float
    collected_at: datetime


class DataRecord(DataRecordCreate):
    id: int
