import os, requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def telegram_tool(summary, translations=None, charts=None):
    base_url = f"https://api.telegram.org/bot{BOT_TOKEN}"
    text = f"<b>US Daily Market Summary</b>\n\n{summary}"

    # Send text
    r = requests.post(f"{base_url}/sendMessage", json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    r.raise_for_status()

    # Send charts
    if charts:
        for c in charts:
            requests.post(f"{base_url}/sendPhoto", json={"chat_id": CHAT_ID, "photo": c})

    return {"ok": True}