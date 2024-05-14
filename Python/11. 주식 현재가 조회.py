import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')
    
    종목코드 = input('종목코드를 입력하세요 (ex: 005930): ')

    request = {
        'In': {
            'InputCondMrktDivCode': 'J ', # 시장분류코드 (J: 주식, E: ETF, EN: ETN)
            'InputIscd1': 종목코드, # 종목코드
        }
    }
    response = await api.request('PRICE', request)
    if response is None:
        print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
종목코드를 입력하세요 (ex: 005930): 005930
Field Count = 12
+------------------+--------+
|       key        | value  |
+------------------+--------+
|       Sdpr       | 78400  |
|       Prpr       | 78000  |
|       Mxpr       | 101900 |
|       Llam       | 54900  |
|       Oprc       | 78600  |
| SdprVrssMrktRate |  0.26  |
| PrprVrssOprcRate |  0.77  |
|       Hprc       | 78800  |
| SdprVrssHgprRate |  0.51  |
|       Lprc       | 77900  |
| SdprVrssLwprRate | -0.64  |
| PrprVrssLwprRate | -0.13  |
+------------------+--------+
...
'''
