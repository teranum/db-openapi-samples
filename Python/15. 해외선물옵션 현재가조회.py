import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
해외선물옵션 로그인시 반드시 wss_domain 옵션을 dbopenapi.WSS_URL_GLOBAL로 설정.
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey, wss_domain=dbopenapi.WSS_URL_GLOBAL): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token, wss_domain=dbopenapi.WSS_URL_GLOBAL): return print(f'연결실패: {api.last_message}')

    종목코드 = input('종목코드를 입력하세요: ')
    
    # 호가 & 현재가 조회
    request = {
        'In': {
            'Code': 종목코드 # 종목코드
        }
    }
    response = await api.request('pibo7042', request)
    if response is None: print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
        print_table(response.body['Out1'])
        print_table(response.body['Out2'])
        print_table(response.body['Out3'])
    
    ... # 다른 작업 수행
    await api.close()
    
asyncio.run(main())

# Output:
'''
종목코드를 입력하세요: HSIK24
Field Count = 11
+------+----------+
| key  |  value   |
+------+----------+
| Code |  HSIK24  |
| Last |  19708   |
| Diff |   166    |
| Rate |   0.84   |
| Open |  19543   |
| High |  19772   |
| Lowp |  19505   |
| Clos |  19542   |
| Tvol |  18155   |
| Lvol |    1     |
| Htim | 01:15:54 |
+------+----------+
Row Count = 5
+-------+------+------+
|  Askp | Askq | Askn |
+-------+------+------+
| 19708 |  4   |  4   |
| 19709 |  6   |  6   |
| 19710 |  6   |  4   |
| 19711 |  6   |  6   |
| 19712 |  5   |  5   |
+-------+------+------+
Row Count = 5
+-------+------+------+
|  Bidp | Bidq | Bidn |
+-------+------+------+
| 19706 |  2   |  2   |
| 19705 |  17  |  8   |
| 19704 |  3   |  3   |
| 19703 |  9   |  9   |
| 19702 |  8   |  8   |
+-------+------+------+
Field Count = 5
+-------+------------+
|  key  |   value    |
+-------+------------+
| Taskq |     27     |
| Tbidq |     39     |
| Taskn |     25     |
| Tbidn |     30     |
|  Bday | 2024/05/20 |
+-------+------------+
'''