import requests, json, os, datetime

API_KEY = os.getenv('SPORTS_DB_KEY')   # set di GitHub Secrets
URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/livescore.php?s=Basketball"

def main():
    resp = requests.get(URL, timeout=10)
    data = resp.json()
    # Simpan hanya info yang diperlukan
    out = {
        "last_update": datetime.datetime.utcnow().isoformat() + "Z",
        "events": data.get("events", [])
    }
    with open("scripts/scores.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

if __name__ == "__main__":
    main()
