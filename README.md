Nexivion Backend 🚀

Bu proje, Nexivion web sitesi ve ileride diğer projeler (mobil / AI servisleri) için
FastAPI tabanlı backend altyapısı oluşturmak amacıyla başlatılmıştır.

Amaç:

Temiz backend mimarisi öğrenmek

Schema (Pydantic) mantığını sindirmek

İleride AI (Pydantic AI), ödeme ve gerçek veritabanı eklemeye hazır olmak

🧱 Kullanılan Teknolojiler

Python 3.9+

FastAPI

Pydantic

Uvicorn

Git / GitHub

📂 Proje Yapısı (Şu An)
nexivion-backend/
│
├── main.py              # Ana FastAPI uygulaması
├── schemas/             # Pydantic schema'lar
│   ├── __init__.py
│   └── user.py          # User schema
│
├── venv/                # Virtual environment (git'e dahil değil)
├── .gitignore
└── README.md

▶️ Uygulamayı Çalıştırma
# Virtual env aktifken
uvicorn main:app --reload


Tarayıcıdan:

Ana endpoint:
👉 http://127.0.0.1:8000

Swagger (dokümantasyon):
👉 http://127.0.0.1:8000/docs

🔗 Mevcut Endpoint’ler
GET /users

Tüm kullanıcıları listeler.

Örnek çıktı:

[
  { "id": 1, "name": "Ali" },
  { "id": 2, "name": "Veli" }
]

POST /users

Yeni kullanıcı ekler.

Body (Swagger veya Postman’dan):

{
  "id": 3,
  "name": "Ayşe"
}

🧠 Öğrenilenler (Şu Ana Kadar)

FastAPI nasıl ayağa kaldırılır

Endpoint nedir

GET / POST farkı

Pydantic schema neden kullanılır

Swagger (/docs) nasıl kullanılır

Fake DB mantığı (liste ile çalışma)

Git commit & push

🛣️ Sonraki Adımlar (Yarın / Sonra)

APIRouter kullanımı

Router’ları dosyalara ayırma

Gerçek veritabanı (SQLite / PostgreSQL)

AI (Pydantic AI) entegrasyonu

Ödeme altyapısı (ileride)

🤍 Not

Bu proje öğrenme odaklıdır.
Adım adım, sindire sindire ilerlenmektedir.
