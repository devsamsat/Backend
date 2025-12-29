from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.dynamic_record_repository import DynamicRecordRepository
from app.usecases.dynamic_record_usecase import DynamicRecordUseCase
from app.schemas.dynamic_schema import DynamicRecordPayload, DynamicRecordResponse

ALLOWED_TABLES = {
    "appgroupuser",
    "appotor",
    "approle",
    "appuser",
    "jnsdok",
    "jnsgolongan",
    "jnsguna",
    "jnshist",
    "jnsjr",
    "jnskatkendaraan",
    "jnskendaraan",
    "jnsmilik",
    "jnspajak",
    "jnsplat",
    "jnsprogresif",
    "jnsranmor",
    "jnsstrurek",
    "jnstarif",
    "jnsumum",
    "mapjnspendapatan",
    "masterab",
    "masterabdet",
    "masterbadan",
    "masterbank",
    "masterbbm",
    "masterbendahara",
    "masterflow",
    "masterhapusdenda",
    "masterhistory",
    "masterjabttd",
    "masterjnspendapatan",
    "masterkabkota",
    "masterkabkotaall",
    "masterkaupt",
    "masterkb",
    "masterkbdet",
    "masterkecamatan",
    "masterkelurahan",
    "masterkiosk",
    "masterktp",
    "masterlibur",
    "mastermerk",
    "masternpwpd",
    "masterpegawai",
    "masterprovinsi",
    "masterrekd",
    "masterreknrc",
    "masterrt",
    "masterrw",
    "mastertarif",
    "mastertarifnjop",
    "masterteks",
    "masterupt",
    "masteruunjop",
    "masterwp",
    "masterwpdata",
    "transdatakohir",
    "transhistpendataan",
    "transhistpendataandet",
    "transhistpenetapan",
    "transpendataan",
    "transpendataandet",
    "transpenetapan",
    "transsts",
    "transstsdet",
    "transwpdata",
    "transwpdataantri",
    "transwpdatafile",
    "ref_flag",
}

router = APIRouter(prefix="/api", tags=["Dynamic Tables"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = DynamicRecordRepository(db)
    return DynamicRecordUseCase(repo)


def validate_table(table_name: str):
    if table_name not in ALLOWED_TABLES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Table '{table_name}' is not registered",
        )


@router.post("/{table_name}", response_model=DynamicRecordResponse)
def create_record(
    table_name: str,
    payload: DynamicRecordPayload,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    validate_table(table_name)
    existing = uc.get_by_record_id(table_name, payload.record_id)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Record already exists",
        )
    return uc.create(table_name, payload.record_id, payload.payload)


@router.get("/{table_name}", response_model=list[DynamicRecordResponse])
def get_records(table_name: str, uc: DynamicRecordUseCase = Depends(get_usecase)):
    validate_table(table_name)
    return uc.get_all(table_name)


@router.get("/{table_name}/{record_id}", response_model=DynamicRecordResponse)
def get_record(
    table_name: str,
    record_id: str,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    validate_table(table_name)
    record = uc.get_by_record_id(table_name, record_id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{table_name}/{record_id}", response_model=DynamicRecordResponse)
def update_record(
    table_name: str,
    record_id: str,
    payload: DynamicRecordPayload,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    validate_table(table_name)
    if payload.record_id != record_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="record_id mismatch",
        )
    record = uc.update(table_name, record_id, payload.payload)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{table_name}/{record_id}")
def delete_record(
    table_name: str,
    record_id: str,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    validate_table(table_name)
    deleted = uc.delete(table_name, record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
