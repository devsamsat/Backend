import os
from pathlib import Path


def load_env(env_path: str | None = None) -> None:
    if env_path is None:
        env_path = str(Path(__file__).resolve().parents[2] / ".env")
    path = Path(env_path)
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value
