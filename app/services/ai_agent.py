def analyze_user_request(message: str) -> str:
    """
    Kullanıcının yazdığı metni analiz eder
    ve ihtiyaç türünü belirler.
    (Şimdilik basit, yakında pydantic-ai)
    """

    text = message.lower()

    if "web" in text:
        return "User needs a website"
    if "mobil" in text or "mobile" in text:
        return "User needs a mobile application"
    if "e-ticaret" in text or "shop" in text:
        return "User needs an e-commerce solution"

    return "Need more information"
