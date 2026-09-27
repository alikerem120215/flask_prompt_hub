# 💡 Flask Prompt Hub — Yapay Zeka Prompt Kütüphanesi & Yönetim Paneli

Büyük Dil Modelleri (ChatGPT, Claude, Gemini) için hazırlanan sistem yönergelerini, şablonları ve prompt metinlerini tek bir merkezi yerde etiketleyip saklamanızı sağlayan Flask tabanlı web yönetim paneli.

---

## 🌟 Özellikler
- **Prompt Ekleme & Düzenleme:** Başlık, içerik ve kategori etiketi (`tag`) ile kolayca yeni prompt kaydetme.
- **Etiket Filtreleme:** Kayıtlı promptları kategorilerine göre (Kodlama, Yazarlık, Analiz vb.) tek tıkla filtreleme.
- **SQLite & SQLAlchemy:** Verileri `instance/prompts.db` dosyasında yerel olarak güvenle saklar.
- **Temiz Kullanıcı Arayüzü:** Minimalist ve göz yormayan modern tasarım.

---

## 🚀 Başlarken

```bash
pip install Flask Flask-SQLAlchemy
python3 app.py
```
Tarayıcınızda `http://127.0.0.1:5000` adresini açın.
