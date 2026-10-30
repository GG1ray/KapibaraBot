import os
import random
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Yeni bir seviye komutu eklemek için buraya bir satır eklemen yeterli.
# {adin} -> komutu yazan kişinin eki almış adı (Ayşe'nin), {yuzde} -> 0-100 arası rastgele sayı
SEVIYELER = {
    "tsundere": "{adin} tsundere seviyesi şu anda: %{yuzde} 😡❤️‍🔥",
    "yandere": "{adin} yandere seviyesi şu anda: %{yuzde} 🔪",
    "yalan": "{adin} yalancı seviyesi şu anda: %{yuzde} 🤫",
    "kapibara": "{adin} kapibara seviyesi şu anda: %{yuzde} 😌",
}

# Büyük harfler ayrıca yazıldı çünkü Python'da "I".lower() "i" verir, Türkçede yanlış olur.
UNLU_EKLERI = {
    "a": "ın", "ı": "ın", "A": "ın", "I": "ın",
    "e": "in", "i": "in", "E": "in", "İ": "in",
    "o": "un", "u": "un", "O": "un", "U": "un",
    "ö": "ün", "ü": "ün", "Ö": "ün", "Ü": "ün",
}

YARDIM_METNI = "Komutlar:\n" + "\n".join(f"`!{isim}`" for isim in SEVIYELER)

intents = discord.Intents.default()
intents.message_content = True  # !komutları okuyabilmek için gerekli

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None,  # yardım !help yerine sadece yazana görünen /help ile veriliyor
    allowed_mentions=discord.AllowedMentions.none(),  # takma addaki @everyone kimseyi etiketlemesin
)


def iyelik_eki(ad: str) -> str:
    harfler = [harf for harf in ad if harf.isalpha()]
    unluler = [harf for harf in harfler if harf in UNLU_EKLERI]
    if not unluler:
        return f"{ad}'nin"
    ek = UNLU_EKLERI[unluler[-1]]
    if harfler[-1] in UNLU_EKLERI:
        ek = "n" + ek
    return f"{ad}'{ek}"


def seviye_komutu_ekle(isim: str, sablon: str) -> None:
    @bot.command(name=isim)
    async def komut(ctx: commands.Context) -> None:
        yuzde = random.randint(0, 100)
        await ctx.send(sablon.format(adin=iyelik_eki(ctx.author.display_name), yuzde=yuzde))


for isim, sablon in SEVIYELER.items():
    seviye_komutu_ekle(isim, sablon)


@bot.tree.command(name="help", description="Komutları sadece sana gösterir")
async def yardim(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(YARDIM_METNI, ephemeral=True)


@bot.event
async def setup_hook() -> None:
    await bot.tree.sync()


@bot.event
async def on_ready() -> None:
    print(f"Giriş yapıldı: {bot.user}")


@bot.event
async def on_command_error(ctx: commands.Context, hata: commands.CommandError) -> None:
    if isinstance(hata, commands.CommandNotFound):
        return
    raise hata


if __name__ == "__main__":
    if not TOKEN:
        sys.exit("DISCORD_TOKEN eksik! .env dosyasına bot token'ını yaz (örnek: .env.example).")
    bot.run(TOKEN)
