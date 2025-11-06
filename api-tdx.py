# ==== Colab: TDX 訪客模式抓取 InterCity 即時車輛資料 ====
import os, requests, json

# 1) 先填你的「訪客用 client_id / client_secret」
#   （若單位有發 Visitor/Guest 憑證就填那組；沒有就填你自己的 App 憑證）
CLIENT_ID     = os.getenv("TDX_CLIENT_ID",     "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("TDX_CLIENT_SECRET", "YOUR_CLIENT_SECRET")

AUTH_URL = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
API_URL  = "https://tdx.transportdata.tw/api/basic/v2/Bus/RealTimeByFrequency/Streaming/InterCity"

def get_access_token(client_id, client_secret):
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    r = requests.post(AUTH_URL, data=data, timeout=20)
    r.raise_for_status()
    return r.json()["access_token"]

token = get_access_token(CLIENT_ID, CLIENT_SECRET)

# 2) 取資料（可依需要調整 $top / 篩選條件）
params = {
    "$top": 2000,          # 取前 2000 筆；可視需要加上 $filter 限縮城市/時間
    "$format": "JSON",
}
headers = {
    "Authorization": f"Bearer {token}",
    "Accept-Encoding": "gzip",
}

resp = requests.get(API_URL, headers=headers, params=params, timeout=30)
resp.raise_for_status()
data = resp.json()

print(f"records: {len(data)}")
print(json.dumps(data[:3], ensure_ascii=False, indent=2))   # 先看前三筆

# 3) 需要存檔就取消下行註解
# with open("intercity_realtime.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
