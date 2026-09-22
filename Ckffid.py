import json
import time
import requests
from pathlib import Path

# ============ কনফিগারেশন ============
ACCOUNT_JSON = "account.json"
UID_PASS_TXT = "RIFAT.UID-PASS.txt"
OUTPUT_ACTIVE = "active_accounts.txt"
OUTPUT_DEAD = "dead_accounts.txt"
OUTPUT_ERROR = "error_accounts.txt"

# Garena-র অফিসিয়াল ban check API
BAN_CHECK_URL = "https://ff.garena.com/api/antihack/check_banned"

REQUEST_TIMEOUT = 15
DELAY_BETWEEN = 2.5  # API rate limit এড়াতে ২.৫ সেকেন্ড

# =====================================


def load_accounts_from_json(path):
    """account.json থেকে ডেটা লোড"""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    accounts = []
    for item in data:
        accounts.append({
            "uid": str(item.get("uid")),
            "password": item.get("password", ""),
            "name": item.get("name", ""),
            "region": item.get("region", "BD"),
            "account_id": item.get("account_id", ""),
        })
    return accounts


def load_accounts_from_txt(path):
    """RIFAT.UID-PASS.txt থেকে uid:password লোড"""
    accounts = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        uid, password = line.split(":", 1)
        accounts.append({
            "uid": uid.strip(),
            "password": password.strip(),
            "region": "BD",
        })
    return accounts


def check_ban_status(uid):
    """
    Garena-র অফিসিয়াল anti-hack API দিয়ে ban status চেক করে।
    রিটার্ন: (is_banned, ban_period, nickname, message)
    """
    try:
        params = {"uid": str(uid)}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
        }
        r = requests.get(
            BAN_CHECK_URL,
            params=params,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
        if r.status_code == 200:
            j = r.json()
            data = j.get("data", {})
            is_banned = data.get("is_banned", 0)
            ban_period = data.get("ban_period", 0)
            nickname = data.get("nickname", "")
            server = data.get("server", "")

            if is_banned == 1:
                return True, ban_period, nickname, f"BANNED for {ban_period} year(s) | Server: {server}"
            else:
                return False, 0, nickname, f"NOT BANNED | Server: {server}"
        else:
            return None, 0, "", f"HTTP {r.status_code}"
    except Exception as e:
        return None, 0, "", f"Error: {type(e).__name__}"


def main():
    # অ্যাকাউন্ট লোড (JSON অগ্রাধিকার)
    accounts = load_accounts_from_json(ACCOUNT_JSON)
    if not accounts:
        accounts = load_accounts_from_txt(UID_PASS_TXT)

    if not accounts:
        print("❌ কোনো অ্যাকাউন্ট পাওয়া যায়নি!")
        return

    print(f"[+] মোট {len(accounts)} টি অ্যাকাউন্ট চেক করা হবে")
    print(f"[+] API: {BAN_CHECK_URL}\n")

    active = []
    dead = []
    errors = []

    for i, acc in enumerate(accounts, 1):
        uid = acc["uid"]
        password = acc["password"]

        is_banned, ban_period, nickname, msg = check_ban_status(uid)

        if is_banned is False:
            status = "✅ ACTIVE"
            active.append(f"{uid}:{password}")
        elif is_banned is True:
            status = "🚫 BANNED"
            dead.append(f"{uid}:{password}")
        else:
            status = "⚠️  ERROR"
            errors.append(f"{uid}:{password}")

        print(f"[{i}/{len(accounts)}] {status}  UID: {uid}")
        print(f"           └─ {msg}\n")

        time.sleep(DELAY_BETWEEN)

    # রেজাল্ট সেভ
    Path(OUTPUT_ACTIVE).write_text("\n".join(active), encoding="utf-8")
    Path(OUTPUT_DEAD).write_text("\n".join(dead), encoding="utf-8")
    Path(OUTPUT_ERROR).write_text("\n".join(errors), encoding="utf-8")

    print("=" * 40)
    print("📊 সামারি")
    print("=" * 40)
    print(f"✅ Active : {len(active)}")
    print(f"❌ Dead/Banned : {len(dead)}")
    print(f"⚠️  Error : {len(errors)}")
    print(f"\n📁 সেভ হয়েছে:")
    print(f"   - {OUTPUT_ACTIVE}")
    print(f"   - {OUTPUT_DEAD}")
    print(f"   - {OUTPUT_ERROR}")


if __name__ == "__main__":
    main()
