import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    시장분류코드 = input('시장분류코드를 입력하세요 (J : 주식, E : ETF, EN : ETN): ')
    종목코드 = input('종목코드를 입력하세요 (ex. 005930): ')

    request = {
        'In': {
            'InputCondMrktDivCode': 'J', # 입력조건시장분류코드
            'InputIscd1': 종목코드 # 입력종목코드1
        }
    }
    response = await api.request('PRICE', request)
    if response is None: print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (J : 주식, E : ETF, EN : ETN): J
종목코드를 입력하세요 (ex. 005930): 005930
Field Count = 12
+------------------+--------+
|       key        | value  |
+------------------+--------+
|       Sdpr       | 78200  |
|       Prpr       | 77400  |
|       Mxpr       | 101600 |
|       Llam       | 54800  |
|       Oprc       | 78600  |
| SdprVrssMrktRate |  0.51  |
| PrprVrssOprcRate |  1.55  |
|       Hprc       | 78800  |
| SdprVrssHgprRate |  0.77  |
|       Lprc       | 77200  |
| SdprVrssLwprRate | -1.28  |
| PrprVrssLwprRate | -0.26  |
+------------------+--------+
'''
