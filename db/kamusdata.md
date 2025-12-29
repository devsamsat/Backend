# Kamus Data V@LIDSAMSAT

Dokumen ini berisi daftar tabel dan kolom berdasarkan `db/V@LIDSAMSAT.sql`.

## Tabel `appgroupuser`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdgroup | character varying(30) | NOT NULL |  |
| nmgroup | character varying(50) | NOT NULL |  |
| ket | character varying(100) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `appotor`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdgroup | character varying(30) | NOT NULL |  |
| roleid | character varying(50) | NOT NULL |  |
| ket | character varying(100) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `approle`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| roleid | character varying(50) | NOT NULL |  |
| idapp | bigint | NULL |  |
| role | character varying(254) | NULL |  |
| type | character(2) | NULL |  |
| menuid | character varying(50) | NULL |  |
| parentid | character varying(50) | NULL |  |
| bantuan | character varying(254) | NULL |  |
| link | character varying(254) | NULL |  |
| icon | character varying(254) | NULL |  |
| kdlevel | integer | NULL |  |
| show | integer | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `appuser`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| userid | character varying(50) | NOT NULL |  |
| idupt | bigint | NULL |  |
| kdtahap | character(5) | NOT NULL |  |
| pwd | character varying(200) | NULL |  |
| idpeg | bigint | NULL |  |
| kdgroup | character varying(30) | NOT NULL |  |
| nik | character varying(50) | NULL |  |
| nama | character varying(100) | NULL |  |
| email | character varying(50) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsdok`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kddok | character varying(10) | NOT NULL |  |
| namadok | character varying(30) | NOT NULL |  |
| keterangan | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsgolongan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| jnsgolid | character(2) | NOT NULL |  |
| golongan | character varying(30) | NOT NULL |  |
| katid | character(1) | NULL |  |
| jnskendid | character(3) | NULL |  |
| viewall | character(1) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsguna`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdguna | character varying(2) | NOT NULL |  |
| guna | character varying(30) | NOT NULL |  |
| gunaplat | character varying(2) | NULL |  |
| progresif | numeric(18,2) | NULL |  |
| groupbpkb | character varying(20) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnshist`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdhist | character(3) | NOT NULL |  |
| nmhist | character varying(50) | NOT NULL |  |
| kdflow | character(2) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsjr`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| jnsjrid | character(2) | NOT NULL |  |
| kodejr | character varying(2) | NOT NULL |  |
| goljns | character varying(2) | NOT NULL |  |
| pu | character varying(2) | NOT NULL |  |
| roda | integer | NOT NULL |  |
| keterangan | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnskatkendaraan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| katid | character(1) | NOT NULL |  |
| kendaraan | character varying(30) | NOT NULL |  |
| jenisbpkb | character varying(20) | NOT NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnskendaraan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| jnskendid | character(3) | NOT NULL |  |
| jnskend | character varying(30) | NOT NULL |  |
| katid | character(1) | NOT NULL |  |
| jnsjrid | character(2) | NULL |  |
| golpjr | integer | NULL |  |
| golujr | integer | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsmilik`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdmilik | character varying(2) | NOT NULL |  |
| milik | character varying(30) | NOT NULL |  |
| bpkpid | character varying(2) | NOT NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnspajak`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdjnspjk | character varying(2) | NOT NULL |  |
| nmjnspjk | character varying(50) | NOT NULL |  |
| keterangan | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsplat`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdplat | character varying(2) | NOT NULL |  |
| plat | character varying(10) | NOT NULL |  |
| pu | character varying(1) | NOT NULL |  |
| platjr | integer | NOT NULL |  |
| numpkb | numeric(18,4) | NOT NULL |  |
| numbbn1 | numeric(18,4) | NOT NULL |  |
| numbbn2 | numeric(18,4) | NOT NULL |  |
| umorg | numeric(18,4) | NOT NULL |  |
| umbrg | numeric(18,4) | NOT NULL |  |
| dnumpkb | numeric(18,4) | NOT NULL |  |
| dnumbbn | numeric(18,4) | NOT NULL |  |
| dumorg | numeric(18,4) | NOT NULL |  |
| dumbrg | numeric(18,4) | NOT NULL |  |
| abpkb | numeric(18,4) | NOT NULL |  |
| abbbn1 | numeric(18,4) | NOT NULL |  |
| abbbn2 | numeric(18,4) | NOT NULL |  |
| numfiskal | numeric(18,4) | NOT NULL |  |
| snid | character varying(1) | NOT NULL |  |
| opspkb | numeric(18,4) | NOT NULL |  |
| opsbbn | numeric(18,4) | NOT NULL |  |
| opsnumpkb | numeric(18,4) | NOT NULL |  |
| opsnumbbn1 | numeric(18,4) | NOT NULL |  |
| opsnumbbn2 | numeric(18,4) | NOT NULL |  |
| opsdnumpkb | numeric(18,4) | NOT NULL |  |
| opsdnumbbn | numeric(18,4) | NOT NULL |  |
| minnumpkb | numeric(18,4) | NOT NULL |  |
| minnumbbn1 | numeric(18,4) | NOT NULL |  |
| minnumbbn2 | numeric(18,4) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsprogresif`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdprogresif | integer | NOT NULL |  |
| progresifr2 | numeric(18,2) | NOT NULL |  |
| progresifr4 | numeric(18,2) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsranmor`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdranmor | character(1) | NOT NULL |  |
| nmranmor | character varying(30) | NOT NULL |  |
| snid | character(1) | NOT NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsstrurek`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| mtglevel | character(2) | NOT NULL |  |
| nmlevel | character varying(50) | NOT NULL |  |
| keterangan | character varying(100) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnstarif`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdjnstarif | character(3) | NOT NULL |  |
| nmjnstarif | character varying(100) | NOT NULL |  |
| idupt | bigint | NOT NULL |  |
| jnskendid | character(3) | NULL |  |
| idrekd | integer | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `jnsumum`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdumum | character(2) | NOT NULL |  |
| nmumum | character varying(30) | NOT NULL |  |
| keterangan | character varying(100) | NOT NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `mapjnspendapatan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idmapjnsd | integer | NOT NULL |  |
| nmjnspendapatan | character varying(200) | NOT NULL |  |
| idrekpkb | integer | NULL |  |
| idrekbbnkb | integer | NULL |  |
| idrekopsenpkb | integer | NULL |  |
| idrekopsenbbnkb | integer | NULL |  |
| idrekpnbp | integer | NULL |  |
| keterangan | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterab`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idab | bigint | NOT NULL |  |
| nomorab | character varying(30) | NOT NULL |  |
| namabadan | character varying(100) | NOT NULL |  |
| alamat | character varying(255) | NULL |  |
| idkabkokta | bigint | NULL |  |
| idkecamatan | bigint | NULL |  |
| idkelurahan | bigint | NULL |  |
| idrw | integer | NULL |  |
| idrt | integer | NULL |  |
| telepon | character varying(30) | NULL |  |
| fax | character varying(30) | NULL |  |
| idktp | bigint | NULL |  |
| noktp | character varying(30) | NULL |  |
| pekerjaan | character varying(50) | NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| tglfaktur | date | NULL | CURRENT_DATE |
| insidentil | character(1) | NOT NULL |  |
| jnskendid | character(3) | NULL |  |
| idmerk | integer | NULL |  |
| merk | character varying(30) | NULL |  |
| tipe | character varying(50) | NULL |  |
| tahunbuat | integer | NULL |  |
| kodebbm | character varying(10) | NULL |  |
| bbm | character varying(30) | NULL |  |
| cylinder | integer | NULL |  |
| norangka | character varying(50) | NULL |  |
| nomesin | character varying(50) | NULL |  |
| nobpkb | character varying(50) | NULL |  |
| kdmilik | character varying(2) | NULL |  |
| kdguna | character varying(2) | NULL |  |
| kendke | integer | NULL |  |
| warna | character varying(50) | NULL |  |
| kdplat | character varying(2) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterabdet`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idabdet | bigint | NOT NULL |  |
| idab | bigint | NOT NULL |  |
| idjnsd | integer | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterbadan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idbadan | bigint | NOT NULL |  |
| nib | character varying(50) | NULL |  |
| idktp | bigint | NULL |  |
| namabadan | character varying(100) | NOT NULL |  |
| nohp | character varying(30) | NOT NULL |  |
| alamat | character varying(255) | NOT NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| idprovinsi | bigint | NULL |  |
| idkabkokta | bigint | NULL |  |
| ket | character varying(512) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterbank`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idbank | integer | NOT NULL |  |
| kodebank | character varying(10) | NOT NULL |  |
| namabank | character varying(100) | NOT NULL |  |
| akronimbank | character varying(50) | NULL |  |
| cabangbank | character varying(50) | NULL |  |
| alamatbank | character varying(100) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterbbm`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kodebbm | character varying(10) | NOT NULL |  |
| namabbm | character varying(50) | NOT NULL |  |
| keterangan | character varying(100) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterbendahara`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idbend | bigint | NOT NULL |  |
| idpegawai | bigint | NOT NULL |  |
| idbank | integer | NOT NULL |  |
| norek | character varying(50) | NOT NULL |  |
| namarek | character varying(100) | NOT NULL |  |
| jnsbend | character varying(2) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| jabatan | character varying(100) | NULL |  |
| pangkat | character varying(50) | NULL |  |
| uid | character varying(15) | NULL |  |
| koordinator | bigint | NULL |  |
| idreknrc | integer | NULL |  |
| telepon | character varying(30) | NULL |  |
| ket | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterflow`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| kdflow | character varying(10) | NOT NULL |  |
| nmflow | character varying(100) | NOT NULL |  |
| pkb | character varying(2) | NULL |  |
| bbn1 | character varying(2) | NULL |  |
| bbn2 | character varying(2) | NULL |  |
| swd | character varying(2) | NULL |  |
| atbkend | character varying(1) | NULL |  |
| flowjr | character varying(1) | NULL |  |
| stnkbaru | character varying(2) | NULL |  |
| tnkb | character varying(2) | NULL |  |
| sahstnk | character varying(2) | NULL |  |
| perpanjangstnk | character varying(2) | NULL |  |
| potongan | character varying(2) | NULL |  |
| bataslayanan | integer | NULL |  |
| satuan | character varying(50) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterhapusdenda`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idhapusdenda | integer | NOT NULL |  |
| jenis | character(1) | NOT NULL |  |
| uraian | character varying(100) | NOT NULL |  |
| awal | date | NULL | CURRENT_DATE |
| akhir | date | NULL | CURRENT_DATE |
| nilai | numeric(18,2) | NULL |  |
| satuan | character varying(30) | NULL |  |
| ket | character varying(256) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterhistory`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idhistory | bigint | NOT NULL |  |
| idwp | bigint | NOT NULL |  |
| objekbadanno | character varying(30) | NOT NULL |  |
| namabadan | character varying(100) | NOT NULL |  |
| idgroupusaha | character varying(2) | NULL |  |
| kodepolisi | character varying(10) | NULL |  |
| kodelokasi | character varying(30) | NULL |  |
| idbadan | bigint | NULL |  |
| idklasifikasi | character varying(2) | NULL |  |
| idlokasi | character varying(2) | NULL |  |
| alamat | character varying(255) | NULL |  |
| idkabkokta | bigint | NULL |  |
| idkecamatan | bigint | NULL |  |
| idkelurahan | bigint | NULL |  |
| idrw | integer | NULL |  |
| idrt | integer | NULL |  |
| telepon | character varying(30) | NULL |  |
| fax | character varying(30) | NULL |  |
| namapemilik | character varying(50) | NULL |  |
| idktp | bigint | NULL |  |
| pekerjaan | character varying(100) | NULL |  |
| tgldaftar | date | NULL |  |
| tglsah | date | NULL |  |
| keteblokir | character varying(255) | NULL |  |
| tglhapus | date | NULL |  |
| groupblokir | character varying(10) | NULL |  |
| insidentil | character(1) | NOT NULL |  |
| nopollama | character varying(30) | NOT NULL |  |
| lastskp | character varying(50) | NULL |  |
| jnskendid | character(3) | NULL |  |
| idmerk | integer | NULL |  |
| merk | character varying(30) | NULL |  |
| tipe | character varying(50) | NULL |  |
| tahunbuat | integer | NULL |  |
| kodebbm | character varying(10) | NULL |  |
| bbm | character varying(30) | NULL |  |
| cylinder | integer | NULL |  |
| norangka | character varying(50) | NULL |  |
| nomesin | character varying(50) | NULL |  |
| nobpkb | character varying(50) | NULL |  |
| kdmilik | character varying(2) | NULL |  |
| kdguna | character varying(2) | NULL |  |
| kendke | integer | NULL |  |
| warna | character varying(50) | NULL |  |
| kdplat | character varying(2) | NOT NULL |  |
| nostnkb | character varying(50) | NULL |  |
| daftarstnk | character varying(50) | NULL |  |
| tglcetakstnk | date | NULL | CURRENT_DATE |
| tglstnk | date | NULL | CURRENT_DATE |
| sdstnk | date | NULL | CURRENT_DATE |
| tglskp | date | NULL | CURRENT_DATE |
| awalskp | date | NULL | CURRENT_DATE |
| akhirskp | date | NULL | CURRENT_DATE |
| tglmutasi | date | NULL |  |
| tgljualbeli | date | NULL |  |
| nodaftar | character varying(30) | NULL |  |
| nosah1 | character varying(20) | NULL |  |
| tglsah1 | date | NULL |  |
| nosah2 | character varying(20) | NULL |  |
| tglsah2 | date | NULL |  |
| nosah3 | character varying(20) | NULL |  |
| tglsah3 | date | NULL |  |
| nosah4 | character varying(20) | NULL |  |
| tglsah4 | date | NULL |  |
| laporjual | date | NULL |  |
| nikpemilik | character varying(30) | NULL |  |
| notelppemilik | character varying(30) | NULL |  |
| putih | character varying(1) | NULL |  |
| status | character(1) | NULL |  |
| statint | character(1) | NULL |  |
| histid | character varying(3) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterjabttd`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idjabttd | bigint | NOT NULL |  |
| idpegawai | bigint | NOT NULL |  |
| kddok | character varying(10) | NOT NULL |  |
| jabatan | character varying(50) | NULL |  |
| ket | character varying(256) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterjnspendapatan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idjnsd | integer | NOT NULL |  |
| nmjnspendapatan | character varying(200) | NOT NULL |  |
| parentid | integer | NULL |  |
| kdrek | character varying(30) | NULL |  |
| jatuhtempo | integer | NULL |  |
| status | character(1) | NULL |  |
| selfassessment | character(1) | NULL |  |
| katid | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkabkota`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkabkota | bigint | NOT NULL |  |
| idprovinsi | bigint | NOT NULL |  |
| kdkabkota | character(10) | NULL |  |
| nmkabkota | character varying(50) | NOT NULL |  |
| akronim | character varying(50) | NOT NULL |  |
| ibukota | character varying(50) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| bpkbid | character varying(4) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkabkotaall`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkabkotaall | bigint | NOT NULL |  |
| idprovinsi | bigint | NOT NULL |  |
| kdkabkota | character(8) | NULL |  |
| nmkabkota | character varying(100) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkaupt`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkaupt | bigint | NOT NULL |  |
| idpegawai | bigint | NULL |  |
| idupt | bigint | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkb`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkb | bigint | NOT NULL |  |
| nomorfaktur | character varying(30) | NULL |  |
| namabadan | character varying(100) | NOT NULL |  |
| alamat | character varying(255) | NULL |  |
| idkabkokta | bigint | NULL |  |
| idkecamatan | bigint | NULL |  |
| idkelurahan | bigint | NULL |  |
| idrw | integer | NULL |  |
| idrt | integer | NULL |  |
| telepon | character varying(30) | NULL |  |
| fax | character varying(30) | NULL |  |
| idktp | bigint | NULL |  |
| noktp | character varying(30) | NULL |  |
| pekerjaan | character varying(50) | NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| tglfaktur | date | NULL | CURRENT_DATE |
| insidentil | character(1) | NOT NULL |  |
| jnskendid | character(3) | NULL |  |
| idmerk | integer | NULL |  |
| merk | character varying(30) | NULL |  |
| tipe | character varying(50) | NULL |  |
| tahunbuat | integer | NULL |  |
| kodebbm | character varying(10) | NULL |  |
| bbm | character varying(30) | NULL |  |
| cylinder | integer | NULL |  |
| norangka | character varying(50) | NULL |  |
| nomesin | character varying(50) | NULL |  |
| nobpkb | character varying(50) | NULL |  |
| kdmilik | character varying(2) | NULL |  |
| kdguna | character varying(2) | NULL |  |
| kendke | integer | NULL |  |
| warna | character varying(50) | NULL |  |
| kdplat | character varying(2) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkbdet`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkbdet | bigint | NOT NULL |  |
| idkb | bigint | NOT NULL |  |
| idjnsd | integer | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkecamatan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkecamatan | bigint | NOT NULL |  |
| idkabkota | bigint | NOT NULL |  |
| kdkecamatan | character(10) | NULL |  |
| nmkecamatan | character varying(100) | NOT NULL |  |
| alamat | character varying(100) | NOT NULL |  |
| telepon | character varying(30) | NOT NULL |  |
| fax | character varying(30) | NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkelurahan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkelurahan | bigint | NOT NULL |  |
| idkecamatan | bigint | NOT NULL |  |
| kdkelurahan | character(10) | NULL |  |
| nmkelurahan | character varying(100) | NOT NULL |  |
| alamat | character varying(100) | NOT NULL |  |
| telepon | character varying(30) | NOT NULL |  |
| kodepos | character varying(30) | NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterkiosk`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkios | integer | NOT NULL |  |
| idparent | integer | NULL |  |
| kodekiosk | character varying(20) | NOT NULL |  |
| datakiosk | character varying(200) | NOT NULL |  |
| level | character(1) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterktp`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idktp | bigint | NOT NULL |  |
| nik | character varying(50) | NOT NULL |  |
| nama | character varying(100) | NOT NULL |  |
| agama | integer | NULL |  |
| nohp | character varying(30) | NOT NULL |  |
| alamat | character varying(255) | NOT NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| idprovinsi | bigint | NULL |  |
| idkabkokta | bigint | NOT NULL |  |
| idkecamatan | bigint | NOT NULL |  |
| idkelurahan | bigint | NOT NULL |  |
| idrw | integer | NULL |  |
| idrt | integer | NULL |  |
| kdrt | character varying(20) | NULL |  |
| nikah | integer | NULL |  |
| tempatlahir | character varying(100) | NULL |  |
| tgllahir | date | NULL |  |
| tglregistrasi | date | NULL |  |
| nokk | character varying(30) | NULL |  |
| nobpjs | character varying(30) | NULL |  |
| goldarah | character varying(2) | NULL |  |
| email | character varying(50) | NULL |  |
| pendidikan | character varying(50) | NULL |  |
| jeniskelamin | character(1) | NULL |  |
| dusun | character varying(50) | NULL |  |
| pekerjaan | character varying(100) | NULL |  |
| namaayah | character varying(100) | NULL |  |
| namaibu | character varying(100) | NULL |  |
| negara | character varying(50) | NULL |  |
| statwn | character(1) | NULL |  |
| statint | character(1) | NULL |  |
| tglint | date | NULL |  |
| ket | character varying(512) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterlibur`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idlibur | integer | NOT NULL |  |
| idkabkota | bigint | NOT NULL |  |
| level | character(1) | NOT NULL |  |
| tanggal | date | NULL | CURRENT_DATE |
| namalibur | character varying(150) | NULL |  |
| keterangan | character(3) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `mastermerk`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idmerk | integer | NOT NULL |  |
| kdmerk | character(2) | NULL |  |
| nmmerk | character varying(100) | NOT NULL |  |
| keterangan | character varying(200) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masternpwpd`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idnpwpd | bigint | NOT NULL |  |
| statnpwpd | character(1) | NULL |  |
| npwpd | character varying(50) | NOT NULL |  |
| idbadan | bigint | NULL |  |
| idktp | bigint | NULL |  |
| tgldaftar | date | NULL |  |
| nib | character varying(50) | NULL |  |
| namabadan | character varying(100) | NULL |  |
| alamat | character varying(100) | NULL |  |
| status | character(1) | NULL |  |
| ket | character varying(512) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterpegawai`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idpegawai | bigint | NOT NULL |  |
| idktp | bigint | NULL |  |
| nip | character varying(50) | NOT NULL |  |
| nik | character varying(50) | NULL |  |
| nama | character varying(50) | NOT NULL |  |
| idupt | bigint | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| jabatan | character varying(100) | NULL |  |
| pangkat | character varying(50) | NULL |  |
| golongan | character varying(20) | NULL |  |
| uid | character varying(15) | NULL |  |
| telepon | character varying(30) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterprovinsi`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idprovinsi | bigint | NOT NULL |  |
| kdprovinsi | character varying(10) | NOT NULL |  |
| nmprovinsi | character varying(100) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterrekd`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idrekd | integer | NOT NULL |  |
| idparent | integer | NULL |  |
| mtglevel | character(2) | NULL |  |
| kdrek | character varying(30) | NOT NULL |  |
| nmrek | character varying(200) | NULL |  |
| kdjnspjk | character varying(2) | NULL |  |
| type | character(1) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterreknrc`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idreknrc | integer | NOT NULL |  |
| mtglevel | character(2) | NULL |  |
| kdrek | character varying(30) | NOT NULL |  |
| nmrek | character varying(500) | NULL |  |
| type | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterrt`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idrt | integer | NOT NULL |  |
| idrw | integer | NOT NULL |  |
| kdrt | character(10) | NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterrw`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idrw | integer | NOT NULL |  |
| idkelurahan | bigint | NOT NULL |  |
| kdrw | character(10) | NULL |  |
| alamat | character varying(100) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `mastertarif`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idtarif | bigint | NOT NULL |  |
| kdjnspjk | character varying(2) | NOT NULL |  |
| jnskendid | character(3) | NULL |  |
| satuan | character varying(200) | NULL |  |
| awal | numeric(18,2) | NULL |  |
| akhir | numeric(18,2) | NULL |  |
| keterangan | character varying(200) | NULL |  |
| kdflow | character varying(10) | NULL |  |
| kdplat | character varying(2) | NULL |  |
| statumum | character(1) | NULL |  |
| tarif | numeric(18,2) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `mastertarifnjop`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idtarifnjop | bigint | NOT NULL |  |
| iduunjop | bigint | NOT NULL |  |
| idrekd | integer | NULL |  |
| kdjnstarif | character(3) | NULL |  |
| namatarif | character varying(200) | NULL |  |
| idmerk | integer | NULL |  |
| tipe | character varying(10) | NULL |  |
| silinder | character varying(50) | NULL |  |
| tahun | character(4) | NULL |  |
| kodebbm | character varying(10) | NULL |  |
| njop | money | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterteks`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idteks | integer | NOT NULL |  |
| datateks | character varying(1024) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterupt`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idupt | bigint | NOT NULL |  |
| idparent | bigint | NULL |  |
| kdupt | character varying(50) | NOT NULL |  |
| nmupt | character varying(500) | NOT NULL |  |
| kdlevel | character(1) | NULL |  |
| type | character(5) | NOT NULL |  |
| akroupt | character varying(200) | NULL |  |
| alamat | character varying(200) | NULL |  |
| telepon | character varying(200) | NULL |  |
| idbank | integer | NULL |  |
| idkabkota | bigint | NULL |  |
| kepala | bigint | NULL |  |
| koordinator | bigint | NULL |  |
| bendahara | bigint | NULL |  |
| norekb | character varying(20) | NULL |  |
| status | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masteruunjop`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| iduunjop | bigint | NOT NULL |  |
| noperkada | character varying(50) | NULL |  |
| isiperkada | character varying(200) | NULL |  |
| tahun | character(4) | NULL |  |
| status | character(1) | NULL |  |
| keterangan | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterwp`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idwp | bigint | NOT NULL |  |
| objekbadanno | character varying(30) | NOT NULL |  |
| namabadan | character varying(100) | NOT NULL |  |
| idgroupusaha | character varying(2) | NULL |  |
| kodepolisi | character varying(10) | NULL |  |
| kodelokasi | character varying(10) | NULL |  |
| idbadan | bigint | NULL |  |
| idklasifikasi | character varying(2) | NULL |  |
| idlokasi | character varying(2) | NULL |  |
| alamat | character varying(255) | NULL |  |
| idkabkokta | bigint | NULL |  |
| idkecamatan | bigint | NULL |  |
| idkelurahan | bigint | NULL |  |
| idrw | integer | NULL |  |
| idrt | integer | NULL |  |
| telepon | character varying(30) | NULL |  |
| fax | character varying(30) | NULL |  |
| namapemilik | character varying(50) | NULL |  |
| idktp | bigint | NULL |  |
| pekerjaan | character varying(100) | NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| tglsah | date | NULL |  |
| keteblokir | character varying(255) | NULL |  |
| tglhapus | date | NULL |  |
| groupblokir | character varying(10) | NULL |  |
| insidentil | character(1) | NOT NULL |  |
| nopollama | character varying(30) | NOT NULL |  |
| lastskp | character varying(50) | NULL |  |
| jnskendid | character(3) | NULL |  |
| idmerk | integer | NULL |  |
| merk | character varying(30) | NULL |  |
| tipe | character varying(50) | NULL |  |
| tahunbuat | integer | NULL |  |
| kodebbm | character varying(10) | NULL |  |
| bbm | character varying(30) | NULL |  |
| cylinder | integer | NULL |  |
| norangka | character varying(50) | NULL |  |
| nomesin | character varying(50) | NULL |  |
| nobpkb | character varying(50) | NULL |  |
| kdmilik | character varying(2) | NULL |  |
| kdguna | character varying(2) | NULL |  |
| kendke | integer | NULL |  |
| warna | character varying(50) | NULL |  |
| kdplat | character varying(2) | NOT NULL |  |
| nostnkb | character varying(50) | NULL |  |
| daftarstnk | character varying(50) | NULL |  |
| tglcetakstnk | date | NULL | CURRENT_DATE |
| tglstnk | date | NULL | CURRENT_DATE |
| sdstnk | date | NULL |  |
| tglskp | date | NULL |  |
| awalskp | date | NULL |  |
| akhirskp | date | NULL |  |
| tglmutasi | date | NULL |  |
| tgljualbeli | date | NULL |  |
| nodaftar | character varying(30) | NULL |  |
| nosah1 | character varying(20) | NULL |  |
| tglsah1 | date | NULL |  |
| nosah2 | character varying(20) | NULL |  |
| tglsah2 | date | NULL |  |
| nosah3 | character varying(20) | NULL |  |
| tglsah3 | date | NULL |  |
| nosah4 | character varying(20) | NULL |  |
| tglsah4 | date | NULL |  |
| laporjual | date | NULL |  |
| nikpemilik | character varying(30) | NULL |  |
| notelppemilik | character varying(30) | NULL |  |
| putih | character varying(1) | NULL |  |
| status | character(1) | NULL |  |
| statint | character(1) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `masterwpdata`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idwpdata | bigint | NOT NULL |  |
| idjnsd | integer | NOT NULL |  |
| tglpendataan | date | NULL | CURRENT_DATE |
| idwp | bigint | NOT NULL |  |
| createdate | date | NULL | CURRENT_DATE |
| createby | character varying(50) | NULL |  |
| updatedate | date | NULL | CURRENT_DATE |
| updateby | character varying(50) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transdatakohir`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idkohir | bigint | NOT NULL |  |
| masaawal | date | NULL | CURRENT_DATE |
| masaakhir | date | NULL | CURRENT_DATE |
| tglpenetapan | date | NULL | CURRENT_DATE |
| penagih | character varying(2) | NOT NULL |  |
| idwp | bigint | NOT NULL |  |
| tglkurangbayar | date | NULL |  |
| keterangan | character varying(256) | NULL |  |
| idupt | bigint | NULL |  |
| skrupt | character varying(20) | NULL |  |
| validjr | character(1) | NULL |  |
| validjrby | character varying(50) | NULL |  |
| validpol | character(1) | NULL |  |
| validpolby | character varying(50) | NULL |  |
| ntpd | character varying(50) | NULL |  |
| tglntpd | date | NULL |  |
| idbank | character varying(3) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transhistpendataan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idhistpendataan | bigint | NOT NULL |  |
| idpendataan | bigint | NOT NULL |  |
| spt | character varying(8) | NOT NULL |  |
| idwpdata | bigint | NOT NULL |  |
| tglpendataan | date | NULL | CURRENT_DATE |
| masaawal | date | NULL | CURRENT_DATE |
| masaakhir | date | NULL | CURRENT_DATE |
| uruttgl | integer | NOT NULL |  |
| jmlomzetawal | numeric(18,2) | NULL |  |
| tarifpjk | numeric(18,2) | NOT NULL |  |
| idupt | bigint | NOT NULL |  |
| kdflow | character varying(10) | NULL |  |
| histid | character varying(3) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transhistpendataandet`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idhistpendataandet | bigint | NOT NULL |  |
| idhistpendataan | bigint | NOT NULL |  |
| idpenetapan | bigint | NOT NULL |  |
| nourut | integer | NOT NULL |  |
| lokasi | character varying(255) | NULL |  |
| transid | character varying(2) | NOT NULL |  |
| ket1 | character varying(50) | NOT NULL |  |
| usahaid | integer | NOT NULL |  |
| tarifpajak | numeric(18,2) | NOT NULL |  |
| histid | character varying(3) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transhistpenetapan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idhistpenetapan | bigint | NOT NULL |  |
| idpenetapan | bigint | NOT NULL |  |
| idkohir | bigint | NOT NULL |  |
| nokohir | character varying(30) | NULL |  |
| idwpdata | bigint | NOT NULL |  |
| tglpenetapan | date | NULL | CURRENT_DATE |
| tgljatuhtempo | date | NULL | CURRENT_DATE |
| masaawal | date | NULL | CURRENT_DATE |
| masaakhir | date | NULL | CURRENT_DATE |
| uruttgl | integer | NOT NULL |  |
| jmlomzetawal | numeric(18,2) | NULL |  |
| tarifpajak | numeric(18,2) | NOT NULL |  |
| denda | numeric(18,2) | NULL |  |
| kenaikan | numeric(18,2) | NULL |  |
| statbayar | character(1) | NOT NULL |  |
| tglbayar | date | NULL |  |
| jmlbayar | numeric(18,2) | NULL |  |
| tglkurangbayar | date | NULL |  |
| jmlkurangbayar | numeric(18,2) | NULL |  |
| jmlperingatan | integer | NULL |  |
| kdflow | character varying(10) | NULL |  |
| status | character(1) | NOT NULL |  |
| opsid | character varying(5) | NULL |  |
| opsprov | numeric(18,2) | NULL |  |
| opskota | numeric(18,2) | NULL |  |
| dendaopsprov | numeric(18,2) | NULL |  |
| dendaopskota | numeric(18,2) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transpendataan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idpendataan | bigint | NOT NULL |  |
| spt | character varying(8) | NOT NULL |  |
| idwpdata | bigint | NOT NULL |  |
| tglpendataan | date | NULL | CURRENT_DATE |
| masaawal | date | NULL | CURRENT_DATE |
| masaakhir | date | NULL | CURRENT_DATE |
| uruttgl | integer | NOT NULL |  |
| jmlomzetawal | numeric(18,2) | NULL |  |
| tarifpjk | numeric(18,2) | NOT NULL |  |
| idupt | bigint | NOT NULL |  |
| kdflow | character varying(10) | NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transpendataandet`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idpendataandet | bigint | NOT NULL |  |
| idpendataan | bigint | NOT NULL |  |
| idpenetapan | bigint | NOT NULL |  |
| nourut | integer | NOT NULL |  |
| lokasi | character varying(255) | NULL |  |
| transid | character varying(2) | NOT NULL |  |
| ket1 | character varying(50) | NOT NULL |  |
| usahaid | integer | NOT NULL |  |
| tarifpajak | numeric(18,2) | NOT NULL |  |
| status | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transpenetapan`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idpenetapan | bigint | NOT NULL |  |
| idkohir | bigint | NOT NULL |  |
| nokohir | character varying(30) | NULL |  |
| idwpdata | bigint | NOT NULL |  |
| tglpenetapan | date | NULL | CURRENT_DATE |
| tgljatuhtempo | date | NULL | CURRENT_DATE |
| masaawal | date | NULL | CURRENT_DATE |
| masaakhir | date | NULL | CURRENT_DATE |
| uruttgl | integer | NOT NULL |  |
| jmlomzetawal | numeric(18,2) | NULL |  |
| tarifpajak | numeric(18,2) | NOT NULL |  |
| denda | numeric(18,2) | NULL |  |
| kenaikan | numeric(18,2) | NULL |  |
| statbayar | character(1) | NOT NULL |  |
| tglbayar | date | NULL |  |
| jmlbayar | numeric(18,2) | NULL |  |
| tglkurangbayar | date | NULL |  |
| jmlkurangbayar | numeric(18,2) | NULL |  |
| jmlperingatan | integer | NULL |  |
| kdflow | character varying(10) | NULL |  |
| status | character(1) | NOT NULL |  |
| opsid | character varying(5) | NULL |  |
| opsprov | numeric(18,2) | NULL |  |
| opskota | numeric(18,2) | NULL |  |
| dendaopsprov | numeric(18,2) | NULL |  |
| dendaopskota | numeric(18,2) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transsts`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idsts | bigint | NOT NULL |  |
| idupt | bigint | NOT NULL |  |
| setorandari | character varying(5) | NULL |  |
| idbend | bigint | NOT NULL |  |
| nosts | character varying(50) | NOT NULL |  |
| tglsts | date | NULL | CURRENT_DATE |
| keterangan | character varying(100) | NOT NULL |  |
| statbayar | character(1) | NOT NULL |  |
| ntpd | character varying(50) | NULL |  |
| tglntpd | date | NULL |  |
| statsts | integer | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transstsdet`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idstsdet | bigint | NOT NULL |  |
| idsts | bigint | NOT NULL |  |
| idrekd | integer | NOT NULL |  |
| nilaists | numeric(18,2) | NOT NULL |  |
| jenis | character(1) | NOT NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transwpdata`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idtwpdata | bigint | NOT NULL |  |
| idnpwpd | bigint | NOT NULL |  |
| kdflow | character varying(10) | NULL |  |
| tgldaftar | date | NULL | CURRENT_DATE |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transwpdataantri`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idantri | integer | NOT NULL |  |
| idtwpdata | bigint | NOT NULL |  |
| noantri | character varying(30) | NOT NULL |  |
| idktp | bigint | NULL |  |
| statantri | character(1) | NULL |  |
| ket | character varying(100) | NULL |  |
| tglantri | character varying(30) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |

## Tabel `transwpdatafile`

| Kolom | Tipe | Null | Default |
| --- | --- | --- | --- |
| idfile | bigint | NOT NULL |  |
| idtwpdata | bigint | NOT NULL |  |
| namafile | character varying(512) | NULL |  |
| direktory | character varying(200) | NULL |  |
| extension | character varying(50) | NULL |  |
| size | bigint | NULL |  |
| url | character varying(200) | NULL |  |
| created_at | date | NULL | CURRENT_DATE |
| created_by | character varying(50) | NULL |  |
| updated_at | date | NULL | CURRENT_DATE |
| updated_by | character varying(50) | NULL |  |
