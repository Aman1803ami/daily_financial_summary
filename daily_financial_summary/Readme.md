
📈 CrewAI Daily US Market Summary

This project implements a CrewAI pipeline that generates a daily US financial markets summary after market close.
It uses multiple agents (employees) to search news, summarize, add charts, translate into multiple languages, and send the report to a Telegram channel.


---

🚀 Features

Search Agent → fetches latest US market/finance news (Serper/Tavily API)

Summary Agent → uses litellm (local Gemini) to produce a <500 word summary

Formatting Agent → inserts [CHART1] and [CHART2] placeholders, attaches charts/images

Translation Agent → translates into Arabic, Hindi, and Hebrew

Send Agent → posts summary + charts to Telegram channel



---




---

⚙ Setup

1. Clone repo & install dependencies

git clone https://github.com/Aman1803ami/crewai-daily-summary.git
cd crewai-daily-summary
pip install -r requirements.txt

2. Start litellm locally with Gemini

pip install litellm
litellm --model gemini-pro --port 4000

Now litellm is running at http://localhost:4000.

3. Configure environment variables

Create a .env file (or export in your shell):

SEARCH_API_KEY=your_serper_or_tavily_key
SEARCH_API_ENDPOINT=https://api.serper.dev/search
LITELLM_MODEL=gemini-pro
LITELLM_API_KEY=not_needed_for_local   # only if running locally
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=@your_channel_or_chat_id


---

▶ Run the pipeline

python run.py

You should see logs showing:

News fetched

Summary generated

Images chosen

Translations created

Message + charts sent to Telegram



---

📊 Example Output

Telegram channel post will look like:

📈 Daily US Market Summary — 2025-08-28

Stocks slipped as Fed minutes reinforced higher-for-longer rates.
S&P 500 -0.6%, Nasdaq -1.2%. Energy stocks rose on oil gains.

[CHART1]

Tech earnings dragged Nasdaq, while banks stayed flat.
Treasury yields edged higher ahead of inflation data.

[CHART2]

Sources:
- Bloomberg
- Reuters
- WSJ

And two charts will be attached under the message.


---

🛡 Guardrails

Each agent has one responsibility (search, summarize, format, translate, send).

Retries and error logging included for API calls.

Summaries capped to 500 words.

Charts inserted only where appropriate ([CHART1], [CHART2]).



---

🌍 Translations

The summary is automatically translated into:

Arabic

Hindi

Hebrew


These are preserved with formatting and shared alongside the English version.


---






