import json
import os
from urllib.parse import unquote

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.infrastructure.clients.simeri_client import (
    SimeriClient,
    SimeriClientError,
)
from app.usecases.simeri_usecase import SimeriUseCase

router = APIRouter(prefix="/api/v1/simeri", tags=["simeri"])


def get_usecase() -> SimeriUseCase:
    base_url = os.environ.get("SIM_ERI_BASE_URL")
    if not base_url:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SIM_ERI_BASE_URL is not configured",
        )
    
    url = base_url + "/webservices/dipenda/pendaftaran.php"
    return SimeriUseCase(SimeriClient(url))


@router.get("/pendaftaran")
def pendaftaran_simeri(
    objekbadanno: str | None = Query(None),
    uc: SimeriUseCase = Depends(get_usecase),
):
    try:
        if not objekbadanno:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="objekbadanno is required",
            )
        decoded = unquote(objekbadanno)
        nopol = decoded.strip().split()
        if len(nopol) != 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="format nopol salah",
            )
        nopola, nopolb, nopolc = nopol
        params = {
            "nopola": nopola,
            "nopolb": nopolb,
            "nopolc": nopolc,
        }
        raw = uc.fetch({k: v for k, v in params.items() if v is not None})
        data = raw.get("data")
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                data = None
        if isinstance(data, list) and data:
            first = data[0]
            if isinstance(first, dict) and first.get("STATUS") == "0":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=first.get("DESKRIPSI", "SIM ERI returned STATUS=0"),
                )
        return uc.map_to_masterwp(raw)
    except SimeriClientError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc
