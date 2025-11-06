import requests
import json

url = "https://data.ntpc.gov.tw/api/v1/openapi/units/1220000"

# 發送 GET 請求
res = requests.get(url, timeout=20)
res.raise_for_status()  # 若錯誤會直接丟出例外

# 將回傳內容轉成 JSON 格式
data = res.json()

# 檢查資料結構
print(type(data))
print(json.dumps(data, ensure_ascii=False, indent=2)[:1000])  # 先看前 1000 字元

# 儲存成 JSON 檔案
with open("ntpc_openapi.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ 已下載並儲存成 ntpc_openapi.json")
