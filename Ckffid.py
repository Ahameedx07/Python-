import json
import time
import requests
from pathlib import Path
from freefire_api import FreeFireClient
from freefire_api.exceptions import FreeFireAPIError, InvalidParameterError

# ============ কনফিগারেশন ============
ACCOUNT_JSON = "account.json"
UID_PASS_TXT = "RIFAT.UID-PASS.txt"
OUTPUT_ACTIVE = "active_accounts.txt"
OUTPUT_DEAD = "dead_accounts.txt"
OUTPUT_ERROR = "error_accounts.txt"

# আপনার অ্যাকাউন্টগুলো BD রিজিয়নের
REGION = "BD"

# Garena-র অফিসিয়াল ban check API
BAN_CHECK_URL = "https://ff.garena.com/api/antihack/check_banned"

REQUEST_TIMEOUT = 15
DELAY_BETWEEN = 2.0  # রেট লিমিট এড়াতে ২ সেকেন্ড বিরতি

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
            "region": item.get("region", REGION),
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
            "region": REGION,
        })
    return accounts


def check_ban_status(uid):
    """
    Garena-র অফিসিয়াল anti-hack API দিয়ে ban status চেক করে।
    রিটার্ন: (is_banned, ban_period, message)
    """
    try:
        params = {"uid": uid}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
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
            # Garena-র রেসপন্স স্ট্রাকচার
            data = j.get("data", {})
            is_banned = data.get("is_banned", 0)
            ban_period = data.get("ban_period", 0)
            nickname = data.get("nickname", "")
            
            if is_banned == 1:
                return True, ban_period, f"Banned for {ban_period} year(s)"
            else:
                return False, 0, f"Not banned | Nick: {nickname}"
        else:
            return None, 0, f"HTTP {r.status_code}"
    except Exception as e:
        return None, 0, f"Error: {type(e).__name__}"


def check_profile_exists(client, uid):
    """
    freefire-api দিয়ে প্রোফাইল চেক করে অ্যাকাউন্ট বিদ্যমান কিনা।
    """
    try:
        profile = client.get_player_profile(uid)
        if profile and profile.get("basicinfo"):
            basic = profile.get("basicinfo", {})
            nickname = basic.get("nickname", "N/A")
            level = basic.get("level", "N/A")
            region = basic.get("region", "N/A")
            return True, f"Nick: {nickname} | Level: {level} | Region: {region}"
        else:
            return False, "Profile not found (invalid UID or guest-only)"
    except InvalidParameterError:
        return False, "Invalid UID format"
    except FreeFireAPIError as e:
        return False, f"API Error: {e}"
    except Exception as e:
        return None, f"Error: {type(e).__name__}"


def main():
    # অ্যাকাউন্ট লোড (JSON অগ্রাধিকার)
    accounts = load_accounts_from_json(ACCOUNT_JSON)
    if not accounts:
        accounts = load_accounts_from_txt(UID_PASS_TXT)

    if not accounts:
        print("❌ কোনো অ্যাকাউন্ট পাওয়া যায়নি!")
        return

    print(f"[+] মোট {len(accounts)} টি অ্যাকাউন্ট চেক করা হবে\n")
    print(f"[+] রিজিয়ন: {REGION}\n")

    # FreeFireClient ইনিশিয়ালাইজ
    client = FreeFireClient(server=REGION)

    active = []
    dead = []
    errors = []

    for i, acc in enumerate(accounts, 1):
        uid = acc["uid"]
        password = acc["password"]

        # ১. Ban status চেক
        is_banned, ban_period, ban_msg = check_ban_status(uid)
        
        # ২. Profile existence চেক
        exists, profile_msg = check_profile_exists(client, uid)

        # সিদ্ধান্ত
        if exists is True and is_banned is False:
            status = "✅ ACTIVE"
            active.append(f"{uid}:{password}")
            detail = f"{profile_msg} | {ban_msg}"
        elif exists is True and is_banned is True:
            status = "🚫 BANNED"
            dead.append(f"{uid}:{password}")
            detail = f"{profile_msg} | {ban_msg}"
        elif exists is False:
            status = "❌ DEAD"
            dead.append(f"{uid}:{password}")
            detail = f"{profile_msg}"
        else:
            status = "⚠️  ERROR"
            errors.append(f"{uid}:{password}")
            detail = f"{profile_msg} | {ban_msg}"

        print(f"[{i}/{len(accounts)}] {status}  UID: {uid}")
        print(f"           └─ {detail}\n")

        time.sleep(DELAY_BETWEEN)

    # রেজাল্ট সেভ
    Path(OUTPUT_ACTIVE).write_text("\n".join(active), encoding="utf-8")
    Path(OUTPUT_DEAD).write_text("\n".join(dead), encoding="utf-8")
    Path(OUTPUT_ERROR).write_text("\n".join(errors), encoding="utf-8")

    print("\n" + "=" * 40)
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
