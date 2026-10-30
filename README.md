# KapibaraBot

Komutlar: `!tsundere`, `!yandere`, `!yalan`, `!kapibara`, `!uyku` — yazan kişinin adını ve rastgele bir yüzde verir. `/help` komut listesini sadece yazan kişiye gösterir.

## Kurulum

### 1. Discord tarafı
1. https://discord.com/developers/applications → **New Application** → bir isim ver.
2. Soldan **Bot** sekmesi → **Reset Token** → token'ı kopyala.
3. Aynı sayfada **Privileged Gateway Intents** altında **Message Content Intent**'i aç ve kaydet (açmazsan bot `!komut`ları göremez).
4. **OAuth2 → URL Generator**: Scopes'ta `bot` ve `applications.commands`, Bot Permissions'ta `Send Messages` ve `Read Message History` seç. Alttaki linki aç ve botu sunucuna ekle. Bot zaten sunucundaysa ve `/help` görünmüyorsa aynı linkle yeniden davet et.

### 2. Bilgisayar tarafı
`.env.example` dosyasını `.env` olarak kopyala ve token'ını yapıştır:

```
DISCORD_TOKEN=senin_tokenin
```

Sonra:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python bot.py
```

Konsolda `Giriş yapıldı: ...` görünce sunucuda `!kapibara` yazıp dene.

> Token'ı kimseyle paylaşma; `.env` dosyası `.gitignore`'da.

## Yeni komut eklemek
`bot.py` içindeki `SEVIYELER` sözlüğüne bir satır ekle:

```python
"kedi": "{adin} kedi seviyesi şu anda: %{yuzde} 🐱",
```
