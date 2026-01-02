# Nexivion Backend 🚀

Bu proje, **Nexivion** için geliştirilen FastAPI tabanlı backend altyapısıdır.  
Amaç; ileride AI (Pydantic AI), ödeme sistemleri ve farklı projelerde tekrar
kullanılabilecek sağlam bir backend temelini oluşturmaktır.

---

## 🧱 Kullanılan Teknolojiler

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn
- Git & GitHub

---

## 📁 Proje Yapısı

nexivion-backend/
│
├── main.py # Ana FastAPI uygulaması
├── schemas/ # Pydantic schema'lar
│ ├── init.py
│ └── user.py # User schema
│
├── venv/ # Virtual environment (git'e girmez)
├── .gitignore
└── README.md


---

## ▶️ Uygulamayı Çalıştırma

### 1️⃣ Virtual environment aktif et
```bash
source venv/bin/activate
```

## 2️⃣ Server’ı başlat
```bash
icorn main:app --reload
```
Tarayıcıdan:

- http://127.0.0.1:8000

- http://127.0.0.1:8000/docs

## 🔗 Endpoint’ler

🔹 GET /

Sağlık kontrolü

Response:
```bash
{
  "status": "ok"
}

```

## 🔹 GET /users

Kayıtlı kullanıcıları listeler

Response:

```bash
[ "id": 1, "name": "Ali" },
  { "id": 2, "name": "Veli" }
]
```

## 🧠 Öğrenilenler (Notlar)

FastAPI endpoint mantığı

Pydantic schema kullanımı

GET / POST farkı

Swagger (/docs) ile test

Git commit & push workflow

## 🚀 Gelecek Planları

APIRouter yapısına geçiş

AI (Pydantic AI) entegrasyonu

Ödeme sistemi (Stripe / Iyzico)

Database (PostgreSQL)

Auth (JWT)

## 🤲 Not

Bu repo öğrenme ve gelişme amaçlıdır.
Adım adım ilerlenmiştir, sade tutulmuştur.

Elhamdulillah 🌿

