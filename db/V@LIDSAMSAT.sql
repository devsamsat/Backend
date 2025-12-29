--
-- PostgreSQL database dump
--

\restrict LlbYeqUyb5PJzWHLpVTCvgjHKizzku4y7deDfAa4J7OGZDgW8lcE8HZXIh0CXGb

-- Dumped from database version 16.11
-- Dumped by pg_dump version 16.11

-- Started on 2025-12-29 16:01:44

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 17027)
-- Name: appgroupuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appgroupuser (
    kdgroup character varying(30) NOT NULL,
    nmgroup character varying(50) NOT NULL,
    ket character varying(100),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.appgroupuser OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 17121)
-- Name: appotor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appotor (
    kdgroup character varying(30) NOT NULL,
    roleid character varying(50) NOT NULL,
    ket character varying(100),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.appotor OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17041)
-- Name: approle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.approle (
    roleid character varying(50) NOT NULL,
    idapp bigint,
    role character varying(254),
    role_type character(2),
    menuid character varying(50),
    parentid character varying(50),
    bantuan character varying(254),
    link character varying(254),
    icon character varying(254),
    kdlevel integer,
    is_show integer,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.approle OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 17050)
-- Name: appuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appuser (
    userid character varying(50) NOT NULL,
    idupt bigint,
    kdtahap character(5) NOT NULL,
    pwd character varying(200),
    idpeg bigint,
    kdgroup character varying(30) NOT NULL,
    nik character varying(50),
    nama character varying(100),
    email character varying(50),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.appuser OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17059)
-- Name: jnsdok; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsdok (
    kddok character varying(10) NOT NULL,
    namadok character varying(30) NOT NULL,
    keterangan character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsdok OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17066)
-- Name: jnsgolongan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsgolongan (
    jnsgolid character(2) NOT NULL,
    golongan character varying(30) NOT NULL,
    katid character(1),
    jnskendid character(3),
    viewall character(1),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsgolongan OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 17073)
-- Name: jnsguna; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsguna (
    kdguna character varying(2) NOT NULL,
    guna character varying(30) NOT NULL,
    gunaplat character varying(2),
    progresif numeric(18,2),
    groupbpkb character varying(20) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsguna OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17080)
-- Name: jnshist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnshist (
    kdhist character(3) NOT NULL,
    nmhist character varying(50) NOT NULL,
    kdflow character(2),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnshist OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17087)
-- Name: jnsjr; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsjr (
    jnsjrid character(2) NOT NULL,
    kodejr character varying(2) NOT NULL,
    goljns character varying(2) NOT NULL,
    pu character varying(2) NOT NULL,
    roda integer NOT NULL,
    keterangan character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsjr OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17094)
-- Name: jnskatkendaraan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnskatkendaraan (
    katid character(1) NOT NULL,
    kendaraan character varying(30) NOT NULL,
    jenisbpkb character varying(20) NOT NULL,
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnskatkendaraan OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17102)
-- Name: jnskendaraan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnskendaraan (
    jnskendid character(3) NOT NULL,
    jnskend character varying(30) NOT NULL,
    katid character(1) NOT NULL,
    jnsjrid character(2),
    golpjr integer,
    golujr integer,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnskendaraan OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17128)
-- Name: jnsmilik; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsmilik (
    kdmilik character varying(2) NOT NULL,
    milik character varying(30) NOT NULL,
    bpkpid character varying(2) NOT NULL,
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsmilik OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17135)
-- Name: jnspajak; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnspajak (
    kdjnspjk character varying(2) NOT NULL,
    nmjnspjk character varying(50) NOT NULL,
    keterangan character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnspajak OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 17142)
-- Name: jnsplat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsplat (
    kdplat character varying(2) NOT NULL,
    plat character varying(10) NOT NULL,
    pu character varying(1) NOT NULL,
    platjr integer NOT NULL,
    numpkb numeric(18,4) NOT NULL,
    numbbn1 numeric(18,4) NOT NULL,
    numbbn2 numeric(18,4) NOT NULL,
    umorg numeric(18,4) NOT NULL,
    umbrg numeric(18,4) NOT NULL,
    dnumpkb numeric(18,4) NOT NULL,
    dnumbbn numeric(18,4) NOT NULL,
    dumorg numeric(18,4) NOT NULL,
    dumbrg numeric(18,4) NOT NULL,
    abpkb numeric(18,4) NOT NULL,
    abbbn1 numeric(18,4) NOT NULL,
    abbbn2 numeric(18,4) NOT NULL,
    numfiskal numeric(18,4) NOT NULL,
    snid character varying(1) NOT NULL,
    opspkb numeric(18,4) NOT NULL,
    opsbbn numeric(18,4) NOT NULL,
    opsnumpkb numeric(18,4) NOT NULL,
    opsnumbbn1 numeric(18,4) NOT NULL,
    opsnumbbn2 numeric(18,4) NOT NULL,
    opsdnumpkb numeric(18,4) NOT NULL,
    opsdnumbbn numeric(18,4) NOT NULL,
    minnumpkb numeric(18,4) NOT NULL,
    minnumbbn1 numeric(18,4) NOT NULL,
    minnumbbn2 numeric(18,4) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsplat OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 17149)
-- Name: jnsprogresif; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsprogresif (
    kdprogresif integer NOT NULL,
    progresifr2 numeric(18,2) NOT NULL,
    progresifr4 numeric(18,2) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsprogresif OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17156)
-- Name: jnsranmor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsranmor (
    kdranmor character(1) NOT NULL,
    nmranmor character varying(30) NOT NULL,
    snid character(1) NOT NULL,
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsranmor OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17163)
-- Name: jnsstrurek; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsstrurek (
    mtglevel character(2) NOT NULL,
    nmlevel character varying(50) NOT NULL,
    keterangan character varying(100) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsstrurek OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 17170)
-- Name: jnstarif; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnstarif (
    kdjnstarif character(3) NOT NULL,
    nmjnstarif character varying(100) NOT NULL,
    idupt bigint NOT NULL,
    jnskendid character(3),
    idrekd integer,
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnstarif OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 17177)
-- Name: jnsumum; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jnsumum (
    kdumum character(2) NOT NULL,
    nmumum character varying(30) NOT NULL,
    keterangan character varying(100) NOT NULL,
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.jnsumum OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 17185)
-- Name: mapjnspendapatan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mapjnspendapatan (
    idmapjnsd integer NOT NULL,
    nmjnspendapatan character varying(200) NOT NULL,
    idrekpkb integer,
    idrekbbnkb integer,
    idrekopsenpkb integer,
    idrekopsenbbnkb integer,
    idrekpnbp integer,
    keterangan character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.mapjnspendapatan OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 17184)
-- Name: mapjnspendapatan_idmapjnsd_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mapjnspendapatan ALTER COLUMN idmapjnsd ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.mapjnspendapatan_idmapjnsd_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 237 (class 1259 OID 17195)
-- Name: masterab; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterab (
    idab bigint NOT NULL,
    nomorab character varying(30) NOT NULL,
    namabadan character varying(100) NOT NULL,
    alamat character varying(255),
    idkabkokta bigint,
    idkecamatan bigint,
    idkelurahan bigint,
    idrw integer,
    idrt integer,
    telepon character varying(30),
    fax character varying(30),
    idktp bigint,
    noktp character varying(30),
    pekerjaan character varying(50),
    tgldaftar date DEFAULT CURRENT_DATE,
    tglfaktur date DEFAULT CURRENT_DATE,
    insidentil character(1) NOT NULL,
    jnskendid character(3),
    idmerk integer,
    merk character varying(30),
    tipe character varying(50),
    tahunbuat integer,
    kodebbm character varying(10),
    bbm character varying(30),
    cylinder integer,
    norangka character varying(50),
    nomesin character varying(50),
    nobpkb character varying(50),
    kdmilik character varying(2),
    kdguna character varying(2),
    kendke integer,
    warna character varying(50),
    kdplat character varying(2) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterab OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 17194)
-- Name: masterab_idab_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterab ALTER COLUMN idab ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterab_idab_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 239 (class 1259 OID 17207)
-- Name: masterabdet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterabdet (
    idabdet bigint NOT NULL,
    idab bigint NOT NULL,
    idjnsd integer NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterabdet OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 17206)
-- Name: masterabdet_idabdet_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterabdet ALTER COLUMN idabdet ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterabdet_idabdet_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 241 (class 1259 OID 17215)
-- Name: masterbadan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterbadan (
    idbadan bigint NOT NULL,
    nib character varying(50),
    idktp bigint,
    namabadan character varying(100) NOT NULL,
    nohp character varying(30) NOT NULL,
    alamat character varying(255) NOT NULL,
    tgldaftar date DEFAULT CURRENT_DATE,
    idprovinsi bigint,
    idkabkokta bigint,
    ket character varying(512),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterbadan OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 17214)
-- Name: masterbadan_idbadan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterbadan ALTER COLUMN idbadan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterbadan_idbadan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 243 (class 1259 OID 17226)
-- Name: masterbank; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterbank (
    idbank integer NOT NULL,
    kodebank character varying(10) NOT NULL,
    namabank character varying(100) NOT NULL,
    akronimbank character varying(50),
    cabangbank character varying(50),
    alamatbank character varying(100),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterbank OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 17225)
-- Name: masterbank_idbank_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterbank ALTER COLUMN idbank ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterbank_idbank_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 244 (class 1259 OID 17233)
-- Name: masterbbm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterbbm (
    kodebbm character varying(10) NOT NULL,
    namabbm character varying(50) NOT NULL,
    keterangan character varying(100),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterbbm OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 17241)
-- Name: masterbendahara; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterbendahara (
    idbend bigint NOT NULL,
    idpegawai bigint NOT NULL,
    idbank integer NOT NULL,
    norek character varying(50) NOT NULL,
    namarek character varying(100) NOT NULL,
    jnsbend character varying(2) NOT NULL,
    status character(1) NOT NULL,
    jabatan character varying(100),
    pangkat character varying(50),
    uid character varying(15),
    koordinator bigint,
    idreknrc integer,
    telepon character varying(30),
    ket character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterbendahara OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 17240)
-- Name: masterbendahara_idbend_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterbendahara ALTER COLUMN idbend ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterbendahara_idbend_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 247 (class 1259 OID 17250)
-- Name: masterflow; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterflow (
    kdflow character varying(10) NOT NULL,
    nmflow character varying(100) NOT NULL,
    pkb character varying(2),
    bbn1 character varying(2),
    bbn2 character varying(2),
    swd character varying(2),
    atbkend character varying(1),
    flowjr character varying(1),
    stnkbaru character varying(2),
    tnkb character varying(2),
    sahstnk character varying(2),
    perpanjangstnk character varying(2),
    potongan character varying(2),
    bataslayanan integer,
    satuan character varying(50),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterflow OWNER TO postgres;

--
-- TOC entry 249 (class 1259 OID 17259)
-- Name: masterhapusdenda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterhapusdenda (
    idhapusdenda integer NOT NULL,
    jenis character(1) NOT NULL,
    uraian character varying(100) NOT NULL,
    awal date DEFAULT CURRENT_DATE,
    akhir date DEFAULT CURRENT_DATE,
    nilai numeric(18,2),
    satuan character varying(30),
    ket character varying(256),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterhapusdenda OWNER TO postgres;

--
-- TOC entry 248 (class 1259 OID 17258)
-- Name: masterhapusdenda_idhapusdenda_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterhapusdenda ALTER COLUMN idhapusdenda ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterhapusdenda_idhapusdenda_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 251 (class 1259 OID 17271)
-- Name: masterhistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterhistory (
    idhistory bigint NOT NULL,
    idwp bigint NOT NULL,
    objekbadanno character varying(30) NOT NULL,
    namabadan character varying(100) NOT NULL,
    idgroupusaha character varying(2),
    kodepolisi character varying(10),
    kodelokasi character varying(30),
    idbadan bigint,
    idklasifikasi character varying(2),
    idlokasi character varying(2),
    alamat character varying(255),
    idkabkokta bigint,
    idkecamatan bigint,
    idkelurahan bigint,
    idrw integer,
    idrt integer,
    telepon character varying(30),
    fax character varying(30),
    namapemilik character varying(50),
    idktp bigint,
    pekerjaan character varying(100),
    tgldaftar date,
    tglsah date,
    keteblokir character varying(255),
    tglhapus date,
    groupblokir character varying(10),
    insidentil character(1) NOT NULL,
    nopollama character varying(30) NOT NULL,
    lastskp character varying(50),
    jnskendid character(3),
    idmerk integer,
    merk character varying(30),
    tipe character varying(50),
    tahunbuat integer,
    kodebbm character varying(10),
    bbm character varying(30),
    cylinder integer,
    norangka character varying(50),
    nomesin character varying(50),
    nobpkb character varying(50),
    kdmilik character varying(2),
    kdguna character varying(2),
    kendke integer,
    warna character varying(50),
    kdplat character varying(2) NOT NULL,
    nostnkb character varying(50),
    daftarstnk character varying(50),
    tglcetakstnk date DEFAULT CURRENT_DATE,
    tglstnk date DEFAULT CURRENT_DATE,
    sdstnk date DEFAULT CURRENT_DATE,
    tglskp date DEFAULT CURRENT_DATE,
    awalskp date DEFAULT CURRENT_DATE,
    akhirskp date DEFAULT CURRENT_DATE,
    tglmutasi date,
    tgljualbeli date,
    nodaftar character varying(30),
    nosah1 character varying(20),
    tglsah1 date,
    nosah2 character varying(20),
    tglsah2 date,
    nosah3 character varying(20),
    tglsah3 date,
    nosah4 character varying(20),
    tglsah4 date,
    laporjual date,
    nikpemilik character varying(30),
    notelppemilik character varying(30),
    putih character varying(1),
    status character(1),
    statint character(1),
    histid character varying(3) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterhistory OWNER TO postgres;

--
-- TOC entry 250 (class 1259 OID 17270)
-- Name: masterhistory_idhistory_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterhistory ALTER COLUMN idhistory ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterhistory_idhistory_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 253 (class 1259 OID 17287)
-- Name: masterjabttd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterjabttd (
    idjabttd bigint NOT NULL,
    idpegawai bigint NOT NULL,
    kddok character varying(10) NOT NULL,
    jabatan character varying(50),
    ket character varying(256),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterjabttd OWNER TO postgres;

--
-- TOC entry 252 (class 1259 OID 17286)
-- Name: masterjabttd_idjabttd_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterjabttd ALTER COLUMN idjabttd ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterjabttd_idjabttd_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 255 (class 1259 OID 17295)
-- Name: masterjnspendapatan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterjnspendapatan (
    idjnsd integer NOT NULL,
    nmjnspendapatan character varying(200) NOT NULL,
    parentid integer,
    kdrek character varying(30),
    jatuhtempo integer,
    status character(1),
    selfassessment character(1),
    katid character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterjnspendapatan OWNER TO postgres;

--
-- TOC entry 254 (class 1259 OID 17294)
-- Name: masterjnspendapatan_idjnsd_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterjnspendapatan ALTER COLUMN idjnsd ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterjnspendapatan_idjnsd_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 257 (class 1259 OID 17303)
-- Name: masterkabkota; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkabkota (
    idkabkota bigint NOT NULL,
    idprovinsi bigint NOT NULL,
    kdkabkota character(10),
    nmkabkota character varying(50) NOT NULL,
    akronim character varying(50) NOT NULL,
    ibukota character varying(50) NOT NULL,
    status character(1) NOT NULL,
    bpkbid character varying(4) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkabkota OWNER TO postgres;

--
-- TOC entry 256 (class 1259 OID 17302)
-- Name: masterkabkota_idkabkota_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkabkota ALTER COLUMN idkabkota ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkabkota_idkabkota_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 259 (class 1259 OID 17311)
-- Name: masterkabkotaall; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkabkotaall (
    idkabkotaall bigint NOT NULL,
    idprovinsi bigint NOT NULL,
    kdkabkota character(8),
    nmkabkota character varying(100) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkabkotaall OWNER TO postgres;

--
-- TOC entry 258 (class 1259 OID 17310)
-- Name: masterkabkotaall_idkabkotaall_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkabkotaall ALTER COLUMN idkabkotaall ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkabkotaall_idkabkotaall_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 261 (class 1259 OID 17319)
-- Name: masterkaupt; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkaupt (
    idkaupt bigint NOT NULL,
    idpegawai bigint,
    idupt bigint NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkaupt OWNER TO postgres;

--
-- TOC entry 260 (class 1259 OID 17318)
-- Name: masterkaupt_idkaupt_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkaupt ALTER COLUMN idkaupt ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkaupt_idkaupt_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 329 (class 1259 OID 17664)
-- Name: masterkb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkb (
    idkb bigint NOT NULL,
    nomorfaktur character varying(30),
    namabadan character varying(100) NOT NULL,
    alamat character varying(255),
    idkabkokta bigint,
    idkecamatan bigint,
    idkelurahan bigint,
    idrw integer,
    idrt integer,
    telepon character varying(30),
    fax character varying(30),
    idktp bigint,
    noktp character varying(30),
    pekerjaan character varying(50),
    tgldaftar date DEFAULT CURRENT_DATE,
    tglfaktur date DEFAULT CURRENT_DATE,
    insidentil character(1) NOT NULL,
    jnskendid character(3),
    idmerk integer,
    merk character varying(30),
    tipe character varying(50),
    tahunbuat integer,
    kodebbm character varying(10),
    bbm character varying(30),
    cylinder integer,
    norangka character varying(50),
    nomesin character varying(50),
    nobpkb character varying(50),
    kdmilik character varying(2),
    kdguna character varying(2),
    kendke integer,
    warna character varying(50),
    kdplat character varying(2) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkb OWNER TO postgres;

--
-- TOC entry 328 (class 1259 OID 17663)
-- Name: masterkb_idkb_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkb ALTER COLUMN idkb ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkb_idkb_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 263 (class 1259 OID 17328)
-- Name: masterkbdet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkbdet (
    idkbdet bigint NOT NULL,
    idkb bigint NOT NULL,
    idjnsd integer NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkbdet OWNER TO postgres;

--
-- TOC entry 262 (class 1259 OID 17327)
-- Name: masterkbdet_idkbdet_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkbdet ALTER COLUMN idkbdet ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkbdet_idkbdet_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 265 (class 1259 OID 17336)
-- Name: masterkecamatan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkecamatan (
    idkecamatan bigint NOT NULL,
    idkabkota bigint NOT NULL,
    kdkecamatan character(10),
    nmkecamatan character varying(100) NOT NULL,
    alamat character varying(100) NOT NULL,
    telepon character varying(30) NOT NULL,
    fax character varying(30),
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkecamatan OWNER TO postgres;

--
-- TOC entry 264 (class 1259 OID 17335)
-- Name: masterkecamatan_idkecamatan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkecamatan ALTER COLUMN idkecamatan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkecamatan_idkecamatan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 267 (class 1259 OID 17344)
-- Name: masterkelurahan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkelurahan (
    idkelurahan bigint NOT NULL,
    idkecamatan bigint NOT NULL,
    kdkelurahan character(10),
    nmkelurahan character varying(100) NOT NULL,
    alamat character varying(100) NOT NULL,
    telepon character varying(30) NOT NULL,
    kodepos character varying(30),
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkelurahan OWNER TO postgres;

--
-- TOC entry 266 (class 1259 OID 17343)
-- Name: masterkelurahan_idkelurahan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkelurahan ALTER COLUMN idkelurahan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkelurahan_idkelurahan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 269 (class 1259 OID 17352)
-- Name: masterkiosk; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterkiosk (
    idkios integer NOT NULL,
    idparent integer,
    kodekiosk character varying(20) NOT NULL,
    datakiosk character varying(200) NOT NULL,
    level character(1) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterkiosk OWNER TO postgres;

--
-- TOC entry 268 (class 1259 OID 17351)
-- Name: masterkiosk_idkios_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterkiosk ALTER COLUMN idkios ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterkiosk_idkios_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 327 (class 1259 OID 17653)
-- Name: masterktp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterktp (
    idktp bigint NOT NULL,
    nik character varying(50) NOT NULL,
    nama character varying(100) NOT NULL,
    agama integer,
    nohp character varying(30) NOT NULL,
    alamat character varying(255) NOT NULL,
    tgldaftar date DEFAULT CURRENT_DATE,
    idprovinsi bigint,
    idkabkokta bigint NOT NULL,
    idkecamatan bigint NOT NULL,
    idkelurahan bigint NOT NULL,
    idrw integer,
    idrt integer,
    kdrt character varying(20),
    nikah integer,
    tempatlahir character varying(100),
    tgllahir date,
    tglregistrasi date,
    nokk character varying(30),
    nobpjs character varying(30),
    goldarah character varying(2),
    email character varying(50),
    pendidikan character varying(50),
    jeniskelamin character(1),
    dusun character varying(50),
    pekerjaan character varying(100),
    namaayah character varying(100),
    namaibu character varying(100),
    negara character varying(50),
    statwn character(1),
    statint character(1),
    tglint date,
    ket character varying(512),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterktp OWNER TO postgres;

--
-- TOC entry 326 (class 1259 OID 17652)
-- Name: masterktp_idktp_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterktp ALTER COLUMN idktp ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterktp_idktp_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 271 (class 1259 OID 17360)
-- Name: masterlibur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterlibur (
    idlibur integer NOT NULL,
    idkabkota bigint NOT NULL,
    level character(1) NOT NULL,
    tanggal date DEFAULT CURRENT_DATE,
    namalibur character varying(150),
    keterangan character(3),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterlibur OWNER TO postgres;

--
-- TOC entry 270 (class 1259 OID 17359)
-- Name: masterlibur_idlibur_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterlibur ALTER COLUMN idlibur ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterlibur_idlibur_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 273 (class 1259 OID 17369)
-- Name: mastermerk; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mastermerk (
    idmerk integer NOT NULL,
    kdmerk character(2),
    nmmerk character varying(100) NOT NULL,
    keterangan character varying(200),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.mastermerk OWNER TO postgres;

--
-- TOC entry 272 (class 1259 OID 17368)
-- Name: mastermerk_idmerk_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mastermerk ALTER COLUMN idmerk ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.mastermerk_idmerk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 275 (class 1259 OID 17377)
-- Name: masternpwpd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masternpwpd (
    idnpwpd bigint NOT NULL,
    statnpwpd character(1),
    npwpd character varying(50) NOT NULL,
    idbadan bigint,
    idktp bigint,
    tgldaftar date,
    nib character varying(50),
    namabadan character varying(100),
    alamat character varying(100),
    status character(1),
    ket character varying(512),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masternpwpd OWNER TO postgres;

--
-- TOC entry 274 (class 1259 OID 17376)
-- Name: masternpwpd_idnpwpd_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masternpwpd ALTER COLUMN idnpwpd ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masternpwpd_idnpwpd_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 277 (class 1259 OID 17387)
-- Name: masterpegawai; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterpegawai (
    idpegawai bigint NOT NULL,
    idktp bigint,
    nip character varying(50) NOT NULL,
    nik character varying(50),
    nama character varying(50) NOT NULL,
    idupt bigint NOT NULL,
    status character(1) NOT NULL,
    jabatan character varying(100),
    pangkat character varying(50),
    golongan character varying(20),
    uid character varying(15),
    telepon character varying(30),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterpegawai OWNER TO postgres;

--
-- TOC entry 276 (class 1259 OID 17386)
-- Name: masterpegawai_idpegawai_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterpegawai ALTER COLUMN idpegawai ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterpegawai_idpegawai_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 279 (class 1259 OID 17395)
-- Name: masterprovinsi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterprovinsi (
    idprovinsi bigint NOT NULL,
    kdprovinsi character varying(10) NOT NULL,
    nmprovinsi character varying(100) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterprovinsi OWNER TO postgres;

--
-- TOC entry 278 (class 1259 OID 17394)
-- Name: masterprovinsi_idprovinsi_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterprovinsi ALTER COLUMN idprovinsi ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterprovinsi_idprovinsi_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 281 (class 1259 OID 17403)
-- Name: masterrekd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterrekd (
    idrekd integer NOT NULL,
    idparent integer,
    mtglevel character(2),
    kdrek character varying(30) NOT NULL,
    nmrek character varying(200),
    kdjnspjk character varying(2),
    rek_type character(1),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterrekd OWNER TO postgres;

--
-- TOC entry 280 (class 1259 OID 17402)
-- Name: masterrekd_idrekd_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterrekd ALTER COLUMN idrekd ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterrekd_idrekd_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 283 (class 1259 OID 17412)
-- Name: masterreknrc; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterreknrc (
    idreknrc integer NOT NULL,
    mtglevel character(2),
    kdrek character varying(30) NOT NULL,
    nmrek character varying(500),
    rek_type character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterreknrc OWNER TO postgres;

--
-- TOC entry 282 (class 1259 OID 17411)
-- Name: masterreknrc_idreknrc_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterreknrc ALTER COLUMN idreknrc ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterreknrc_idreknrc_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 285 (class 1259 OID 17422)
-- Name: masterrt; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterrt (
    idrt integer NOT NULL,
    idrw integer NOT NULL,
    kdrt character(10),
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterrt OWNER TO postgres;

--
-- TOC entry 284 (class 1259 OID 17421)
-- Name: masterrt_idrt_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterrt ALTER COLUMN idrt ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterrt_idrt_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 287 (class 1259 OID 17430)
-- Name: masterrw; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterrw (
    idrw integer NOT NULL,
    idkelurahan bigint NOT NULL,
    kdrw character(10),
    alamat character varying(100) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterrw OWNER TO postgres;

--
-- TOC entry 286 (class 1259 OID 17429)
-- Name: masterrw_idrw_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterrw ALTER COLUMN idrw ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterrw_idrw_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 289 (class 1259 OID 17438)
-- Name: mastertarif; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mastertarif (
    idtarif bigint NOT NULL,
    kdjnspjk character varying(2) NOT NULL,
    jnskendid character(3),
    satuan character varying(200),
    awal numeric(18,2),
    akhir numeric(18,2),
    keterangan character varying(200),
    kdflow character varying(10),
    kdplat character varying(2),
    statumum character(1),
    tarif numeric(18,2),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.mastertarif OWNER TO postgres;

--
-- TOC entry 288 (class 1259 OID 17437)
-- Name: mastertarif_idtarif_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mastertarif ALTER COLUMN idtarif ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.mastertarif_idtarif_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 291 (class 1259 OID 17448)
-- Name: mastertarifnjop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mastertarifnjop (
    idtarifnjop bigint NOT NULL,
    iduunjop bigint NOT NULL,
    idrekd integer,
    kdjnstarif character(3),
    namatarif character varying(200),
    idmerk integer,
    tipe character varying(10),
    silinder character varying(50),
    tahun character(4),
    kodebbm character varying(10),
    njop numeric(18,2),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.mastertarifnjop OWNER TO postgres;

--
-- TOC entry 290 (class 1259 OID 17447)
-- Name: mastertarifnjop_idtarifnjop_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mastertarifnjop ALTER COLUMN idtarifnjop ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.mastertarifnjop_idtarifnjop_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 293 (class 1259 OID 17466)
-- Name: masterteks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterteks (
    idteks integer NOT NULL,
    datateks character varying(1024) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterteks OWNER TO postgres;

--
-- TOC entry 292 (class 1259 OID 17465)
-- Name: masterteks_idteks_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterteks ALTER COLUMN idteks ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterteks_idteks_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 295 (class 1259 OID 17476)
-- Name: masterupt; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterupt (
    idupt bigint NOT NULL,
    idparent bigint,
    kdupt character varying(50) NOT NULL,
    nmupt character varying(500) NOT NULL,
    kdlevel character(1),
    upt_type character(5) NOT NULL,
    akroupt character varying(200),
    alamat character varying(200),
    telepon character varying(200),
    idbank integer,
    idkabkota bigint,
    kepala bigint,
    koordinator bigint,
    bendahara bigint,
    norekb character varying(20),
    status character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterupt OWNER TO postgres;

--
-- TOC entry 294 (class 1259 OID 17475)
-- Name: masterupt_idupt_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterupt ALTER COLUMN idupt ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterupt_idupt_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 297 (class 1259 OID 17486)
-- Name: masteruunjop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masteruunjop (
    iduunjop bigint NOT NULL,
    noperkada character varying(50),
    isiperkada character varying(200),
    tahun character(4),
    status character(1),
    keterangan character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masteruunjop OWNER TO postgres;

--
-- TOC entry 296 (class 1259 OID 17485)
-- Name: masteruunjop_iduunjop_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masteruunjop ALTER COLUMN iduunjop ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masteruunjop_iduunjop_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 299 (class 1259 OID 17497)
-- Name: masterwp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterwp (
    idwp bigint NOT NULL,
    objekbadanno character varying(30) NOT NULL,
    namabadan character varying(100) NOT NULL,
    idgroupusaha character varying(2),
    kodepolisi character varying(10),
    kodelokasi character varying(10),
    idbadan bigint,
    idklasifikasi character varying(2),
    idlokasi character varying(2),
    alamat character varying(255),
    idkabkokta bigint,
    idkecamatan bigint,
    idkelurahan bigint,
    idrw integer,
    idrt integer,
    telepon character varying(30),
    fax character varying(30),
    namapemilik character varying(50),
    idktp bigint,
    pekerjaan character varying(100),
    tgldaftar date DEFAULT CURRENT_DATE,
    tglsah date,
    keteblokir character varying(255),
    tglhapus date,
    groupblokir character varying(10),
    insidentil character(1) NOT NULL,
    nopollama character varying(30) NOT NULL,
    lastskp character varying(50),
    jnskendid character(3),
    idmerk integer,
    merk character varying(30),
    tipe character varying(50),
    tahunbuat integer,
    kodebbm character varying(10),
    bbm character varying(30),
    cylinder integer,
    norangka character varying(50),
    nomesin character varying(50),
    nobpkb character varying(50),
    kdmilik character varying(2),
    kdguna character varying(2),
    kendke integer,
    warna character varying(50),
    kdplat character varying(2) NOT NULL,
    nostnkb character varying(50),
    daftarstnk character varying(50),
    tglcetakstnk date DEFAULT CURRENT_DATE,
    tglstnk date DEFAULT CURRENT_DATE,
    sdstnk date,
    tglskp date,
    awalskp date,
    akhirskp date,
    tglmutasi date,
    tgljualbeli date,
    nodaftar character varying(30),
    nosah1 character varying(20),
    tglsah1 date,
    nosah2 character varying(20),
    tglsah2 date,
    nosah3 character varying(20),
    tglsah3 date,
    nosah4 character varying(20),
    tglsah4 date,
    laporjual date,
    nikpemilik character varying(30),
    notelppemilik character varying(30),
    putih character varying(1),
    status character(1),
    statint character(1),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterwp OWNER TO postgres;

--
-- TOC entry 298 (class 1259 OID 17496)
-- Name: masterwp_idwp_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterwp ALTER COLUMN idwp ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterwp_idwp_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 301 (class 1259 OID 17510)
-- Name: masterwpdata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.masterwpdata (
    idwpdata bigint NOT NULL,
    idjnsd integer NOT NULL,
    tglpendataan date DEFAULT CURRENT_DATE,
    idwp bigint NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.masterwpdata OWNER TO postgres;

--
-- TOC entry 300 (class 1259 OID 17509)
-- Name: masterwpdata_idwpdata_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.masterwpdata ALTER COLUMN idwpdata ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.masterwpdata_idwpdata_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 303 (class 1259 OID 17521)
-- Name: transdatakohir; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transdatakohir (
    idkohir bigint NOT NULL,
    masaawal date DEFAULT CURRENT_DATE,
    masaakhir date DEFAULT CURRENT_DATE,
    tglpenetapan date DEFAULT CURRENT_DATE,
    penagih character varying(2) NOT NULL,
    idwp bigint NOT NULL,
    tglkurangbayar date,
    keterangan character varying(256),
    idupt bigint,
    skrupt character varying(20),
    validjr character(1),
    validjrby character varying(50),
    validpol character(1),
    validpolby character varying(50),
    ntpd character varying(50),
    tglntpd date,
    idbank character varying(3),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transdatakohir OWNER TO postgres;

--
-- TOC entry 302 (class 1259 OID 17520)
-- Name: transdatakohir_idkohir_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transdatakohir ALTER COLUMN idkohir ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transdatakohir_idkohir_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 305 (class 1259 OID 17534)
-- Name: transhistpendataan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transhistpendataan (
    idhistpendataan bigint NOT NULL,
    idpendataan bigint NOT NULL,
    spt character varying(8) NOT NULL,
    idwpdata bigint NOT NULL,
    tglpendataan date DEFAULT CURRENT_DATE,
    masaawal date DEFAULT CURRENT_DATE,
    masaakhir date DEFAULT CURRENT_DATE,
    uruttgl integer NOT NULL,
    jmlomzetawal numeric(18,2),
    tarifpjk numeric(18,2) NOT NULL,
    idupt bigint NOT NULL,
    kdflow character varying(10),
    histid character varying(3) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transhistpendataan OWNER TO postgres;

--
-- TOC entry 304 (class 1259 OID 17533)
-- Name: transhistpendataan_idhistpendataan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transhistpendataan ALTER COLUMN idhistpendataan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transhistpendataan_idhistpendataan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 307 (class 1259 OID 17545)
-- Name: transhistpendataandet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transhistpendataandet (
    idhistpendataandet bigint NOT NULL,
    idhistpendataan bigint NOT NULL,
    idpenetapan bigint NOT NULL,
    nourut integer NOT NULL,
    lokasi character varying(255),
    transid character varying(2) NOT NULL,
    ket1 character varying(50) NOT NULL,
    usahaid integer NOT NULL,
    tarifpajak numeric(18,2) NOT NULL,
    histid character varying(3) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transhistpendataandet OWNER TO postgres;

--
-- TOC entry 306 (class 1259 OID 17544)
-- Name: transhistpendataandet_idhistpendataandet_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transhistpendataandet ALTER COLUMN idhistpendataandet ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transhistpendataandet_idhistpendataandet_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 309 (class 1259 OID 17553)
-- Name: transhistpenetapan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transhistpenetapan (
    idhistpenetapan bigint NOT NULL,
    idpenetapan bigint NOT NULL,
    idkohir bigint NOT NULL,
    nokohir character varying(30),
    idwpdata bigint NOT NULL,
    tglpenetapan date DEFAULT CURRENT_DATE,
    tgljatuhtempo date DEFAULT CURRENT_DATE,
    masaawal date DEFAULT CURRENT_DATE,
    masaakhir date DEFAULT CURRENT_DATE,
    uruttgl integer NOT NULL,
    jmlomzetawal numeric(18,2),
    tarifpajak numeric(18,2) NOT NULL,
    denda numeric(18,2),
    kenaikan numeric(18,2),
    statbayar character(1) NOT NULL,
    tglbayar date,
    jmlbayar numeric(18,2),
    tglkurangbayar date,
    jmlkurangbayar numeric(18,2),
    jmlperingatan integer,
    kdflow character varying(10),
    status character(1) NOT NULL,
    opsid character varying(5),
    opsprov numeric(18,2),
    opskota numeric(18,2),
    dendaopsprov numeric(18,2),
    dendaopskota numeric(18,2),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transhistpenetapan OWNER TO postgres;

--
-- TOC entry 308 (class 1259 OID 17552)
-- Name: transhistpenetapan_idhistpenetapan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transhistpenetapan ALTER COLUMN idhistpenetapan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transhistpenetapan_idhistpenetapan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 311 (class 1259 OID 17566)
-- Name: transpendataan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transpendataan (
    idpendataan bigint NOT NULL,
    spt character varying(8) NOT NULL,
    idwpdata bigint NOT NULL,
    tglpendataan date DEFAULT CURRENT_DATE,
    masaawal date DEFAULT CURRENT_DATE,
    masaakhir date DEFAULT CURRENT_DATE,
    uruttgl integer NOT NULL,
    jmlomzetawal numeric(18,2),
    tarifpjk numeric(18,2) NOT NULL,
    idupt bigint NOT NULL,
    kdflow character varying(10),
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transpendataan OWNER TO postgres;

--
-- TOC entry 310 (class 1259 OID 17565)
-- Name: transpendataan_idpendataan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transpendataan ALTER COLUMN idpendataan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transpendataan_idpendataan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 313 (class 1259 OID 17577)
-- Name: transpendataandet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transpendataandet (
    idpendataandet bigint NOT NULL,
    idpendataan bigint NOT NULL,
    idpenetapan bigint NOT NULL,
    nourut integer NOT NULL,
    lokasi character varying(255),
    transid character varying(2) NOT NULL,
    ket1 character varying(50) NOT NULL,
    usahaid integer NOT NULL,
    tarifpajak numeric(18,2) NOT NULL,
    status character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transpendataandet OWNER TO postgres;

--
-- TOC entry 312 (class 1259 OID 17576)
-- Name: transpendataandet_idpendataandet_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transpendataandet ALTER COLUMN idpendataandet ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transpendataandet_idpendataandet_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 315 (class 1259 OID 17585)
-- Name: transpenetapan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transpenetapan (
    idpenetapan bigint NOT NULL,
    idkohir bigint NOT NULL,
    nokohir character varying(30),
    idwpdata bigint NOT NULL,
    tglpenetapan date DEFAULT CURRENT_DATE,
    tgljatuhtempo date DEFAULT CURRENT_DATE,
    masaawal date DEFAULT CURRENT_DATE,
    masaakhir date DEFAULT CURRENT_DATE,
    uruttgl integer NOT NULL,
    jmlomzetawal numeric(18,2),
    tarifpajak numeric(18,2) NOT NULL,
    denda numeric(18,2),
    kenaikan numeric(18,2),
    statbayar character(1) NOT NULL,
    tglbayar date,
    jmlbayar numeric(18,2),
    tglkurangbayar date,
    jmlkurangbayar numeric(18,2),
    jmlperingatan integer,
    kdflow character varying(10),
    status character(1) NOT NULL,
    opsid character varying(5),
    opsprov numeric(18,2),
    opskota numeric(18,2),
    dendaopsprov numeric(18,2),
    dendaopskota numeric(18,2),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transpenetapan OWNER TO postgres;

--
-- TOC entry 314 (class 1259 OID 17584)
-- Name: transpenetapan_idpenetapan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transpenetapan ALTER COLUMN idpenetapan ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transpenetapan_idpenetapan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 317 (class 1259 OID 17597)
-- Name: transsts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transsts (
    idsts bigint NOT NULL,
    idupt bigint NOT NULL,
    setorandari character varying(5),
    idbend bigint NOT NULL,
    nosts character varying(50) NOT NULL,
    tglsts date DEFAULT CURRENT_DATE,
    keterangan character varying(100) NOT NULL,
    statbayar character(1) NOT NULL,
    ntpd character varying(50),
    tglntpd date,
    statsts integer,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transsts OWNER TO postgres;

--
-- TOC entry 316 (class 1259 OID 17596)
-- Name: transsts_idsts_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transsts ALTER COLUMN idsts ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transsts_idsts_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 319 (class 1259 OID 17606)
-- Name: transstsdet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transstsdet (
    idstsdet bigint NOT NULL,
    idsts bigint NOT NULL,
    idrekd integer NOT NULL,
    nilaists numeric(18,2) NOT NULL,
    jenis character(1) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transstsdet OWNER TO postgres;

--
-- TOC entry 318 (class 1259 OID 17605)
-- Name: transstsdet_idstsdet_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transstsdet ALTER COLUMN idstsdet ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transstsdet_idstsdet_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 321 (class 1259 OID 17614)
-- Name: transwpdata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transwpdata (
    idtwpdata bigint NOT NULL,
    idnpwpd bigint NOT NULL,
    kdflow character varying(10),
    tgldaftar date DEFAULT CURRENT_DATE,
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transwpdata OWNER TO postgres;

--
-- TOC entry 320 (class 1259 OID 17613)
-- Name: transwpdata_idtwpdata_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transwpdata ALTER COLUMN idtwpdata ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transwpdata_idtwpdata_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 323 (class 1259 OID 17623)
-- Name: transwpdataantri; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transwpdataantri (
    idantri integer NOT NULL,
    idtwpdata bigint NOT NULL,
    noantri character varying(30) NOT NULL,
    idktp bigint,
    statantri character(1),
    ket character varying(100),
    tglantri character varying(30),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transwpdataantri OWNER TO postgres;

--
-- TOC entry 322 (class 1259 OID 17622)
-- Name: transwpdataantri_idantri_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transwpdataantri ALTER COLUMN idantri ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transwpdataantri_idantri_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 325 (class 1259 OID 17631)
-- Name: transwpdatafile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transwpdatafile (
    idfile bigint NOT NULL,
    idtwpdata bigint NOT NULL,
    namafile character varying(512),
    direktory character varying(200),
    extension character varying(50),
    size bigint,
    url character varying(200),
    created_at timestamptz NOT NULL DEFAULT now(),
    created_by character varying(50),
    updated_at timestamptz NOT NULL DEFAULT now(),
    updated_by character varying(50)
);


ALTER TABLE public.transwpdatafile OWNER TO postgres;

--
-- TOC entry 324 (class 1259 OID 17630)
-- Name: transwpdatafile_idfile_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.transwpdatafile ALTER COLUMN idfile ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.transwpdatafile_idfile_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

--
-- Constraints, indexes, and audit triggers
--

CREATE TABLE public.ref_flag (
    flag_code character(1) NOT NULL,
    description character varying(50) NOT NULL
);

ALTER TABLE public.ref_flag OWNER TO postgres;

ALTER TABLE public.ref_flag
    ADD CONSTRAINT ref_flag_pkey PRIMARY KEY (flag_code);

INSERT INTO public.ref_flag (flag_code, description)
VALUES
    ('0', 'Tidak/Nonaktif'),
    ('1', 'Ya/Aktif');

CREATE OR REPLACE FUNCTION public.set_updated_at()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$;

ALTER TABLE public.appgroupuser
    ADD CONSTRAINT appgroupuser_pkey PRIMARY KEY (kdgroup);

ALTER TABLE public.appotor
    ADD CONSTRAINT appotor_pkey PRIMARY KEY (kdgroup, roleid);

ALTER TABLE public.approle
    ADD CONSTRAINT approle_pkey PRIMARY KEY (roleid);

ALTER TABLE public.appuser
    ADD CONSTRAINT appuser_pkey PRIMARY KEY (userid);

ALTER TABLE public.jnsdok
    ADD CONSTRAINT jnsdok_pkey PRIMARY KEY (kddok);

ALTER TABLE public.jnsgolongan
    ADD CONSTRAINT jnsgolongan_pkey PRIMARY KEY (jnsgolid);

ALTER TABLE public.jnsguna
    ADD CONSTRAINT jnsguna_pkey PRIMARY KEY (kdguna);

ALTER TABLE public.jnshist
    ADD CONSTRAINT jnshist_pkey PRIMARY KEY (kdhist);

ALTER TABLE public.jnsjr
    ADD CONSTRAINT jnsjr_pkey PRIMARY KEY (jnsjrid);

ALTER TABLE public.jnskatkendaraan
    ADD CONSTRAINT jnskatkendaraan_pkey PRIMARY KEY (katid);

ALTER TABLE public.jnskendaraan
    ADD CONSTRAINT jnskendaraan_pkey PRIMARY KEY (jnskendid);

ALTER TABLE public.jnsmilik
    ADD CONSTRAINT jnsmilik_pkey PRIMARY KEY (kdmilik);

ALTER TABLE public.jnspajak
    ADD CONSTRAINT jnspajak_pkey PRIMARY KEY (kdjnspjk);

ALTER TABLE public.jnsplat
    ADD CONSTRAINT jnsplat_pkey PRIMARY KEY (kdplat);

ALTER TABLE public.jnsprogresif
    ADD CONSTRAINT jnsprogresif_pkey PRIMARY KEY (kdprogresif);

ALTER TABLE public.jnsranmor
    ADD CONSTRAINT jnsranmor_pkey PRIMARY KEY (kdranmor);

ALTER TABLE public.jnsstrurek
    ADD CONSTRAINT jnsstrurek_pkey PRIMARY KEY (mtglevel);

ALTER TABLE public.jnstarif
    ADD CONSTRAINT jnstarif_pkey PRIMARY KEY (kdjnstarif);

ALTER TABLE public.jnsumum
    ADD CONSTRAINT jnsumum_pkey PRIMARY KEY (kdumum);

ALTER TABLE public.mapjnspendapatan
    ADD CONSTRAINT mapjnspendapatan_pkey PRIMARY KEY (idmapjnsd);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_pkey PRIMARY KEY (idab);

ALTER TABLE public.masterabdet
    ADD CONSTRAINT masterabdet_pkey PRIMARY KEY (idabdet);

ALTER TABLE public.masterbadan
    ADD CONSTRAINT masterbadan_pkey PRIMARY KEY (idbadan);

ALTER TABLE public.masterbank
    ADD CONSTRAINT masterbank_pkey PRIMARY KEY (idbank);

ALTER TABLE public.masterbbm
    ADD CONSTRAINT masterbbm_pkey PRIMARY KEY (kodebbm);

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_pkey PRIMARY KEY (idbend);

ALTER TABLE public.masterflow
    ADD CONSTRAINT masterflow_pkey PRIMARY KEY (kdflow);

ALTER TABLE public.masterhapusdenda
    ADD CONSTRAINT masterhapusdenda_pkey PRIMARY KEY (idhapusdenda);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_pkey PRIMARY KEY (idhistory);

ALTER TABLE public.masterjabttd
    ADD CONSTRAINT masterjabttd_pkey PRIMARY KEY (idjabttd);

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_pkey PRIMARY KEY (idjnsd);

ALTER TABLE public.masterkabkota
    ADD CONSTRAINT masterkabkota_pkey PRIMARY KEY (idkabkota);

ALTER TABLE public.masterkabkotaall
    ADD CONSTRAINT masterkabkotaall_pkey PRIMARY KEY (idkabkotaall);

ALTER TABLE public.masterkaupt
    ADD CONSTRAINT masterkaupt_pkey PRIMARY KEY (idkaupt);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_pkey PRIMARY KEY (idkb);

ALTER TABLE public.masterkbdet
    ADD CONSTRAINT masterkbdet_pkey PRIMARY KEY (idkbdet);

ALTER TABLE public.masterkecamatan
    ADD CONSTRAINT masterkecamatan_pkey PRIMARY KEY (idkecamatan);

ALTER TABLE public.masterkelurahan
    ADD CONSTRAINT masterkelurahan_pkey PRIMARY KEY (idkelurahan);

ALTER TABLE public.masterkiosk
    ADD CONSTRAINT masterkiosk_pkey PRIMARY KEY (idkios);

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_pkey PRIMARY KEY (idktp);

ALTER TABLE public.masterlibur
    ADD CONSTRAINT masterlibur_pkey PRIMARY KEY (idlibur);

ALTER TABLE public.mastermerk
    ADD CONSTRAINT mastermerk_pkey PRIMARY KEY (idmerk);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_pkey PRIMARY KEY (idnpwpd);

ALTER TABLE public.masterpegawai
    ADD CONSTRAINT masterpegawai_pkey PRIMARY KEY (idpegawai);

ALTER TABLE public.masterprovinsi
    ADD CONSTRAINT masterprovinsi_pkey PRIMARY KEY (idprovinsi);

ALTER TABLE public.masterrekd
    ADD CONSTRAINT masterrekd_pkey PRIMARY KEY (idrekd);

ALTER TABLE public.masterreknrc
    ADD CONSTRAINT masterreknrc_pkey PRIMARY KEY (idreknrc);

ALTER TABLE public.masterrt
    ADD CONSTRAINT masterrt_pkey PRIMARY KEY (idrt);

ALTER TABLE public.masterrw
    ADD CONSTRAINT masterrw_pkey PRIMARY KEY (idrw);

ALTER TABLE public.mastertarif
    ADD CONSTRAINT mastertarif_pkey PRIMARY KEY (idtarif);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_pkey PRIMARY KEY (idtarifnjop);

ALTER TABLE public.masterteks
    ADD CONSTRAINT masterteks_pkey PRIMARY KEY (idteks);

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_pkey PRIMARY KEY (idupt);

ALTER TABLE public.masteruunjop
    ADD CONSTRAINT masteruunjop_pkey PRIMARY KEY (iduunjop);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_pkey PRIMARY KEY (idwp);

ALTER TABLE public.masterwpdata
    ADD CONSTRAINT masterwpdata_pkey PRIMARY KEY (idwpdata);

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_pkey PRIMARY KEY (idkohir);

ALTER TABLE public.transhistpendataan
    ADD CONSTRAINT transhistpendataan_pkey PRIMARY KEY (idhistpendataan);

ALTER TABLE public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_pkey PRIMARY KEY (idhistpendataandet);

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_pkey PRIMARY KEY (idhistpenetapan);

ALTER TABLE public.transpendataan
    ADD CONSTRAINT transpendataan_pkey PRIMARY KEY (idpendataan);

ALTER TABLE public.transpendataandet
    ADD CONSTRAINT transpendataandet_pkey PRIMARY KEY (idpendataandet);

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_pkey PRIMARY KEY (idpenetapan);

ALTER TABLE public.transsts
    ADD CONSTRAINT transsts_pkey PRIMARY KEY (idsts);

ALTER TABLE public.transstsdet
    ADD CONSTRAINT transstsdet_pkey PRIMARY KEY (idstsdet);

ALTER TABLE public.transwpdata
    ADD CONSTRAINT transwpdata_pkey PRIMARY KEY (idtwpdata);

ALTER TABLE public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_pkey PRIMARY KEY (idantri);

ALTER TABLE public.transwpdatafile
    ADD CONSTRAINT transwpdatafile_pkey PRIMARY KEY (idfile);

ALTER TABLE public.masterbank
    ADD CONSTRAINT masterbank_kodebank_key UNIQUE (kodebank);

ALTER TABLE public.masterrekd
    ADD CONSTRAINT masterrekd_kdrek_key UNIQUE (kdrek);

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_norekb_key UNIQUE (norekb);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_npwpd_key UNIQUE (npwpd);

ALTER TABLE public.jnsgolongan
    ADD CONSTRAINT jnsgolongan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnshist
    ADD CONSTRAINT jnshist_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnskatkendaraan
    ADD CONSTRAINT jnskatkendaraan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnsmilik
    ADD CONSTRAINT jnsmilik_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnsranmor
    ADD CONSTRAINT jnsranmor_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnstarif
    ADD CONSTRAINT jnstarif_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.jnsumum
    ADD CONSTRAINT jnsumum_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterbank
    ADD CONSTRAINT masterbank_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterflow
    ADD CONSTRAINT masterflow_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterhapusdenda
    ADD CONSTRAINT masterhapusdenda_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_statint_check CHECK (statint IN ('0', '1'));

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_insidentil_check CHECK (insidentil IN ('0', '1'));

ALTER TABLE public.masterjabttd
    ADD CONSTRAINT masterjabttd_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_selfassessment_check CHECK (selfassessment IN ('0', '1'));

ALTER TABLE public.masterkabkota
    ADD CONSTRAINT masterkabkota_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterkabkotaall
    ADD CONSTRAINT masterkabkotaall_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterkecamatan
    ADD CONSTRAINT masterkecamatan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterkelurahan
    ADD CONSTRAINT masterkelurahan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterkiosk
    ADD CONSTRAINT masterkiosk_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_statint_check CHECK (statint IN ('0', '1'));

ALTER TABLE public.mastermerk
    ADD CONSTRAINT mastermerk_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_statnpwpd_check CHECK (statnpwpd IN ('0', '1'));

ALTER TABLE public.masterpegawai
    ADD CONSTRAINT masterpegawai_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterprovinsi
    ADD CONSTRAINT masterprovinsi_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterrekd
    ADD CONSTRAINT masterrekd_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterrt
    ADD CONSTRAINT masterrt_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterrw
    ADD CONSTRAINT masterrw_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterteks
    ADD CONSTRAINT masterteks_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masteruunjop
    ADD CONSTRAINT masteruunjop_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_statint_check CHECK (statint IN ('0', '1'));

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_insidentil_check CHECK (insidentil IN ('0', '1'));

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_insidentil_check CHECK (insidentil IN ('0', '1'));

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_insidentil_check CHECK (insidentil IN ('0', '1'));

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_validjr_check CHECK (validjr IN ('0', '1'));

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_validpol_check CHECK (validpol IN ('0', '1'));

ALTER TABLE public.transhistpendataan
    ADD CONSTRAINT transhistpendataan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_statbayar_check CHECK (statbayar IN ('0', '1'));

ALTER TABLE public.transpendataan
    ADD CONSTRAINT transpendataan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transpendataandet
    ADD CONSTRAINT transpendataandet_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_status_check CHECK (status IN ('0', '1'));

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_statbayar_check CHECK (statbayar IN ('0', '1'));

ALTER TABLE public.transsts
    ADD CONSTRAINT transsts_statbayar_check CHECK (statbayar IN ('0', '1'));

ALTER TABLE public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_statantri_check CHECK (statantri IN ('0', '1'));

ALTER TABLE public.jnsgolongan
    ADD CONSTRAINT jnsgolongan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnshist
    ADD CONSTRAINT jnshist_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnskatkendaraan
    ADD CONSTRAINT jnskatkendaraan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnsmilik
    ADD CONSTRAINT jnsmilik_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnsranmor
    ADD CONSTRAINT jnsranmor_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnstarif
    ADD CONSTRAINT jnstarif_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.jnsumum
    ADD CONSTRAINT jnsumum_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterbank
    ADD CONSTRAINT masterbank_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterflow
    ADD CONSTRAINT masterflow_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterhapusdenda
    ADD CONSTRAINT masterhapusdenda_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_statint_fkey FOREIGN KEY (statint)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_insidentil_fkey FOREIGN KEY (insidentil)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterjabttd
    ADD CONSTRAINT masterjabttd_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_selfassessment_fkey FOREIGN KEY (selfassessment)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkabkota
    ADD CONSTRAINT masterkabkota_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkabkotaall
    ADD CONSTRAINT masterkabkotaall_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkecamatan
    ADD CONSTRAINT masterkecamatan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkelurahan
    ADD CONSTRAINT masterkelurahan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkiosk
    ADD CONSTRAINT masterkiosk_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_statint_fkey FOREIGN KEY (statint)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.mastermerk
    ADD CONSTRAINT mastermerk_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_statnpwpd_fkey FOREIGN KEY (statnpwpd)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterpegawai
    ADD CONSTRAINT masterpegawai_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterprovinsi
    ADD CONSTRAINT masterprovinsi_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterrekd
    ADD CONSTRAINT masterrekd_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterrt
    ADD CONSTRAINT masterrt_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterrw
    ADD CONSTRAINT masterrw_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterteks
    ADD CONSTRAINT masterteks_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masteruunjop
    ADD CONSTRAINT masteruunjop_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_statint_fkey FOREIGN KEY (statint)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_insidentil_fkey FOREIGN KEY (insidentil)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_insidentil_fkey FOREIGN KEY (insidentil)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_insidentil_fkey FOREIGN KEY (insidentil)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_validjr_fkey FOREIGN KEY (validjr)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_validpol_fkey FOREIGN KEY (validpol)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transhistpendataan
    ADD CONSTRAINT transhistpendataan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_statbayar_fkey FOREIGN KEY (statbayar)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transpendataan
    ADD CONSTRAINT transpendataan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transpendataandet
    ADD CONSTRAINT transpendataandet_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_status_fkey FOREIGN KEY (status)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_statbayar_fkey FOREIGN KEY (statbayar)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transsts
    ADD CONSTRAINT transsts_statbayar_fkey FOREIGN KEY (statbayar)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_statantri_fkey FOREIGN KEY (statantri)
        REFERENCES public.ref_flag (flag_code);

ALTER TABLE public.appotor
    ADD CONSTRAINT appotor_kdgroup_fkey FOREIGN KEY (kdgroup)
        REFERENCES public.appgroupuser (kdgroup);

ALTER TABLE public.appotor
    ADD CONSTRAINT appotor_roleid_fkey FOREIGN KEY (roleid)
        REFERENCES public.approle (roleid);

ALTER TABLE public.appuser
    ADD CONSTRAINT appuser_kdgroup_fkey FOREIGN KEY (kdgroup)
        REFERENCES public.appgroupuser (kdgroup);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idkabkokta_fkey FOREIGN KEY (idkabkokta)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idkecamatan_fkey FOREIGN KEY (idkecamatan)
        REFERENCES public.masterkecamatan (idkecamatan);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idkelurahan_fkey FOREIGN KEY (idkelurahan)
        REFERENCES public.masterkelurahan (idkelurahan);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idrw_fkey FOREIGN KEY (idrw)
        REFERENCES public.masterrw (idrw);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idrt_fkey FOREIGN KEY (idrt)
        REFERENCES public.masterrt (idrt);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_jnskendid_fkey FOREIGN KEY (jnskendid)
        REFERENCES public.jnskendaraan (jnskendid);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_idmerk_fkey FOREIGN KEY (idmerk)
        REFERENCES public.mastermerk (idmerk);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_kdmilik_fkey FOREIGN KEY (kdmilik)
        REFERENCES public.jnsmilik (kdmilik);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_kdguna_fkey FOREIGN KEY (kdguna)
        REFERENCES public.jnsguna (kdguna);

ALTER TABLE public.masterab
    ADD CONSTRAINT masterab_kdplat_fkey FOREIGN KEY (kdplat)
        REFERENCES public.jnsplat (kdplat);

ALTER TABLE public.masterabdet
    ADD CONSTRAINT masterabdet_idab_fkey FOREIGN KEY (idab)
        REFERENCES public.masterab (idab);

ALTER TABLE public.masterabdet
    ADD CONSTRAINT masterabdet_idjnsd_fkey FOREIGN KEY (idjnsd)
        REFERENCES public.masterjnspendapatan (idjnsd);

ALTER TABLE public.masterbadan
    ADD CONSTRAINT masterbadan_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterbadan
    ADD CONSTRAINT masterbadan_idprovinsi_fkey FOREIGN KEY (idprovinsi)
        REFERENCES public.masterprovinsi (idprovinsi);

ALTER TABLE public.masterbadan
    ADD CONSTRAINT masterbadan_idkabkokta_fkey FOREIGN KEY (idkabkokta)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_idpegawai_fkey FOREIGN KEY (idpegawai)
        REFERENCES public.masterpegawai (idpegawai);

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_idbank_fkey FOREIGN KEY (idbank)
        REFERENCES public.masterbank (idbank);

ALTER TABLE public.masterbendahara
    ADD CONSTRAINT masterbendahara_idreknrc_fkey FOREIGN KEY (idreknrc)
        REFERENCES public.masterreknrc (idreknrc);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_idwp_fkey FOREIGN KEY (idwp)
        REFERENCES public.masterwp (idwp);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_jnskendid_fkey FOREIGN KEY (jnskendid)
        REFERENCES public.jnskendaraan (jnskendid);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_idmerk_fkey FOREIGN KEY (idmerk)
        REFERENCES public.mastermerk (idmerk);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_kdmilik_fkey FOREIGN KEY (kdmilik)
        REFERENCES public.jnsmilik (kdmilik);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_kdguna_fkey FOREIGN KEY (kdguna)
        REFERENCES public.jnsguna (kdguna);

ALTER TABLE public.masterhistory
    ADD CONSTRAINT masterhistory_kdplat_fkey FOREIGN KEY (kdplat)
        REFERENCES public.jnsplat (kdplat);

ALTER TABLE public.masterjabttd
    ADD CONSTRAINT masterjabttd_kddok_fkey FOREIGN KEY (kddok)
        REFERENCES public.jnsdok (kddok);

ALTER TABLE public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_parentid_fkey FOREIGN KEY (parentid)
        REFERENCES public.masterjnspendapatan (idjnsd);

ALTER TABLE public.masterkabkota
    ADD CONSTRAINT masterkabkota_idprovinsi_fkey FOREIGN KEY (idprovinsi)
        REFERENCES public.masterprovinsi (idprovinsi);

ALTER TABLE public.masterkabkotaall
    ADD CONSTRAINT masterkabkotaall_idprovinsi_fkey FOREIGN KEY (idprovinsi)
        REFERENCES public.masterprovinsi (idprovinsi);

ALTER TABLE public.masterkaupt
    ADD CONSTRAINT masterkaupt_idpegawai_fkey FOREIGN KEY (idpegawai)
        REFERENCES public.masterpegawai (idpegawai);

ALTER TABLE public.masterkaupt
    ADD CONSTRAINT masterkaupt_idupt_fkey FOREIGN KEY (idupt)
        REFERENCES public.masterupt (idupt);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idkabkokta_fkey FOREIGN KEY (idkabkokta)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idkecamatan_fkey FOREIGN KEY (idkecamatan)
        REFERENCES public.masterkecamatan (idkecamatan);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idkelurahan_fkey FOREIGN KEY (idkelurahan)
        REFERENCES public.masterkelurahan (idkelurahan);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idrw_fkey FOREIGN KEY (idrw)
        REFERENCES public.masterrw (idrw);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idrt_fkey FOREIGN KEY (idrt)
        REFERENCES public.masterrt (idrt);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_jnskendid_fkey FOREIGN KEY (jnskendid)
        REFERENCES public.jnskendaraan (jnskendid);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_idmerk_fkey FOREIGN KEY (idmerk)
        REFERENCES public.mastermerk (idmerk);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_kdmilik_fkey FOREIGN KEY (kdmilik)
        REFERENCES public.jnsmilik (kdmilik);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_kdguna_fkey FOREIGN KEY (kdguna)
        REFERENCES public.jnsguna (kdguna);

ALTER TABLE public.masterkb
    ADD CONSTRAINT masterkb_kdplat_fkey FOREIGN KEY (kdplat)
        REFERENCES public.jnsplat (kdplat);

ALTER TABLE public.masterkbdet
    ADD CONSTRAINT masterkbdet_idkb_fkey FOREIGN KEY (idkb)
        REFERENCES public.masterkb (idkb);

ALTER TABLE public.masterkbdet
    ADD CONSTRAINT masterkbdet_idjnsd_fkey FOREIGN KEY (idjnsd)
        REFERENCES public.masterjnspendapatan (idjnsd);

ALTER TABLE public.masterkecamatan
    ADD CONSTRAINT masterkecamatan_idkabkota_fkey FOREIGN KEY (idkabkota)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterkelurahan
    ADD CONSTRAINT masterkelurahan_idkecamatan_fkey FOREIGN KEY (idkecamatan)
        REFERENCES public.masterkecamatan (idkecamatan);

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_idkabkokta_fkey FOREIGN KEY (idkabkokta)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_idkecamatan_fkey FOREIGN KEY (idkecamatan)
        REFERENCES public.masterkecamatan (idkecamatan);

ALTER TABLE public.masterktp
    ADD CONSTRAINT masterktp_idkelurahan_fkey FOREIGN KEY (idkelurahan)
        REFERENCES public.masterkelurahan (idkelurahan);

ALTER TABLE public.masterlibur
    ADD CONSTRAINT masterlibur_idkabkota_fkey FOREIGN KEY (idkabkota)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_idbadan_fkey FOREIGN KEY (idbadan)
        REFERENCES public.masterbadan (idbadan);

ALTER TABLE public.masternpwpd
    ADD CONSTRAINT masternpwpd_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterpegawai
    ADD CONSTRAINT masterpegawai_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterpegawai
    ADD CONSTRAINT masterpegawai_idupt_fkey FOREIGN KEY (idupt)
        REFERENCES public.masterupt (idupt);

ALTER TABLE public.masterrekd
    ADD CONSTRAINT masterrekd_kdjnspjk_fkey FOREIGN KEY (kdjnspjk)
        REFERENCES public.jnspajak (kdjnspjk);

ALTER TABLE public.masterrt
    ADD CONSTRAINT masterrt_idrw_fkey FOREIGN KEY (idrw)
        REFERENCES public.masterrw (idrw);

ALTER TABLE public.masterrw
    ADD CONSTRAINT masterrw_idkelurahan_fkey FOREIGN KEY (idkelurahan)
        REFERENCES public.masterkelurahan (idkelurahan);

ALTER TABLE public.mastertarif
    ADD CONSTRAINT mastertarif_kdjnspjk_fkey FOREIGN KEY (kdjnspjk)
        REFERENCES public.jnspajak (kdjnspjk);

ALTER TABLE public.mastertarif
    ADD CONSTRAINT mastertarif_jnskendid_fkey FOREIGN KEY (jnskendid)
        REFERENCES public.jnskendaraan (jnskendid);

ALTER TABLE public.mastertarif
    ADD CONSTRAINT mastertarif_kdflow_fkey FOREIGN KEY (kdflow)
        REFERENCES public.masterflow (kdflow);

ALTER TABLE public.mastertarif
    ADD CONSTRAINT mastertarif_kdplat_fkey FOREIGN KEY (kdplat)
        REFERENCES public.jnsplat (kdplat);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_iduunjop_fkey FOREIGN KEY (iduunjop)
        REFERENCES public.masteruunjop (iduunjop);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_idrekd_fkey FOREIGN KEY (idrekd)
        REFERENCES public.masterrekd (idrekd);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_kdjnstarif_fkey FOREIGN KEY (kdjnstarif)
        REFERENCES public.jnstarif (kdjnstarif);

ALTER TABLE public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_idmerk_fkey FOREIGN KEY (idmerk)
        REFERENCES public.mastermerk (idmerk);

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_idbank_fkey FOREIGN KEY (idbank)
        REFERENCES public.masterbank (idbank);

ALTER TABLE public.masterupt
    ADD CONSTRAINT masterupt_idkabkota_fkey FOREIGN KEY (idkabkota)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idkabkokta_fkey FOREIGN KEY (idkabkokta)
        REFERENCES public.masterkabkota (idkabkota);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idkecamatan_fkey FOREIGN KEY (idkecamatan)
        REFERENCES public.masterkecamatan (idkecamatan);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idkelurahan_fkey FOREIGN KEY (idkelurahan)
        REFERENCES public.masterkelurahan (idkelurahan);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idrw_fkey FOREIGN KEY (idrw)
        REFERENCES public.masterrw (idrw);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idrt_fkey FOREIGN KEY (idrt)
        REFERENCES public.masterrt (idrt);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_jnskendid_fkey FOREIGN KEY (jnskendid)
        REFERENCES public.jnskendaraan (jnskendid);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_idmerk_fkey FOREIGN KEY (idmerk)
        REFERENCES public.mastermerk (idmerk);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_kdmilik_fkey FOREIGN KEY (kdmilik)
        REFERENCES public.jnsmilik (kdmilik);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_kdguna_fkey FOREIGN KEY (kdguna)
        REFERENCES public.jnsguna (kdguna);

ALTER TABLE public.masterwp
    ADD CONSTRAINT masterwp_kdplat_fkey FOREIGN KEY (kdplat)
        REFERENCES public.jnsplat (kdplat);

ALTER TABLE public.masterwpdata
    ADD CONSTRAINT masterwpdata_idjnsd_fkey FOREIGN KEY (idjnsd)
        REFERENCES public.masterjnspendapatan (idjnsd);

ALTER TABLE public.masterwpdata
    ADD CONSTRAINT masterwpdata_idwp_fkey FOREIGN KEY (idwp)
        REFERENCES public.masterwp (idwp);

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_idwp_fkey FOREIGN KEY (idwp)
        REFERENCES public.masterwp (idwp);

ALTER TABLE public.transdatakohir
    ADD CONSTRAINT transdatakohir_idupt_fkey FOREIGN KEY (idupt)
        REFERENCES public.masterupt (idupt);

ALTER TABLE public.transhistpendataan
    ADD CONSTRAINT transhistpendataan_idwpdata_fkey FOREIGN KEY (idwpdata)
        REFERENCES public.masterwpdata (idwpdata);

ALTER TABLE public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_idhistpendataan_fkey FOREIGN KEY (idhistpendataan)
        REFERENCES public.transhistpendataan (idhistpendataan);

ALTER TABLE public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_idpenetapan_fkey FOREIGN KEY (idpenetapan)
        REFERENCES public.transpenetapan (idpenetapan);

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_idkohir_fkey FOREIGN KEY (idkohir)
        REFERENCES public.transdatakohir (idkohir);

ALTER TABLE public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_idwpdata_fkey FOREIGN KEY (idwpdata)
        REFERENCES public.masterwpdata (idwpdata);

ALTER TABLE public.transpendataan
    ADD CONSTRAINT transpendataan_idwpdata_fkey FOREIGN KEY (idwpdata)
        REFERENCES public.masterwpdata (idwpdata);

ALTER TABLE public.transpendataandet
    ADD CONSTRAINT transpendataandet_idpendataan_fkey FOREIGN KEY (idpendataan)
        REFERENCES public.transpendataan (idpendataan);

ALTER TABLE public.transpendataandet
    ADD CONSTRAINT transpendataandet_idpenetapan_fkey FOREIGN KEY (idpenetapan)
        REFERENCES public.transpenetapan (idpenetapan);

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_idkohir_fkey FOREIGN KEY (idkohir)
        REFERENCES public.transdatakohir (idkohir);

ALTER TABLE public.transpenetapan
    ADD CONSTRAINT transpenetapan_idwpdata_fkey FOREIGN KEY (idwpdata)
        REFERENCES public.masterwpdata (idwpdata);

ALTER TABLE public.transsts
    ADD CONSTRAINT transsts_idupt_fkey FOREIGN KEY (idupt)
        REFERENCES public.masterupt (idupt);

ALTER TABLE public.transsts
    ADD CONSTRAINT transsts_idbend_fkey FOREIGN KEY (idbend)
        REFERENCES public.masterbendahara (idbend);

ALTER TABLE public.transstsdet
    ADD CONSTRAINT transstsdet_idsts_fkey FOREIGN KEY (idsts)
        REFERENCES public.transsts (idsts);

ALTER TABLE public.transstsdet
    ADD CONSTRAINT transstsdet_idrekd_fkey FOREIGN KEY (idrekd)
        REFERENCES public.masterrekd (idrekd);

ALTER TABLE public.transwpdata
    ADD CONSTRAINT transwpdata_idnpwpd_fkey FOREIGN KEY (idnpwpd)
        REFERENCES public.masternpwpd (idnpwpd);

ALTER TABLE public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_idtwpdata_fkey FOREIGN KEY (idtwpdata)
        REFERENCES public.transwpdata (idtwpdata);

ALTER TABLE public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_idktp_fkey FOREIGN KEY (idktp)
        REFERENCES public.masterktp (idktp);

ALTER TABLE public.transwpdatafile
    ADD CONSTRAINT transwpdatafile_idtwpdata_fkey FOREIGN KEY (idtwpdata)
        REFERENCES public.transwpdata (idtwpdata);

CREATE INDEX idx_appotor_kdgroup ON public.appotor (kdgroup);
CREATE INDEX idx_appotor_roleid ON public.appotor (roleid);
CREATE INDEX idx_appuser_kdgroup ON public.appuser (kdgroup);
CREATE INDEX idx_masterab_idktp ON public.masterab (idktp);
CREATE INDEX idx_masterab_idkabkokta ON public.masterab (idkabkokta);
CREATE INDEX idx_masterab_idkecamatan ON public.masterab (idkecamatan);
CREATE INDEX idx_masterab_idkelurahan ON public.masterab (idkelurahan);
CREATE INDEX idx_masterab_idrw ON public.masterab (idrw);
CREATE INDEX idx_masterab_idrt ON public.masterab (idrt);
CREATE INDEX idx_masterab_jnskendid ON public.masterab (jnskendid);
CREATE INDEX idx_masterab_idmerk ON public.masterab (idmerk);
CREATE INDEX idx_masterab_kdmilik ON public.masterab (kdmilik);
CREATE INDEX idx_masterab_kdguna ON public.masterab (kdguna);
CREATE INDEX idx_masterab_kdplat ON public.masterab (kdplat);
CREATE INDEX idx_masterabdet_idab ON public.masterabdet (idab);
CREATE INDEX idx_masterabdet_idjnsd ON public.masterabdet (idjnsd);
CREATE INDEX idx_masterbadan_idktp ON public.masterbadan (idktp);
CREATE INDEX idx_masterbadan_idprovinsi ON public.masterbadan (idprovinsi);
CREATE INDEX idx_masterbadan_idkabkokta ON public.masterbadan (idkabkokta);
CREATE INDEX idx_masterbendahara_idpegawai ON public.masterbendahara (idpegawai);
CREATE INDEX idx_masterbendahara_idbank ON public.masterbendahara (idbank);
CREATE INDEX idx_masterbendahara_idreknrc ON public.masterbendahara (idreknrc);
CREATE INDEX idx_masterhistory_idwp ON public.masterhistory (idwp);
CREATE INDEX idx_masterhistory_idktp ON public.masterhistory (idktp);
CREATE INDEX idx_masterhistory_jnskendid ON public.masterhistory (jnskendid);
CREATE INDEX idx_masterhistory_idmerk ON public.masterhistory (idmerk);
CREATE INDEX idx_masterhistory_kdmilik ON public.masterhistory (kdmilik);
CREATE INDEX idx_masterhistory_kdguna ON public.masterhistory (kdguna);
CREATE INDEX idx_masterhistory_kdplat ON public.masterhistory (kdplat);
CREATE INDEX idx_masterjabttd_kddok ON public.masterjabttd (kddok);
CREATE INDEX idx_masterjnspendapatan_parentid ON public.masterjnspendapatan (parentid);
CREATE INDEX idx_masterkabkota_idprovinsi ON public.masterkabkota (idprovinsi);
CREATE INDEX idx_masterkabkotaall_idprovinsi ON public.masterkabkotaall (idprovinsi);
CREATE INDEX idx_masterkaupt_idpegawai ON public.masterkaupt (idpegawai);
CREATE INDEX idx_masterkaupt_idupt ON public.masterkaupt (idupt);
CREATE INDEX idx_masterkb_idktp ON public.masterkb (idktp);
CREATE INDEX idx_masterkb_idkabkokta ON public.masterkb (idkabkokta);
CREATE INDEX idx_masterkb_idkecamatan ON public.masterkb (idkecamatan);
CREATE INDEX idx_masterkb_idkelurahan ON public.masterkb (idkelurahan);
CREATE INDEX idx_masterkb_idrw ON public.masterkb (idrw);
CREATE INDEX idx_masterkb_idrt ON public.masterkb (idrt);
CREATE INDEX idx_masterkb_jnskendid ON public.masterkb (jnskendid);
CREATE INDEX idx_masterkb_idmerk ON public.masterkb (idmerk);
CREATE INDEX idx_masterkb_kdmilik ON public.masterkb (kdmilik);
CREATE INDEX idx_masterkb_kdguna ON public.masterkb (kdguna);
CREATE INDEX idx_masterkb_kdplat ON public.masterkb (kdplat);
CREATE INDEX idx_masterkbdet_idkb ON public.masterkbdet (idkb);
CREATE INDEX idx_masterkbdet_idjnsd ON public.masterkbdet (idjnsd);
CREATE INDEX idx_masterkecamatan_idkabkota ON public.masterkecamatan (idkabkota);
CREATE INDEX idx_masterkelurahan_idkecamatan ON public.masterkelurahan (idkecamatan);
CREATE INDEX idx_masterktp_idkabkokta ON public.masterktp (idkabkokta);
CREATE INDEX idx_masterktp_idkecamatan ON public.masterktp (idkecamatan);
CREATE INDEX idx_masterktp_idkelurahan ON public.masterktp (idkelurahan);
CREATE INDEX idx_masterlibur_idkabkota ON public.masterlibur (idkabkota);
CREATE INDEX idx_masternpwpd_idbadan ON public.masternpwpd (idbadan);
CREATE INDEX idx_masternpwpd_idktp ON public.masternpwpd (idktp);
CREATE INDEX idx_masterpegawai_idktp ON public.masterpegawai (idktp);
CREATE INDEX idx_masterpegawai_idupt ON public.masterpegawai (idupt);
CREATE INDEX idx_masterrekd_kdjnspjk ON public.masterrekd (kdjnspjk);
CREATE INDEX idx_masterrt_idrw ON public.masterrt (idrw);
CREATE INDEX idx_masterrw_idkelurahan ON public.masterrw (idkelurahan);
CREATE INDEX idx_mastertarif_kdjnspjk ON public.mastertarif (kdjnspjk);
CREATE INDEX idx_mastertarif_jnskendid ON public.mastertarif (jnskendid);
CREATE INDEX idx_mastertarif_kdflow ON public.mastertarif (kdflow);
CREATE INDEX idx_mastertarif_kdplat ON public.mastertarif (kdplat);
CREATE INDEX idx_mastertarifnjop_iduunjop ON public.mastertarifnjop (iduunjop);
CREATE INDEX idx_mastertarifnjop_idrekd ON public.mastertarifnjop (idrekd);
CREATE INDEX idx_mastertarifnjop_kdjnstarif ON public.mastertarifnjop (kdjnstarif);
CREATE INDEX idx_mastertarifnjop_idmerk ON public.mastertarifnjop (idmerk);
CREATE INDEX idx_masterupt_idbank ON public.masterupt (idbank);
CREATE INDEX idx_masterupt_idkabkota ON public.masterupt (idkabkota);
CREATE INDEX idx_masterwp_idktp ON public.masterwp (idktp);
CREATE INDEX idx_masterwp_idkabkokta ON public.masterwp (idkabkokta);
CREATE INDEX idx_masterwp_idkecamatan ON public.masterwp (idkecamatan);
CREATE INDEX idx_masterwp_idkelurahan ON public.masterwp (idkelurahan);
CREATE INDEX idx_masterwp_idrw ON public.masterwp (idrw);
CREATE INDEX idx_masterwp_idrt ON public.masterwp (idrt);
CREATE INDEX idx_masterwp_jnskendid ON public.masterwp (jnskendid);
CREATE INDEX idx_masterwp_idmerk ON public.masterwp (idmerk);
CREATE INDEX idx_masterwp_kdmilik ON public.masterwp (kdmilik);
CREATE INDEX idx_masterwp_kdguna ON public.masterwp (kdguna);
CREATE INDEX idx_masterwp_kdplat ON public.masterwp (kdplat);
CREATE INDEX idx_masterwpdata_idjnsd ON public.masterwpdata (idjnsd);
CREATE INDEX idx_masterwpdata_idwp ON public.masterwpdata (idwp);
CREATE INDEX idx_transdatakohir_idwp ON public.transdatakohir (idwp);
CREATE INDEX idx_transdatakohir_idupt ON public.transdatakohir (idupt);
CREATE INDEX idx_transhistpendataan_idwpdata ON public.transhistpendataan (idwpdata);
CREATE INDEX idx_transhistpendataandet_idhistpendataan ON public.transhistpendataandet (idhistpendataan);
CREATE INDEX idx_transhistpendataandet_idpenetapan ON public.transhistpendataandet (idpenetapan);
CREATE INDEX idx_transhistpenetapan_idkohir ON public.transhistpenetapan (idkohir);
CREATE INDEX idx_transhistpenetapan_idwpdata ON public.transhistpenetapan (idwpdata);
CREATE INDEX idx_transpendataan_idwpdata ON public.transpendataan (idwpdata);
CREATE INDEX idx_transpendataandet_idpendataan ON public.transpendataandet (idpendataan);
CREATE INDEX idx_transpendataandet_idpenetapan ON public.transpendataandet (idpenetapan);
CREATE INDEX idx_transpenetapan_idkohir ON public.transpenetapan (idkohir);
CREATE INDEX idx_transpenetapan_idwpdata ON public.transpenetapan (idwpdata);
CREATE INDEX idx_transsts_idupt ON public.transsts (idupt);
CREATE INDEX idx_transsts_idbend ON public.transsts (idbend);
CREATE INDEX idx_transstsdet_idsts ON public.transstsdet (idsts);
CREATE INDEX idx_transstsdet_idrekd ON public.transstsdet (idrekd);
CREATE INDEX idx_transwpdata_idnpwpd ON public.transwpdata (idnpwpd);
CREATE INDEX idx_transwpdataantri_idtwpdata ON public.transwpdataantri (idtwpdata);
CREATE INDEX idx_transwpdataantri_idktp ON public.transwpdataantri (idktp);
CREATE INDEX idx_transwpdatafile_idtwpdata ON public.transwpdatafile (idtwpdata);

CREATE TRIGGER set_updated_at_appgroupuser
    BEFORE UPDATE ON public.appgroupuser
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_appotor
    BEFORE UPDATE ON public.appotor
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_approle
    BEFORE UPDATE ON public.approle
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_appuser
    BEFORE UPDATE ON public.appuser
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsdok
    BEFORE UPDATE ON public.jnsdok
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsgolongan
    BEFORE UPDATE ON public.jnsgolongan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsguna
    BEFORE UPDATE ON public.jnsguna
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnshist
    BEFORE UPDATE ON public.jnshist
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsjr
    BEFORE UPDATE ON public.jnsjr
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnskatkendaraan
    BEFORE UPDATE ON public.jnskatkendaraan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnskendaraan
    BEFORE UPDATE ON public.jnskendaraan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsmilik
    BEFORE UPDATE ON public.jnsmilik
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnspajak
    BEFORE UPDATE ON public.jnspajak
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsplat
    BEFORE UPDATE ON public.jnsplat
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsprogresif
    BEFORE UPDATE ON public.jnsprogresif
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsranmor
    BEFORE UPDATE ON public.jnsranmor
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsstrurek
    BEFORE UPDATE ON public.jnsstrurek
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnstarif
    BEFORE UPDATE ON public.jnstarif
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_jnsumum
    BEFORE UPDATE ON public.jnsumum
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_mapjnspendapatan
    BEFORE UPDATE ON public.mapjnspendapatan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterab
    BEFORE UPDATE ON public.masterab
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterabdet
    BEFORE UPDATE ON public.masterabdet
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterbadan
    BEFORE UPDATE ON public.masterbadan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterbank
    BEFORE UPDATE ON public.masterbank
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterbbm
    BEFORE UPDATE ON public.masterbbm
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterbendahara
    BEFORE UPDATE ON public.masterbendahara
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterflow
    BEFORE UPDATE ON public.masterflow
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterhapusdenda
    BEFORE UPDATE ON public.masterhapusdenda
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterhistory
    BEFORE UPDATE ON public.masterhistory
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterjabttd
    BEFORE UPDATE ON public.masterjabttd
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterjnspendapatan
    BEFORE UPDATE ON public.masterjnspendapatan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkabkota
    BEFORE UPDATE ON public.masterkabkota
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkabkotaall
    BEFORE UPDATE ON public.masterkabkotaall
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkaupt
    BEFORE UPDATE ON public.masterkaupt
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkb
    BEFORE UPDATE ON public.masterkb
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkbdet
    BEFORE UPDATE ON public.masterkbdet
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkecamatan
    BEFORE UPDATE ON public.masterkecamatan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkelurahan
    BEFORE UPDATE ON public.masterkelurahan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterkiosk
    BEFORE UPDATE ON public.masterkiosk
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterktp
    BEFORE UPDATE ON public.masterktp
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterlibur
    BEFORE UPDATE ON public.masterlibur
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_mastermerk
    BEFORE UPDATE ON public.mastermerk
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masternpwpd
    BEFORE UPDATE ON public.masternpwpd
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterpegawai
    BEFORE UPDATE ON public.masterpegawai
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterprovinsi
    BEFORE UPDATE ON public.masterprovinsi
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterrekd
    BEFORE UPDATE ON public.masterrekd
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterreknrc
    BEFORE UPDATE ON public.masterreknrc
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterrt
    BEFORE UPDATE ON public.masterrt
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterrw
    BEFORE UPDATE ON public.masterrw
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_mastertarif
    BEFORE UPDATE ON public.mastertarif
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_mastertarifnjop
    BEFORE UPDATE ON public.mastertarifnjop
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterteks
    BEFORE UPDATE ON public.masterteks
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterupt
    BEFORE UPDATE ON public.masterupt
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masteruunjop
    BEFORE UPDATE ON public.masteruunjop
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterwp
    BEFORE UPDATE ON public.masterwp
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_masterwpdata
    BEFORE UPDATE ON public.masterwpdata
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transdatakohir
    BEFORE UPDATE ON public.transdatakohir
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transhistpendataan
    BEFORE UPDATE ON public.transhistpendataan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transhistpendataandet
    BEFORE UPDATE ON public.transhistpendataandet
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transhistpenetapan
    BEFORE UPDATE ON public.transhistpenetapan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transpendataan
    BEFORE UPDATE ON public.transpendataan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transpendataandet
    BEFORE UPDATE ON public.transpendataandet
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transpenetapan
    BEFORE UPDATE ON public.transpenetapan
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transsts
    BEFORE UPDATE ON public.transsts
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transstsdet
    BEFORE UPDATE ON public.transstsdet
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transwpdata
    BEFORE UPDATE ON public.transwpdata
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transwpdataantri
    BEFORE UPDATE ON public.transwpdataantri
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
CREATE TRIGGER set_updated_at_transwpdatafile
    BEFORE UPDATE ON public.transwpdatafile
    FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();

COMMENT ON TABLE public.masterwp IS 'Data wajib pajak utama.';
COMMENT ON TABLE public.masterhistory IS 'Riwayat perubahan data wajib pajak.';
COMMENT ON TABLE public.mastertarifnjop IS 'Tarif NJOP kendaraan.';
COMMENT ON TABLE public.masterwpdata IS 'Data pendataan wajib pajak.';
COMMENT ON TABLE public.ref_flag IS 'Referensi nilai flag status 0/1.';
COMMENT ON COLUMN public.masterwp.status IS 'Status aktif/nonaktif (0/1).';
COMMENT ON COLUMN public.masterhistory.status IS 'Status aktif/nonaktif (0/1).';
COMMENT ON COLUMN public.transpenetapan.statbayar IS 'Status pembayaran (0/1).';
COMMENT ON COLUMN public.transhistpenetapan.statbayar IS 'Status pembayaran (0/1).';
COMMENT ON COLUMN public.transdatakohir.validjr IS 'Validasi JR (0/1).';
COMMENT ON COLUMN public.transdatakohir.validpol IS 'Validasi polisi (0/1).';


--
-- TOC entry 5403 (class 0 OID 17027)
-- Dependencies: 215
-- Data for Name: appgroupuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appgroupuser (kdgroup, nmgroup, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5413 (class 0 OID 17121)
-- Dependencies: 225
-- Data for Name: appotor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appotor (kdgroup, roleid, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5404 (class 0 OID 17041)
-- Dependencies: 216
-- Data for Name: approle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.approle (roleid, idapp, role, role_type, menuid, parentid, bantuan, link, icon, kdlevel, is_show, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5405 (class 0 OID 17050)
-- Dependencies: 217
-- Data for Name: appuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appuser (userid, idupt, kdtahap, pwd, idpeg, kdgroup, nik, nama, email, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5406 (class 0 OID 17059)
-- Dependencies: 218
-- Data for Name: jnsdok; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsdok (kddok, namadok, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5407 (class 0 OID 17066)
-- Dependencies: 219
-- Data for Name: jnsgolongan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsgolongan (jnsgolid, golongan, katid, jnskendid, viewall, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5408 (class 0 OID 17073)
-- Dependencies: 220
-- Data for Name: jnsguna; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsguna (kdguna, guna, gunaplat, progresif, groupbpkb, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5409 (class 0 OID 17080)
-- Dependencies: 221
-- Data for Name: jnshist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnshist (kdhist, nmhist, kdflow, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5410 (class 0 OID 17087)
-- Dependencies: 222
-- Data for Name: jnsjr; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsjr (jnsjrid, kodejr, goljns, pu, roda, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5411 (class 0 OID 17094)
-- Dependencies: 223
-- Data for Name: jnskatkendaraan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnskatkendaraan (katid, kendaraan, jenisbpkb, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5412 (class 0 OID 17102)
-- Dependencies: 224
-- Data for Name: jnskendaraan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnskendaraan (jnskendid, jnskend, katid, jnsjrid, golpjr, golujr, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5414 (class 0 OID 17128)
-- Dependencies: 226
-- Data for Name: jnsmilik; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsmilik (kdmilik, milik, bpkpid, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5415 (class 0 OID 17135)
-- Dependencies: 227
-- Data for Name: jnspajak; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnspajak (kdjnspjk, nmjnspjk, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5416 (class 0 OID 17142)
-- Dependencies: 228
-- Data for Name: jnsplat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsplat (kdplat, plat, pu, platjr, numpkb, numbbn1, numbbn2, umorg, umbrg, dnumpkb, dnumbbn, dumorg, dumbrg, abpkb, abbbn1, abbbn2, numfiskal, snid, opspkb, opsbbn, opsnumpkb, opsnumbbn1, opsnumbbn2, opsdnumpkb, opsdnumbbn, minnumpkb, minnumbbn1, minnumbbn2, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5417 (class 0 OID 17149)
-- Dependencies: 229
-- Data for Name: jnsprogresif; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsprogresif (kdprogresif, progresifr2, progresifr4, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5418 (class 0 OID 17156)
-- Dependencies: 230
-- Data for Name: jnsranmor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsranmor (kdranmor, nmranmor, snid, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5419 (class 0 OID 17163)
-- Dependencies: 231
-- Data for Name: jnsstrurek; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsstrurek (mtglevel, nmlevel, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5420 (class 0 OID 17170)
-- Dependencies: 232
-- Data for Name: jnstarif; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnstarif (kdjnstarif, nmjnstarif, idupt, jnskendid, idrekd, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5421 (class 0 OID 17177)
-- Dependencies: 233
-- Data for Name: jnsumum; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jnsumum (kdumum, nmumum, keterangan, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5423 (class 0 OID 17185)
-- Dependencies: 235
-- Data for Name: mapjnspendapatan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mapjnspendapatan (idmapjnsd, nmjnspendapatan, idrekpkb, idrekbbnkb, idrekopsenpkb, idrekopsenbbnkb, idrekpnbp, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5425 (class 0 OID 17195)
-- Dependencies: 237
-- Data for Name: masterab; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterab (idab, nomorab, namabadan, alamat, idkabkokta, idkecamatan, idkelurahan, idrw, idrt, telepon, fax, idktp, noktp, pekerjaan, tgldaftar, tglfaktur, insidentil, jnskendid, idmerk, merk, tipe, tahunbuat, kodebbm, bbm, cylinder, norangka, nomesin, nobpkb, kdmilik, kdguna, kendke, warna, kdplat, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5427 (class 0 OID 17207)
-- Dependencies: 239
-- Data for Name: masterabdet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterabdet (idabdet, idab, idjnsd, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5429 (class 0 OID 17215)
-- Dependencies: 241
-- Data for Name: masterbadan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterbadan (idbadan, nib, idktp, namabadan, nohp, alamat, tgldaftar, idprovinsi, idkabkokta, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5431 (class 0 OID 17226)
-- Dependencies: 243
-- Data for Name: masterbank; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterbank (idbank, kodebank, namabank, akronimbank, cabangbank, alamatbank, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5432 (class 0 OID 17233)
-- Dependencies: 244
-- Data for Name: masterbbm; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterbbm (kodebbm, namabbm, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5434 (class 0 OID 17241)
-- Dependencies: 246
-- Data for Name: masterbendahara; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterbendahara (idbend, idpegawai, idbank, norek, namarek, jnsbend, status, jabatan, pangkat, uid, koordinator, idreknrc, telepon, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5435 (class 0 OID 17250)
-- Dependencies: 247
-- Data for Name: masterflow; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterflow (kdflow, nmflow, pkb, bbn1, bbn2, swd, atbkend, flowjr, stnkbaru, tnkb, sahstnk, perpanjangstnk, potongan, bataslayanan, satuan, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5437 (class 0 OID 17259)
-- Dependencies: 249
-- Data for Name: masterhapusdenda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterhapusdenda (idhapusdenda, jenis, uraian, awal, akhir, nilai, satuan, ket, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5439 (class 0 OID 17271)
-- Dependencies: 251
-- Data for Name: masterhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterhistory (idhistory, idwp, objekbadanno, namabadan, idgroupusaha, kodepolisi, kodelokasi, idbadan, idklasifikasi, idlokasi, alamat, idkabkokta, idkecamatan, idkelurahan, idrw, idrt, telepon, fax, namapemilik, idktp, pekerjaan, tgldaftar, tglsah, keteblokir, tglhapus, groupblokir, insidentil, nopollama, lastskp, jnskendid, idmerk, merk, tipe, tahunbuat, kodebbm, bbm, cylinder, norangka, nomesin, nobpkb, kdmilik, kdguna, kendke, warna, kdplat, nostnkb, daftarstnk, tglcetakstnk, tglstnk, sdstnk, tglskp, awalskp, akhirskp, tglmutasi, tgljualbeli, nodaftar, nosah1, tglsah1, nosah2, tglsah2, nosah3, tglsah3, nosah4, tglsah4, laporjual, nikpemilik, notelppemilik, putih, status, statint, histid, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5441 (class 0 OID 17287)
-- Dependencies: 253
-- Data for Name: masterjabttd; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterjabttd (idjabttd, idpegawai, kddok, jabatan, ket, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5443 (class 0 OID 17295)
-- Dependencies: 255
-- Data for Name: masterjnspendapatan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterjnspendapatan (idjnsd, nmjnspendapatan, parentid, kdrek, jatuhtempo, status, selfassessment, katid, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5445 (class 0 OID 17303)
-- Dependencies: 257
-- Data for Name: masterkabkota; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkabkota (idkabkota, idprovinsi, kdkabkota, nmkabkota, akronim, ibukota, status, bpkbid, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5447 (class 0 OID 17311)
-- Dependencies: 259
-- Data for Name: masterkabkotaall; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkabkotaall (idkabkotaall, idprovinsi, kdkabkota, nmkabkota, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5449 (class 0 OID 17319)
-- Dependencies: 261
-- Data for Name: masterkaupt; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkaupt (idkaupt, idpegawai, idupt, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5517 (class 0 OID 17664)
-- Dependencies: 329
-- Data for Name: masterkb; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkb (idkb, nomorfaktur, namabadan, alamat, idkabkokta, idkecamatan, idkelurahan, idrw, idrt, telepon, fax, idktp, noktp, pekerjaan, tgldaftar, tglfaktur, insidentil, jnskendid, idmerk, merk, tipe, tahunbuat, kodebbm, bbm, cylinder, norangka, nomesin, nobpkb, kdmilik, kdguna, kendke, warna, kdplat, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5451 (class 0 OID 17328)
-- Dependencies: 263
-- Data for Name: masterkbdet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkbdet (idkbdet, idkb, idjnsd, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5453 (class 0 OID 17336)
-- Dependencies: 265
-- Data for Name: masterkecamatan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkecamatan (idkecamatan, idkabkota, kdkecamatan, nmkecamatan, alamat, telepon, fax, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5455 (class 0 OID 17344)
-- Dependencies: 267
-- Data for Name: masterkelurahan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkelurahan (idkelurahan, idkecamatan, kdkelurahan, nmkelurahan, alamat, telepon, kodepos, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5457 (class 0 OID 17352)
-- Dependencies: 269
-- Data for Name: masterkiosk; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterkiosk (idkios, idparent, kodekiosk, datakiosk, level, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5515 (class 0 OID 17653)
-- Dependencies: 327
-- Data for Name: masterktp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterktp (idktp, nik, nama, agama, nohp, alamat, tgldaftar, idprovinsi, idkabkokta, idkecamatan, idkelurahan, idrw, idrt, kdrt, nikah, tempatlahir, tgllahir, tglregistrasi, nokk, nobpjs, goldarah, email, pendidikan, jeniskelamin, dusun, pekerjaan, namaayah, namaibu, negara, statwn, statint, tglint, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5459 (class 0 OID 17360)
-- Dependencies: 271
-- Data for Name: masterlibur; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterlibur (idlibur, idkabkota, level, tanggal, namalibur, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5461 (class 0 OID 17369)
-- Dependencies: 273
-- Data for Name: mastermerk; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mastermerk (idmerk, kdmerk, nmmerk, keterangan, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5463 (class 0 OID 17377)
-- Dependencies: 275
-- Data for Name: masternpwpd; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masternpwpd (idnpwpd, statnpwpd, npwpd, idbadan, idktp, tgldaftar, nib, namabadan, alamat, status, ket, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5465 (class 0 OID 17387)
-- Dependencies: 277
-- Data for Name: masterpegawai; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterpegawai (idpegawai, idktp, nip, nik, nama, idupt, status, jabatan, pangkat, golongan, uid, telepon, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5467 (class 0 OID 17395)
-- Dependencies: 279
-- Data for Name: masterprovinsi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterprovinsi (idprovinsi, kdprovinsi, nmprovinsi, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5469 (class 0 OID 17403)
-- Dependencies: 281
-- Data for Name: masterrekd; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterrekd (idrekd, idparent, mtglevel, kdrek, nmrek, kdjnspjk, rek_type, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5471 (class 0 OID 17412)
-- Dependencies: 283
-- Data for Name: masterreknrc; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterreknrc (idreknrc, mtglevel, kdrek, nmrek, rek_type, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5473 (class 0 OID 17422)
-- Dependencies: 285
-- Data for Name: masterrt; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterrt (idrt, idrw, kdrt, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5475 (class 0 OID 17430)
-- Dependencies: 287
-- Data for Name: masterrw; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterrw (idrw, idkelurahan, kdrw, alamat, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5477 (class 0 OID 17438)
-- Dependencies: 289
-- Data for Name: mastertarif; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mastertarif (idtarif, kdjnspjk, jnskendid, satuan, awal, akhir, keterangan, kdflow, kdplat, statumum, tarif, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5479 (class 0 OID 17448)
-- Dependencies: 291
-- Data for Name: mastertarifnjop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mastertarifnjop (idtarifnjop, iduunjop, idrekd, kdjnstarif, namatarif, idmerk, tipe, silinder, tahun, kodebbm, njop, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5481 (class 0 OID 17466)
-- Dependencies: 293
-- Data for Name: masterteks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterteks (idteks, datateks, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5483 (class 0 OID 17476)
-- Dependencies: 295
-- Data for Name: masterupt; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterupt (idupt, idparent, kdupt, nmupt, kdlevel, upt_type, akroupt, alamat, telepon, idbank, idkabkota, kepala, koordinator, bendahara, norekb, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5485 (class 0 OID 17486)
-- Dependencies: 297
-- Data for Name: masteruunjop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masteruunjop (iduunjop, noperkada, isiperkada, tahun, status, keterangan, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5487 (class 0 OID 17497)
-- Dependencies: 299
-- Data for Name: masterwp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterwp (idwp, objekbadanno, namabadan, idgroupusaha, kodepolisi, kodelokasi, idbadan, idklasifikasi, idlokasi, alamat, idkabkokta, idkecamatan, idkelurahan, idrw, idrt, telepon, fax, namapemilik, idktp, pekerjaan, tgldaftar, tglsah, keteblokir, tglhapus, groupblokir, insidentil, nopollama, lastskp, jnskendid, idmerk, merk, tipe, tahunbuat, kodebbm, bbm, cylinder, norangka, nomesin, nobpkb, kdmilik, kdguna, kendke, warna, kdplat, nostnkb, daftarstnk, tglcetakstnk, tglstnk, sdstnk, tglskp, awalskp, akhirskp, tglmutasi, tgljualbeli, nodaftar, nosah1, tglsah1, nosah2, tglsah2, nosah3, tglsah3, nosah4, tglsah4, laporjual, nikpemilik, notelppemilik, putih, status, statint, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5489 (class 0 OID 17510)
-- Dependencies: 301
-- Data for Name: masterwpdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.masterwpdata (idwpdata, idjnsd, tglpendataan, idwp, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5491 (class 0 OID 17521)
-- Dependencies: 303
-- Data for Name: transdatakohir; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transdatakohir (idkohir, masaawal, masaakhir, tglpenetapan, penagih, idwp, tglkurangbayar, keterangan, idupt, skrupt, validjr, validjrby, validpol, validpolby, ntpd, tglntpd, idbank, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5493 (class 0 OID 17534)
-- Dependencies: 305
-- Data for Name: transhistpendataan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transhistpendataan (idhistpendataan, idpendataan, spt, idwpdata, tglpendataan, masaawal, masaakhir, uruttgl, jmlomzetawal, tarifpjk, idupt, kdflow, histid, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5495 (class 0 OID 17545)
-- Dependencies: 307
-- Data for Name: transhistpendataandet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transhistpendataandet (idhistpendataandet, idhistpendataan, idpenetapan, nourut, lokasi, transid, ket1, usahaid, tarifpajak, histid, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5497 (class 0 OID 17553)
-- Dependencies: 309
-- Data for Name: transhistpenetapan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transhistpenetapan (idhistpenetapan, idpenetapan, idkohir, nokohir, idwpdata, tglpenetapan, tgljatuhtempo, masaawal, masaakhir, uruttgl, jmlomzetawal, tarifpajak, denda, kenaikan, statbayar, tglbayar, jmlbayar, tglkurangbayar, jmlkurangbayar, jmlperingatan, kdflow, status, opsid, opsprov, opskota, dendaopsprov, dendaopskota, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5499 (class 0 OID 17566)
-- Dependencies: 311
-- Data for Name: transpendataan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transpendataan (idpendataan, spt, idwpdata, tglpendataan, masaawal, masaakhir, uruttgl, jmlomzetawal, tarifpjk, idupt, kdflow, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5501 (class 0 OID 17577)
-- Dependencies: 313
-- Data for Name: transpendataandet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transpendataandet (idpendataandet, idpendataan, idpenetapan, nourut, lokasi, transid, ket1, usahaid, tarifpajak, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5503 (class 0 OID 17585)
-- Dependencies: 315
-- Data for Name: transpenetapan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transpenetapan (idpenetapan, idkohir, nokohir, idwpdata, tglpenetapan, tgljatuhtempo, masaawal, masaakhir, uruttgl, jmlomzetawal, tarifpajak, denda, kenaikan, statbayar, tglbayar, jmlbayar, tglkurangbayar, jmlkurangbayar, jmlperingatan, kdflow, status, opsid, opsprov, opskota, dendaopsprov, dendaopskota, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5505 (class 0 OID 17597)
-- Dependencies: 317
-- Data for Name: transsts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transsts (idsts, idupt, setorandari, idbend, nosts, tglsts, keterangan, statbayar, ntpd, tglntpd, statsts, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5507 (class 0 OID 17606)
-- Dependencies: 319
-- Data for Name: transstsdet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transstsdet (idstsdet, idsts, idrekd, nilaists, jenis, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5509 (class 0 OID 17614)
-- Dependencies: 321
-- Data for Name: transwpdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transwpdata (idtwpdata, idnpwpd, kdflow, tgldaftar, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5511 (class 0 OID 17623)
-- Dependencies: 323
-- Data for Name: transwpdataantri; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transwpdataantri (idantri, idtwpdata, noantri, idktp, statantri, ket, tglantri, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5513 (class 0 OID 17631)
-- Dependencies: 325
-- Data for Name: transwpdatafile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transwpdatafile (idfile, idtwpdata, namafile, direktory, extension, size, url, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 5523 (class 0 OID 0)
-- Dependencies: 234
-- Name: mapjnspendapatan_idmapjnsd_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mapjnspendapatan_idmapjnsd_seq', 1, false);


--
-- TOC entry 5524 (class 0 OID 0)
-- Dependencies: 236
-- Name: masterab_idab_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterab_idab_seq', 1, false);


--
-- TOC entry 5525 (class 0 OID 0)
-- Dependencies: 238
-- Name: masterabdet_idabdet_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterabdet_idabdet_seq', 1, false);


--
-- TOC entry 5526 (class 0 OID 0)
-- Dependencies: 240
-- Name: masterbadan_idbadan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterbadan_idbadan_seq', 1, false);


--
-- TOC entry 5527 (class 0 OID 0)
-- Dependencies: 242
-- Name: masterbank_idbank_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterbank_idbank_seq', 1, false);


--
-- TOC entry 5528 (class 0 OID 0)
-- Dependencies: 245
-- Name: masterbendahara_idbend_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterbendahara_idbend_seq', 1, false);


--
-- TOC entry 5529 (class 0 OID 0)
-- Dependencies: 248
-- Name: masterhapusdenda_idhapusdenda_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterhapusdenda_idhapusdenda_seq', 1, false);


--
-- TOC entry 5530 (class 0 OID 0)
-- Dependencies: 250
-- Name: masterhistory_idhistory_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterhistory_idhistory_seq', 1, false);


--
-- TOC entry 5531 (class 0 OID 0)
-- Dependencies: 252
-- Name: masterjabttd_idjabttd_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterjabttd_idjabttd_seq', 1, false);


--
-- TOC entry 5532 (class 0 OID 0)
-- Dependencies: 254
-- Name: masterjnspendapatan_idjnsd_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterjnspendapatan_idjnsd_seq', 1, false);


--
-- TOC entry 5533 (class 0 OID 0)
-- Dependencies: 256
-- Name: masterkabkota_idkabkota_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkabkota_idkabkota_seq', 1, false);


--
-- TOC entry 5534 (class 0 OID 0)
-- Dependencies: 258
-- Name: masterkabkotaall_idkabkotaall_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkabkotaall_idkabkotaall_seq', 1, false);


--
-- TOC entry 5535 (class 0 OID 0)
-- Dependencies: 260
-- Name: masterkaupt_idkaupt_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkaupt_idkaupt_seq', 1, false);


--
-- TOC entry 5536 (class 0 OID 0)
-- Dependencies: 328
-- Name: masterkb_idkb_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkb_idkb_seq', 1, false);


--
-- TOC entry 5537 (class 0 OID 0)
-- Dependencies: 262
-- Name: masterkbdet_idkbdet_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkbdet_idkbdet_seq', 1, false);


--
-- TOC entry 5538 (class 0 OID 0)
-- Dependencies: 264
-- Name: masterkecamatan_idkecamatan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkecamatan_idkecamatan_seq', 1, false);


--
-- TOC entry 5539 (class 0 OID 0)
-- Dependencies: 266
-- Name: masterkelurahan_idkelurahan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkelurahan_idkelurahan_seq', 1, false);


--
-- TOC entry 5540 (class 0 OID 0)
-- Dependencies: 268
-- Name: masterkiosk_idkios_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterkiosk_idkios_seq', 1, false);


--
-- TOC entry 5541 (class 0 OID 0)
-- Dependencies: 326
-- Name: masterktp_idktp_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterktp_idktp_seq', 1, false);


--
-- TOC entry 5542 (class 0 OID 0)
-- Dependencies: 270
-- Name: masterlibur_idlibur_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterlibur_idlibur_seq', 1, false);


--
-- TOC entry 5543 (class 0 OID 0)
-- Dependencies: 272
-- Name: mastermerk_idmerk_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mastermerk_idmerk_seq', 1, false);


--
-- TOC entry 5544 (class 0 OID 0)
-- Dependencies: 274
-- Name: masternpwpd_idnpwpd_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masternpwpd_idnpwpd_seq', 1, false);


--
-- TOC entry 5545 (class 0 OID 0)
-- Dependencies: 276
-- Name: masterpegawai_idpegawai_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterpegawai_idpegawai_seq', 1, false);


--
-- TOC entry 5546 (class 0 OID 0)
-- Dependencies: 278
-- Name: masterprovinsi_idprovinsi_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterprovinsi_idprovinsi_seq', 1, false);


--
-- TOC entry 5547 (class 0 OID 0)
-- Dependencies: 280
-- Name: masterrekd_idrekd_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterrekd_idrekd_seq', 1, false);


--
-- TOC entry 5548 (class 0 OID 0)
-- Dependencies: 282
-- Name: masterreknrc_idreknrc_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterreknrc_idreknrc_seq', 1, false);


--
-- TOC entry 5549 (class 0 OID 0)
-- Dependencies: 284
-- Name: masterrt_idrt_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterrt_idrt_seq', 1, false);


--
-- TOC entry 5550 (class 0 OID 0)
-- Dependencies: 286
-- Name: masterrw_idrw_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterrw_idrw_seq', 1, false);


--
-- TOC entry 5551 (class 0 OID 0)
-- Dependencies: 288
-- Name: mastertarif_idtarif_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mastertarif_idtarif_seq', 1, false);


--
-- TOC entry 5552 (class 0 OID 0)
-- Dependencies: 290
-- Name: mastertarifnjop_idtarifnjop_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mastertarifnjop_idtarifnjop_seq', 1, false);


--
-- TOC entry 5553 (class 0 OID 0)
-- Dependencies: 292
-- Name: masterteks_idteks_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterteks_idteks_seq', 1, false);


--
-- TOC entry 5554 (class 0 OID 0)
-- Dependencies: 294
-- Name: masterupt_idupt_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterupt_idupt_seq', 1, false);


--
-- TOC entry 5555 (class 0 OID 0)
-- Dependencies: 296
-- Name: masteruunjop_iduunjop_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masteruunjop_iduunjop_seq', 1, false);


--
-- TOC entry 5556 (class 0 OID 0)
-- Dependencies: 298
-- Name: masterwp_idwp_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterwp_idwp_seq', 1, false);


--
-- TOC entry 5557 (class 0 OID 0)
-- Dependencies: 300
-- Name: masterwpdata_idwpdata_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.masterwpdata_idwpdata_seq', 1, false);


--
-- TOC entry 5558 (class 0 OID 0)
-- Dependencies: 302
-- Name: transdatakohir_idkohir_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transdatakohir_idkohir_seq', 1, false);


--
-- TOC entry 5559 (class 0 OID 0)
-- Dependencies: 304
-- Name: transhistpendataan_idhistpendataan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transhistpendataan_idhistpendataan_seq', 1, false);


--
-- TOC entry 5560 (class 0 OID 0)
-- Dependencies: 306
-- Name: transhistpendataandet_idhistpendataandet_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transhistpendataandet_idhistpendataandet_seq', 1, false);


--
-- TOC entry 5561 (class 0 OID 0)
-- Dependencies: 308
-- Name: transhistpenetapan_idhistpenetapan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transhistpenetapan_idhistpenetapan_seq', 1, false);


--
-- TOC entry 5562 (class 0 OID 0)
-- Dependencies: 310
-- Name: transpendataan_idpendataan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transpendataan_idpendataan_seq', 1, false);


--
-- TOC entry 5563 (class 0 OID 0)
-- Dependencies: 312
-- Name: transpendataandet_idpendataandet_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transpendataandet_idpendataandet_seq', 1, false);


--
-- TOC entry 5564 (class 0 OID 0)
-- Dependencies: 314
-- Name: transpenetapan_idpenetapan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transpenetapan_idpenetapan_seq', 1, false);


--
-- TOC entry 5565 (class 0 OID 0)
-- Dependencies: 316
-- Name: transsts_idsts_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transsts_idsts_seq', 1, false);


--
-- TOC entry 5566 (class 0 OID 0)
-- Dependencies: 318
-- Name: transstsdet_idstsdet_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transstsdet_idstsdet_seq', 1, false);


--
-- TOC entry 5567 (class 0 OID 0)
-- Dependencies: 320
-- Name: transwpdata_idtwpdata_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transwpdata_idtwpdata_seq', 1, false);


--
-- TOC entry 5568 (class 0 OID 0)
-- Dependencies: 322
-- Name: transwpdataantri_idantri_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transwpdataantri_idantri_seq', 1, false);


--
-- TOC entry 5569 (class 0 OID 0)
-- Dependencies: 324
-- Name: transwpdatafile_idfile_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transwpdatafile_idfile_seq', 1, false);


--
-- TOC entry 5125 (class 2606 OID 17033)
-- Name: appgroupuser appgroupuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appgroupuser
    ADD CONSTRAINT appgroupuser_pkey PRIMARY KEY (kdgroup);


--
-- TOC entry 5145 (class 2606 OID 17127)
-- Name: appotor appotor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appotor
    ADD CONSTRAINT appotor_pkey PRIMARY KEY (kdgroup, roleid);


--
-- TOC entry 5127 (class 2606 OID 17049)
-- Name: approle approle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.approle
    ADD CONSTRAINT approle_pkey PRIMARY KEY (roleid);


--
-- TOC entry 5129 (class 2606 OID 17058)
-- Name: appuser appuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appuser
    ADD CONSTRAINT appuser_pkey PRIMARY KEY (userid);


--
-- TOC entry 5131 (class 2606 OID 17065)
-- Name: jnsdok jnsdok_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsdok
    ADD CONSTRAINT jnsdok_pkey PRIMARY KEY (kddok);


--
-- TOC entry 5133 (class 2606 OID 17072)
-- Name: jnsgolongan jnsgolongan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsgolongan
    ADD CONSTRAINT jnsgolongan_pkey PRIMARY KEY (jnsgolid);


--
-- TOC entry 5135 (class 2606 OID 17079)
-- Name: jnsguna jnsguna_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsguna
    ADD CONSTRAINT jnsguna_pkey PRIMARY KEY (kdguna);


--
-- TOC entry 5137 (class 2606 OID 17086)
-- Name: jnshist jnshist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnshist
    ADD CONSTRAINT jnshist_pkey PRIMARY KEY (kdhist);


--
-- TOC entry 5139 (class 2606 OID 17093)
-- Name: jnsjr jnsjr_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsjr
    ADD CONSTRAINT jnsjr_pkey PRIMARY KEY (jnsjrid);


--
-- TOC entry 5141 (class 2606 OID 17100)
-- Name: jnskatkendaraan jnskatkendaraan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnskatkendaraan
    ADD CONSTRAINT jnskatkendaraan_pkey PRIMARY KEY (katid);


--
-- TOC entry 5143 (class 2606 OID 17108)
-- Name: jnskendaraan jnskendaraan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnskendaraan
    ADD CONSTRAINT jnskendaraan_pkey PRIMARY KEY (jnskendid);


--
-- TOC entry 5147 (class 2606 OID 17134)
-- Name: jnsmilik jnsmilik_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsmilik
    ADD CONSTRAINT jnsmilik_pkey PRIMARY KEY (kdmilik);


--
-- TOC entry 5149 (class 2606 OID 17141)
-- Name: jnspajak jnspajak_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnspajak
    ADD CONSTRAINT jnspajak_pkey PRIMARY KEY (kdjnspjk);


--
-- TOC entry 5151 (class 2606 OID 17148)
-- Name: jnsplat jnsplat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsplat
    ADD CONSTRAINT jnsplat_pkey PRIMARY KEY (kdplat);


--
-- TOC entry 5153 (class 2606 OID 17155)
-- Name: jnsprogresif jnsprogresif_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsprogresif
    ADD CONSTRAINT jnsprogresif_pkey PRIMARY KEY (kdprogresif);


--
-- TOC entry 5155 (class 2606 OID 17162)
-- Name: jnsranmor jnsranmor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsranmor
    ADD CONSTRAINT jnsranmor_pkey PRIMARY KEY (kdranmor);


--
-- TOC entry 5157 (class 2606 OID 17169)
-- Name: jnsstrurek jnsstrurek_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsstrurek
    ADD CONSTRAINT jnsstrurek_pkey PRIMARY KEY (mtglevel);


--
-- TOC entry 5159 (class 2606 OID 17176)
-- Name: jnstarif jnstarif_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnstarif
    ADD CONSTRAINT jnstarif_pkey PRIMARY KEY (kdjnstarif);


--
-- TOC entry 5161 (class 2606 OID 17183)
-- Name: jnsumum jnsumum_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jnsumum
    ADD CONSTRAINT jnsumum_pkey PRIMARY KEY (kdumum);


--
-- TOC entry 5163 (class 2606 OID 17193)
-- Name: mapjnspendapatan mapjnspendapatan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mapjnspendapatan
    ADD CONSTRAINT mapjnspendapatan_pkey PRIMARY KEY (idmapjnsd);


--
-- TOC entry 5165 (class 2606 OID 17205)
-- Name: masterab masterab_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterab
    ADD CONSTRAINT masterab_pkey PRIMARY KEY (idab);


--
-- TOC entry 5167 (class 2606 OID 17213)
-- Name: masterabdet masterabdet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterabdet
    ADD CONSTRAINT masterabdet_pkey PRIMARY KEY (idabdet);


--
-- TOC entry 5169 (class 2606 OID 17224)
-- Name: masterbadan masterbadan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterbadan
    ADD CONSTRAINT masterbadan_pkey PRIMARY KEY (idbadan);


--
-- TOC entry 5171 (class 2606 OID 17232)
-- Name: masterbank masterbank_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterbank
    ADD CONSTRAINT masterbank_pkey PRIMARY KEY (idbank);


--
-- TOC entry 5173 (class 2606 OID 17239)
-- Name: masterbbm masterbbm_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterbbm
    ADD CONSTRAINT masterbbm_pkey PRIMARY KEY (kodebbm);


--
-- TOC entry 5175 (class 2606 OID 17249)
-- Name: masterbendahara masterbendahara_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterbendahara
    ADD CONSTRAINT masterbendahara_pkey PRIMARY KEY (idbend);


--
-- TOC entry 5177 (class 2606 OID 17256)
-- Name: masterflow masterflow_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterflow
    ADD CONSTRAINT masterflow_pkey PRIMARY KEY (kdflow);


--
-- TOC entry 5179 (class 2606 OID 17269)
-- Name: masterhapusdenda masterhapusdenda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterhapusdenda
    ADD CONSTRAINT masterhapusdenda_pkey PRIMARY KEY (idhapusdenda);


--
-- TOC entry 5181 (class 2606 OID 17285)
-- Name: masterhistory masterhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterhistory
    ADD CONSTRAINT masterhistory_pkey PRIMARY KEY (idhistory);


--
-- TOC entry 5183 (class 2606 OID 17293)
-- Name: masterjabttd masterjabttd_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterjabttd
    ADD CONSTRAINT masterjabttd_pkey PRIMARY KEY (idjabttd);


--
-- TOC entry 5185 (class 2606 OID 17301)
-- Name: masterjnspendapatan masterjnspendapatan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterjnspendapatan
    ADD CONSTRAINT masterjnspendapatan_pkey PRIMARY KEY (idjnsd);


--
-- TOC entry 5187 (class 2606 OID 17309)
-- Name: masterkabkota masterkabkota_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkabkota
    ADD CONSTRAINT masterkabkota_pkey PRIMARY KEY (idkabkota);


--
-- TOC entry 5189 (class 2606 OID 17317)
-- Name: masterkabkotaall masterkabkotaall_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkabkotaall
    ADD CONSTRAINT masterkabkotaall_pkey PRIMARY KEY (idkabkotaall);


--
-- TOC entry 5191 (class 2606 OID 17325)
-- Name: masterkaupt masterkaupt_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkaupt
    ADD CONSTRAINT masterkaupt_pkey PRIMARY KEY (idkaupt);


--
-- TOC entry 5259 (class 2606 OID 17674)
-- Name: masterkb masterkb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkb
    ADD CONSTRAINT masterkb_pkey PRIMARY KEY (idkb);


--
-- TOC entry 5193 (class 2606 OID 17334)
-- Name: masterkbdet masterkbdet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkbdet
    ADD CONSTRAINT masterkbdet_pkey PRIMARY KEY (idkbdet);


--
-- TOC entry 5195 (class 2606 OID 17342)
-- Name: masterkecamatan masterkecamatan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkecamatan
    ADD CONSTRAINT masterkecamatan_pkey PRIMARY KEY (idkecamatan);


--
-- TOC entry 5197 (class 2606 OID 17350)
-- Name: masterkelurahan masterkelurahan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkelurahan
    ADD CONSTRAINT masterkelurahan_pkey PRIMARY KEY (idkelurahan);


--
-- TOC entry 5199 (class 2606 OID 17358)
-- Name: masterkiosk masterkiosk_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterkiosk
    ADD CONSTRAINT masterkiosk_pkey PRIMARY KEY (idkios);


--
-- TOC entry 5257 (class 2606 OID 17662)
-- Name: masterktp masterktp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterktp
    ADD CONSTRAINT masterktp_pkey PRIMARY KEY (idktp);


--
-- TOC entry 5201 (class 2606 OID 17367)
-- Name: masterlibur masterlibur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterlibur
    ADD CONSTRAINT masterlibur_pkey PRIMARY KEY (idlibur);


--
-- TOC entry 5203 (class 2606 OID 17375)
-- Name: mastermerk mastermerk_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mastermerk
    ADD CONSTRAINT mastermerk_pkey PRIMARY KEY (idmerk);


--
-- TOC entry 5205 (class 2606 OID 17385)
-- Name: masternpwpd masternpwpd_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masternpwpd
    ADD CONSTRAINT masternpwpd_pkey PRIMARY KEY (idnpwpd);


--
-- TOC entry 5207 (class 2606 OID 17393)
-- Name: masterpegawai masterpegawai_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterpegawai
    ADD CONSTRAINT masterpegawai_pkey PRIMARY KEY (idpegawai);


--
-- TOC entry 5209 (class 2606 OID 17401)
-- Name: masterprovinsi masterprovinsi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterprovinsi
    ADD CONSTRAINT masterprovinsi_pkey PRIMARY KEY (idprovinsi);


--
-- TOC entry 5211 (class 2606 OID 17409)
-- Name: masterrekd masterrekd_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterrekd
    ADD CONSTRAINT masterrekd_pkey PRIMARY KEY (idrekd);


--
-- TOC entry 5213 (class 2606 OID 17420)
-- Name: masterreknrc masterreknrc_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterreknrc
    ADD CONSTRAINT masterreknrc_pkey PRIMARY KEY (idreknrc);


--
-- TOC entry 5215 (class 2606 OID 17428)
-- Name: masterrt masterrt_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterrt
    ADD CONSTRAINT masterrt_pkey PRIMARY KEY (idrt);


--
-- TOC entry 5217 (class 2606 OID 17436)
-- Name: masterrw masterrw_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterrw
    ADD CONSTRAINT masterrw_pkey PRIMARY KEY (idrw);


--
-- TOC entry 5219 (class 2606 OID 17446)
-- Name: mastertarif mastertarif_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mastertarif
    ADD CONSTRAINT mastertarif_pkey PRIMARY KEY (idtarif);


--
-- TOC entry 5221 (class 2606 OID 17454)
-- Name: mastertarifnjop mastertarifnjop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mastertarifnjop
    ADD CONSTRAINT mastertarifnjop_pkey PRIMARY KEY (idtarifnjop);


--
-- TOC entry 5223 (class 2606 OID 17474)
-- Name: masterteks masterteks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterteks
    ADD CONSTRAINT masterteks_pkey PRIMARY KEY (idteks);


--
-- TOC entry 5225 (class 2606 OID 17484)
-- Name: masterupt masterupt_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterupt
    ADD CONSTRAINT masterupt_pkey PRIMARY KEY (idupt);


--
-- TOC entry 5227 (class 2606 OID 17494)
-- Name: masteruunjop masteruunjop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masteruunjop
    ADD CONSTRAINT masteruunjop_pkey PRIMARY KEY (iduunjop);


--
-- TOC entry 5229 (class 2606 OID 17508)
-- Name: masterwp masterwp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterwp
    ADD CONSTRAINT masterwp_pkey PRIMARY KEY (idwp);


--
-- TOC entry 5231 (class 2606 OID 17519)
-- Name: masterwpdata masterwpdata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.masterwpdata
    ADD CONSTRAINT masterwpdata_pkey PRIMARY KEY (idwpdata);


--
-- TOC entry 5233 (class 2606 OID 17532)
-- Name: transdatakohir transdatakohir_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transdatakohir
    ADD CONSTRAINT transdatakohir_pkey PRIMARY KEY (idkohir);


--
-- TOC entry 5235 (class 2606 OID 17543)
-- Name: transhistpendataan transhistpendataan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transhistpendataan
    ADD CONSTRAINT transhistpendataan_pkey PRIMARY KEY (idhistpendataan);


--
-- TOC entry 5237 (class 2606 OID 17551)
-- Name: transhistpendataandet transhistpendataandet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transhistpendataandet
    ADD CONSTRAINT transhistpendataandet_pkey PRIMARY KEY (idhistpendataandet);


--
-- TOC entry 5239 (class 2606 OID 17563)
-- Name: transhistpenetapan transhistpenetapan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transhistpenetapan
    ADD CONSTRAINT transhistpenetapan_pkey PRIMARY KEY (idhistpenetapan);


--
-- TOC entry 5241 (class 2606 OID 17575)
-- Name: transpendataan transpendataan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transpendataan
    ADD CONSTRAINT transpendataan_pkey PRIMARY KEY (idpendataan);


--
-- TOC entry 5243 (class 2606 OID 17583)
-- Name: transpendataandet transpendataandet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transpendataandet
    ADD CONSTRAINT transpendataandet_pkey PRIMARY KEY (idpendataandet);


--
-- TOC entry 5245 (class 2606 OID 17595)
-- Name: transpenetapan transpenetapan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transpenetapan
    ADD CONSTRAINT transpenetapan_pkey PRIMARY KEY (idpenetapan);


--
-- TOC entry 5247 (class 2606 OID 17604)
-- Name: transsts transsts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transsts
    ADD CONSTRAINT transsts_pkey PRIMARY KEY (idsts);


--
-- TOC entry 5249 (class 2606 OID 17612)
-- Name: transstsdet transstsdet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transstsdet
    ADD CONSTRAINT transstsdet_pkey PRIMARY KEY (idstsdet);


--
-- TOC entry 5251 (class 2606 OID 17621)
-- Name: transwpdata transwpdata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transwpdata
    ADD CONSTRAINT transwpdata_pkey PRIMARY KEY (idtwpdata);


--
-- TOC entry 5253 (class 2606 OID 17629)
-- Name: transwpdataantri transwpdataantri_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transwpdataantri
    ADD CONSTRAINT transwpdataantri_pkey PRIMARY KEY (idantri);


--
-- TOC entry 5255 (class 2606 OID 17639)
-- Name: transwpdatafile transwpdatafile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transwpdatafile
    ADD CONSTRAINT transwpdatafile_pkey PRIMARY KEY (idfile);


-- Completed on 2025-12-29 16:01:44

--
-- PostgreSQL database dump complete
--

\unrestrict LlbYeqUyb5PJzWHLpVTCvgjHKizzku4y7deDfAa4J7OGZDgW8lcE8HZXIh0CXGb
