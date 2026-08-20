from fastapi import APIRouter

from app.schemas import DataRecord, DataRecordCreate


router = APIRouter(
    prefix="/records",
    tags=["records"],
)

records: list[DataRecord] = []


@router.post("/", response_model=DataRecord, status_code=201)
def create_record(record: DataRecordCreate):
    new_record = DataRecord(
        id=len(records) + 1,
        **record.model_dump(),
    )

    records.append(new_record)

    return new_record


@router.get("/", response_model=list[DataRecord])
def get_records():
    return records
