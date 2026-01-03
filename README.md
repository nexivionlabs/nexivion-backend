# Nexivion Backend 🚀

Nexivion Backend, müşteri ihtiyaçlarını anlayan, analiz eden ve doğru hizmete yönlendiren
**AI destekli bir karar motoru** üzerine inşa edilmiş modern bir FastAPI backend’idir.

Bu proje yalnızca CRUD yapan bir API değil;  
**iş mantığı, karar verme ve yapay zekâ entegrasyonuna hazır bir mimari** sunar.

---

## 🎯 Projenin Amacı

- Kullanıcıdan gelen metinsel talepleri almak
- Bu talepleri anlamlandırmak
- AI destekli kararlar üretmek
- Müşteriyi doğru Nexivion hizmetine yönlendirmek

---

## 🧠 Mimari Yaklaşım

Nexivion Backend **katmanlı + AI-first mimari** ile tasarlanmıştır.

### 1️⃣ Katmanlı Mimari (Layered Architecture)


┌──────────────────────────┐
│ Presentation │
│ FastAPI Routers (API) │
│ app/api/ │
└────────────▲─────────────┘
│
┌────────────┴─────────────┐
│ Application │
│ AI & Business Logic │
│ app/services/ │
└────────────▲─────────────┘
│
┌────────────┴─────────────┐
│ Domain │
│ Schemas & Contracts │
│ app/schemas/ │
└────────────▲─────────────┘
│
┌────────────┴─────────────┐
│ Infrastructure │
│ DB, External APIs │
│ (future integrations) │
└──────────────────────────┘

### Katmanların Sorumlulukları

- **API (`api/`)**  
  Sadece request / response yönetir.

- **Schemas (`schemas/`)**  
  Veri yapıları ve sözleşmeler.

- **Services (`services/`)**  
  İş kuralları ve AI karar mantığı  
  (pydantic-ai entegrasyonuna hazır).

- **Main (`main.py`)**  
  Router’ları birleştiren orchestrator.

---

## ⚙️ Kurulum

### 1️⃣ Ortamı hazırla

```bash
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Bağımlılıkları yükle

```bash
pip install fastapi uvicorn
```

Not: İleride: pydantic-ai, model sağlayıcıları ve ek servisler eklenecektir.

### ▶️ Uygulamayı Çalıştır

```bash
uvicorn app.main:app --reload
```

Tarayıcıdan erişim:

API Docs (Swagger):
http://127.0.0.1:8000/docs

🔍 Örnek Kullanım
POST /users

Request

```bash
{
  "message": "Web sitesi yaptırmak istiyorum"
}
```
Response

```bash
{
  "decision": "User needs a website","suggested_service": "Web Development"


}
```

🧩 Yapay Zekâ Katmanı

AI karar mantığı şu dosyada izole edilmiştir:

```bash
app/services/ai_agent.py
```

### Bu yapı sayesinde:

- API katmanı AI detaylarını bilmez

- Farklı AI modelleri kolayca entegre edilebilir

- İş mantığı test edilebilir ve sürdürülebilirdir

### 🛣️ Yol Haritası

- pydantic-ai entegrasyonu

- Structured AI outputs (enum / model)

- Servis & paket öneri motoru

- Veritabanı entegrasyonu

- Authentication & kullanıcı akışları

### 🤝 Katkı

Bu proje, öğrenerek inşa etme yaklaşımıyla geliştirilmektedir.
Katkılar ve öneriler memnuniyetle karşılanır.

📜 Lisans

Bu proje Nexivion Labs çatısı altında geliştirilmektedir.
