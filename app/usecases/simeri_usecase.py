import re
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

    @staticmethod
    def _clean_area(value: str | None) -> str | None:
        if not value:
            return None
        cleaned = re.sub(r"[\]\)\}]+$", "", value).strip(" .,-;:")
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned or None

    @classmethod
    def _parse_address_parts(cls, value: Any) -> dict[str, str | None]:
        if not isinstance(value, str):
            return {
                "rt": None,
                "rw": None,
                "kelurahan": None,
                "kecamatan": None,
                "kabupaten_kota": None,
            }

        text = value.strip()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[\]\)\}]+$", "", text).strip(" ,.;:")

        rt = rw = None
        rt_rw_match = re.search(r"\bRT\s*/\s*RW\s*(\d{1,3})\s*/\s*(\d{1,3})\b", text, re.IGNORECASE)
        if rt_rw_match:
            rt, rw = rt_rw_match.group(1), rt_rw_match.group(2)

        kel_match = re.search(
            r"\b(?:DS\.?|DESA|KEL\.?|KELURAHAN)\s*([A-Z0-9 .'-]+?)(?=\b(?:KEC\.?|KECAMATAN|KAB\.?|KABUPATEN|KOTA\.?|KOTA)\b|$)",
            text,
            re.IGNORECASE,
        )
        kec_match = re.search(
            r"\b(?:KEC\.?|KECAMATAN)\s*([A-Z0-9 .'-]+?)(?=\b(?:KAB\.?|KABUPATEN|KOTA\.?|KOTA)\b|$)",
            text,
            re.IGNORECASE,
        )
        kab_match = re.search(
            r"\b(?:KAB\.?|KABUPATEN|KOTA\.?|KOTA)\s*([A-Z0-9 .'-]+)$",
            text,
            re.IGNORECASE,
        )

        return {
            "rt": cls._clean_area(rt),
            "rw": cls._clean_area(rw),
            "kelurahan": cls._clean_area(kel_match.group(1)) if kel_match else None,
            "kecamatan": cls._clean_area(kec_match.group(1)) if kec_match else None,
            "kabupaten_kota": cls._clean_area(kab_match.group(1)) if kab_match else None,
        }

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
        alamat = data.get("Alamat")
        address_parts = self._parse_address_parts(alamat)
        return {
            "objekbadanno": objekbadanno,
            "namabadan": data.get("NamaPemilik"),
            "insidentil": None,
            "nopollama": nopollama,
            "kdplat": None,
            "kodepolisi": data.get("NopolA"),
            "kodelokasi": data.get("NopolC"),
            "alamat": alamat,
            "rt": address_parts["rt"],
            "rw": address_parts["rw"],
            "kelurahan": address_parts["kelurahan"],
            "kecamatan": address_parts["kecamatan"],
            "kabupaten_kota": address_parts["kabupaten_kota"],
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
