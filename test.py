# 安裝套件
# pip install requests

# 取得 Access Token 的範例程式碼
import requests

auth_url = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET'
}

response = requests.post(auth_url, data=auth_data)
access_token = response.json()['access_token']

# 呼叫 API 取得台北市公車路線資料
api_url = "https://tdx.transportdata.tw/api/basic/v2/Bus/Route/City/Taipei"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept-Encoding': 'gzip'
}

bus_data = requests.get(api_url, headers=headers)
print(bus_data.json())
