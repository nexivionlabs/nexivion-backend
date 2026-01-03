🚀 Nexivion Backend

🇹🇷 Türkçe | 🇬🇧 English

- AI-First Backend Mimarisi / AI-First Backend Architecture

🎯 Vision | 🎯 Vizyon

🇹🇷
Nexivion Backend’in vizyonu, kullanıcı girdilerini değil kullanıcı niyetini anlamak ve bu niyete göre AI destekli kararlar üretmektir.

🇬🇧
The vision of Nexivion Backend is to understand user intent, not just input, and produce AI-assisted decisions accordingly.

Bu repository:

- ❌ Sadece CRUD yapan bir demo değildir

- ✅ Mimari düşünceyi merkeze alan bir sistem altyapısıdır


🧠 Architectural Approach (AI-First) | 🧠 Mimari Yaklaşım (AI-First)

![CleanArchitecture](https://github.com/user-attachments/assets/d27b25d6-126d-4e48-bd1b-8275f0ffe973)

```bash
flowchart TB
    Client --> API[FastAPI Router]
    API --> Schemas[Pydantic Şemalar]
    Schemas --> Services[İş Mantığı & AI]
    Services --> Decision[AI Karar Katmanı]
    Decision --> API
    API --> Client
```

🇹🇷
Nexivion Backend, katmanlı ve AI-first bir mimari izler.
API yalnızca HTTP iletişiminden sorumludur; iş mantığı ve AI kararları servis katmanında izole edilmiştir.

- API katmanı yalnızca HTTP iletişiminden sorumludur

- Veri doğrulama ve sözleşmeler Pydantic şemalar ile sağlanır

- İş kuralları ve AI mantığı services katmanında izole edilmiştir

- AI karar katmanı değiştirilebilir ve genişletilebilir yapıdadır

Bu yaklaşım:

- Sürdürülebilirlik

- Test edilebilirlik

- Ölçeklenebilirlik
  
sağlar.


🇬🇧
Nexivion Backend follows a layered, AI-first architecture.
The API layer handles only HTTP communication, while business logic and AI decisions are isolated in the service layer.
Nexivion Backend katmanlı ve AI-first bir mimari izler:



🧩 Katmanlı Mimari | 🧩 Layered Architecture

```bash
graph LR
    Presentation["Sunum Katmanı<br/>FastAPI (api/)"]
    Application["Uygulama Katmanı<br/>AI & İş Mantığı (services/)"]
    Domain["Domain Katmanı<br/>Şemalar (schemas/)"]
    Infrastructure["Altyapı<br/>DB & Harici Servisler"]

    Presentation --> Application
    Application --> Domain
    Application --> Infrastructure
```


🇹🇷 Katman Sorumlulukları

Presentation: Request / response

Schemas: Veri doğrulama ve sözleşmeler

Services: İş kuralları ve AI karar mantığı

- Sunum Katmanı (api/)
Request / response yönetir.
İş mantığı içermez.

- Şemalar (schemas/)
Veri yapıları ve sözleşmeler.

- Servisler (services/)
İş kuralları, AI karar mantığı, niyet analizi.
pydantic-ai entegrasyonuna hazırdır.

- Main (main.py)
Router’ları birleştiren uygulama orkestratörü.

🇬🇧 Layer Responsibilities

Presentation: Request / response handling

Schemas: Data validation & contracts

Services: Business rules & AI decision logic


🔁 İstek → AI Karar Akışı | 🔁 Request → AI Decision Flow

🔁 İstek → AI Karar Akışı

```bash
sequenceDiagram
    participant Kullanıcı
    participant API as FastAPI Router
    participant Schema as Pydantic Şema
    participant Service as AI Servisi
    participant Decision as AI Karar Katmanı

    Kullanıcı->>API: HTTP İsteği
    API->>Schema: Veri Doğrulama
    Schema->>Service: Temiz Veri
    Service->>Decision: Niyet Analizi
    Decision-->>Service: Karar
    Service-->>API: Yapılandırılmış Cevap
    API-->>Kullanıcı: JSON Response
```

📂 Proje Yapısı | 📂 Project Structure 

```bash
app/
├── api/
│   └── v1/
│       └── users.py
├── schemas/
│   └── user.py
├── services/
│   ├── ai_agent.py
│   └── config.py
├── main.py
```

🤖 AI Karar Katmanı | 🤖 AI Decision Layer

🇹🇷
AI karar mantığı bilinçli olarak API’den ayrılmıştır.
Bu sayede sistem kural tabanlıdan tam agent mimarisine evrilebilir.

AI karar mantığı bilinçli olarak services/ katmanında izole edilmiştir.

- API içinde AI logic yoktur

- HTTP ile AI birbirine bağlı değildir

Sistem şu şekilde evrilebilir:

- Kural tabanlı sistem

  → AI destekli kararlar

  → Tam agent mimarisi

Bu yapı Nexivion’u geleceğe hazır kılar.

🇬🇧
The AI decision logic is intentionally decoupled from the API.
This allows the system to evolve from rule-based logic to full agent architectures.



📄 Yönetici Özeti (Founder / Recruiter için) | 📄 Executive Summary


🇹🇷
Bu proje, özellik sayısından çok mimari olgunluğu gösterir.

Bu proje:

- Katmanlı sistem tasarımını

- AI-first düşünceyi

- Gerçek ürün altyapısı yaklaşımını

- Ölçeklenebilir backend vizyonunu

ortaya koyar.

Bu bir “endpoint koleksiyonu” değil, bir sistem tasarımıdır.

🇬🇧
This project demonstrates architectural maturity, not feature quantity.





🛠️ Teknoloji Yığını | 🛠️ Tech Stack

🇹🇷
- FastAPI – Yüksek performanslı API framework

- Pydantic – Veri doğrulama ve sözleşmeler

- Python – Temiz ve okunabilir backend dili

- AI-Ready Mimari – pydantic-ai entegrasyonuna hazırlık eklenecektir!


🇬🇧
- FastAPI

- Pydantic

- Python

- AI-ready architecture (pydantic-ai compatible)

▶️ Çalıştırma | ▶️ Run

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

API Dokümantasyonu:
👉 http://127.0.0.1:8000/docs

✍️ Yazar | ✍️ Author

Fatih
Full Stack & AI-Oriented Software Developer

| “I don’t just write code — I design systems.”

📌 Son Not | 📌 Final Note

🇹🇷
Bu proje bitmiş bir ürün değil, bilinçli olarak tasarlanmış bir temeldir.

Zamanla:

- Yeni domain’ler

- Daha gelişmiş AI kararları

- Gerçek dünya entegrasyonları

eklenmek üzere hazırlanmıştır.

Nexivion Backend, akıllı sistemlerin başlangıç noktasıdır.

🇬🇧
Nexivion Backend is where intelligent systems begin.
