# Rekomendasi Perbaikan Database V@LIDSAMSAT

Dokumen ini berisi saran perbaikan berdasarkan audit pada `db/V@LIDSAMSAT.sql`.

## Prioritas Tinggi (Integritas Data)
1. **Tambahkan Primary Key** di setiap tabel.
   - Tetapkan kolom identity sebagai PK (`id*`), atau buat PK komposit untuk tabel kode seperti `appgroupuser.kdgroup`, `jnsdok.kddok`, `jnspajak.kdjnspjk`, dsb.
2. **Tambahkan Foreign Key** untuk relasi utama.
   - Contoh: `appuser.kdgroup` → `appgroupuser.kdgroup`, `masterwp.idktp` → `masterktp.idktp`, `transpenetapan.idkohir` → `transdatakohir.idkohir`.
3. **Tambahkan Unique Constraint** untuk kolom kode yang harus unik.
   - Misal `kdgroup`, `kodebank`, `kdjnspjk`, `kdplat`, `kdrek`, `norekb`, `npwpd` (sesuai kebutuhan bisnis).
4. **Tambahkan CHECK constraint** untuk kolom status/flag.
   - `status`, `statbayar`, `statint`, `insidentil`, `validjr`, `validpol`, dsb.

## Prioritas Menengah (Kualitas & Konsistensi)
5. **Standarisasi kolom audit**:
   - Ubah `created_at/updated_at` menjadi `timestamptz` dengan `DEFAULT now()`.
   - Buat trigger otomatis update `updated_at`.
   - Pertimbangkan `NOT NULL` untuk kolom audit penting.
6. **Hilangkan atau konsolidasikan kolom audit ganda** pada `masterwpdata` (`createdate/createby/updatedate/updateby`).
7. **Ganti tipe `money`** dengan `numeric(18,2)` pada `mastertarifnjop.njop`.
8. **Normalisasi penamaan** untuk menghindari keyword SQL dan meningkatkan konsistensi (`show`, `type`, `status` tanpa domain kontrol).

## Prioritas Rendah (Dokumentasi & Performa)
9. **Tambahkan indeks** pada kolom yang sering dipakai join/filter (kolom FK dan kode referensi).
10. **Tambahkan komentar tabel/kolom** (`COMMENT ON`) untuk kamus data internal.
11. **Buat tabel domain/reference** untuk status/flag agar konsisten (misal `status=1/0` atau enum).
12. **Evaluasi duplikasi struktur** seperti `masterwp` vs `masterhistory` untuk efisiensi penyimpanan.
