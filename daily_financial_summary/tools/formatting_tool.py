import requests

def formatting_tool(summary, search_results=None):
    """
    Insert placeholders [CHART1] [CHART2] and return with dummy chart URLs.
    You can enhance this to scrape real charts from finance APIs.
    """
    if "[CHART1]" not in summary:
        summary = "[CHART1]\n\n" + summary + "\n\n[CHART2]"

    charts = [
        "https://placeholder.pics/svg/600x300?text=S&P500",
        "https://placeholder.pics/svg/600x300?text=NASDAQ"
    ]
    return {"summary": summary, "charts": charts}