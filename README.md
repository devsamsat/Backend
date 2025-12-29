# Backend

## Ringkasan
Backend ini menggunakan FastAPI dengan struktur Clean Architecture sederhana untuk modul user.

## Developer Guide (Dummy)
**Developer:** Anisa Putri  
**Role:** Backend Engineer  
**Kontak:** anisa.putri@example.com  
**Jam kerja:** Senin–Jumat, 09.00–18.00 WIB  

### Setup Lokal (ringkas)
1. Buat virtual environment dan aktifkan.
2. Install dependensi.
3. Jalankan aplikasi.

Contoh (sesuaikan dengan environment Anda):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deskripsi Folder

### Root
- `README.md` — Dokumentasi project.
- `app/` — Source code aplikasi (FastAPI + Clean Architecture).
- `docs/` — Dokumen pendukung (mis. `dev-guide.docx`).

### `app/`
- `main.py` — Entry point FastAPI, registrasi router.
- `core/` — Konfigurasi inti (mis. database).
  - `database.py` — SQLAlchemy engine, session, dan `Base`.
- `domain/` — Entity dan kontrak (interface) bisnis.
  - `entities/` — Dataclass entity (mis. `User`).
  - `repositories/` — Abstract repository (kontrak).
- `usecases/` — Logika use case (orchestrator bisnis).
- `infrastructure/` — Implementasi teknis (ORM, repository).
  - `orm/` — Model SQLAlchemy (mis. `UserModel`).
  - `repositories/` — Implementasi repository berbasis DB.
- `interfaces/` — Layer antarmuka aplikasi.
  - `api/` — Router FastAPI (endpoint).
- `schemas/` — Pydantic schema untuk request/response.
- `tesapi` — File SQLite database lokal (lihat `core/database.py`).

## Step-by-step: Menambahkan Endpoint Baru
Contoh: menambahkan endpoint `GET /users/{user_id}`.

1. **Tambahkan fungsi use case (jika belum ada).**  
   Lokasi: `app/usecases/user_usecase.py`  
   Pastikan method `get_user(self, user_id: int)` tersedia.  

2. **Pastikan repository kontrak mendukung query.**  
   Lokasi: `app/domain/repositories/user_repository.py`  
   Tambahkan method baru jika perlu (mis. `get_by_id`).  

3. **Implementasikan repository di layer infrastructure.**  
   Lokasi: `app/infrastructure/repositories/user_repository_impl.py`  
   Implementasikan method sesuai kontrak (mis. `get_by_id`).

4. **Tambahkan/ubah schema response.**  
   Lokasi: `app/schemas/user_schema.py`  
   Gunakan `UserResponse` atau buat schema baru jika dibutuhkan.

5. **Daftarkan endpoint di router API.**  
   Lokasi: `app/interfaces/api/users.py`  
   Contoh implementasi:
   ```python
   @router.get("/{user_id}", response_model=UserResponse)
   def get_user(user_id: int, uc: UserUseCase = Depends(get_usecase)):
       user = uc.get_user(user_id)
       if not user:
           raise HTTPException(status_code=404, detail="User not found")
       return user
   ```

6. **Jalankan aplikasi dan uji endpoint.**  
   ```bash
   uvicorn app.main:app --reload
   curl http://127.0.0.1:8000/users/1
   ```

> Catatan: Untuk endpoint baru pada domain lain, ikuti pola yang sama:
> **interfaces ➜ usecases ➜ domain ➜ infrastructure ➜ schemas**.
