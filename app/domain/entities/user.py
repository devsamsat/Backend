from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password_hash: str
    full_name: Optional[str]
    is_active: bool
