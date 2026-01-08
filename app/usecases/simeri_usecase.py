from datetime import date, datetime
from typing import Any, Mapping

from app.infrastructure.clients.simeri_client import SimeriClient


class SimeriUseCase:
    def __init__(self, client: SimeriClient) -> None:
        self.client = client

    def fetch(self, params: Mapping[str, str]) -> dict:
        return self.client.get(params)

    def map_to_masterwp(self, response: Mapping[str, Any]) -> dict:
        data = response.get("data")
        if isinstance(data, list):
            mapped = [self._map_record(item) for item in data if isinstance(item, Mapping)]
        elif isinstance(data, Mapping):
            mapped = self._map_record(data)
        else:
            mapped = data
        return {"status_code": response.get("status_code"), "data": mapped}

    @staticmethod
    def _parse_date(value: Any) -> date | None:
        if not value:
            return None
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
                try:
                    return datetime.strptime(value, fmt).date()
                except ValueError:
                    continue
        return None

    @staticmethod
    def _parse_int(value: Any) -> int | None:
        if value is None:
            return None
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return None
            try:
                return int(float(stripped.replace(",", "")))
            except ValueError:
                digits = "".join(ch for ch in stripped if ch.isdigit())
                return int(digits) if digits else None
        return None

    @staticmethod
    def _concat_nopol(nopola: Any, nopolb: Any, nopolc: Any) -> str | None:
        parts = [str(part) for part in (nopola, nopolb, nopolc) if part]
        return "".join(parts) if parts else None

    def _map_record(self, data: Mapping[str, Any]) -> dict:
        status = data.get("STATUS")
        status_flag = status if status in ("0", "1") else None
        nopola = data.get("NopolA")
        nopollama = self._concat_nopol(
            data.get("NopolALama"),
            data.get("NopolBLama"),
            data.get("NopolCLama"),
        )
        objekbadanno = self._concat_nopol(
            data.get("NopolA"),
            data.get("NopolB"),
            data.get("NopolC"),
        )
        kdplat = nopola if isinstance(nopola, str) and len(nopola) <= 2 else None
        return {
            "objekbadanno": objekbadanno,
            "namabadan": data.get("NamaPemilik"),
            "insidentil": None,
            "nopollama": nopollama,
            "kdplat": None,
            "kodepolisi": data.get("NopolA"),
            "kodelokasi": data.get("NopolC"),
            "alamat": data.get("Alamat"),
            "namapemilik": data.get("NamaPemilik"),
            "tgldaftar": self._parse_date(data.get("TglDaftar")),
            "tglstnk": self._parse_date(data.get("TglSTNK")),
            "tgljualbeli": self._parse_date(data.get("TglFaktur")),
            "nodaftar": data.get("NoPendaftaran"),
            "nikpemilik": data.get("NoKTP"),
            "notelppemilik": data.get("NoHP"),
            "merk": data.get("Merk"),
            "tipe": data.get("Type"),
            "tahunbuat": self._parse_int(data.get("TahunPembuatan")),
            "kodebbm": data.get("KodeBBM"),
            "bbm": data.get("BBM"),
            "cylinder": self._parse_int(data.get("IsiCylinder")),
            "norangka": data.get("NoRangka"),
            "nomesin": data.get("NoMesin"),
            "nobpkb": data.get("NoBPKB"),
            "warna": data.get("Warna"),
            "nostnkb": data.get("NoRegisterSTNK"),
            "daftarstnk": data.get("NoRegisterSTNK"),
            "jnskendid": data.get("KodeJenisKendaraan"),
            "kdguna": data.get("KodeFungsi"),
            "status": status_flag,
            "statint": status_flag,
        }
