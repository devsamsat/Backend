import json
import os
from typing import Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import urlopen


class SimeriClientError(RuntimeError):
    pass


class SimeriClient:
    def __init__(self, url: str, timeout_seconds: int = 15) -> None:
        self.url = url
        self.timeout_seconds = timeout_seconds
        self.username = os.environ.get("SIM_ERI_USERNAME")
        self.password = os.environ.get("SIM_ERI_PASSWORD")

    def _build_url(self, params: Mapping[str, str]) -> str:
        parts = urlsplit(self.url)
        query = dict(parse_qsl(parts.query, keep_blank_values=True))
        if self.username:
            query.setdefault("username", self.username)
        if self.password:
            query.setdefault("password", self.password)
        for key, value in params.items():
            if value is None:
                continue
            query[key] = value
        return urlunsplit(
            (parts.scheme, parts.netloc, parts.path, urlencode(query, doseq=True), parts.fragment)
        )

    def get(self, params: Mapping[str, str]) -> dict:
        url = self._build_url(params)
        try:
            with urlopen(url, timeout=self.timeout_seconds) as response:
                body = response.read()
                content_type = response.headers.get("Content-Type", "")
                text = body.decode("utf-8", errors="replace")
                if "application/json" in content_type:
                    return {"status_code": response.status, "data": json.loads(text)}
                return {"status_code": response.status, "data": text}
        except HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise SimeriClientError(f"SIM ERI error {exc.code}: {body}") from exc
        except URLError as exc:
            raise SimeriClientError(f"SIM ERI connection error: {exc.reason}") from exc
