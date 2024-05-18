import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    print("F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물");
    print("O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, EU : 야간옵션, SO: 코스닥 150옵션");
    시장분류코드 = input('시장분류코드를 입력하세요 (F,O,...,SO): ')
    종목코드 = input('종목코드를 입력하세요: ')

    request = {
        'In': {
            'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
            'InputIscd1': 종목코드 # 입력종목코드1
        }
    }
    response = await api.request('FPRICE', request)
    if response is None: print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물
O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, EU : 야간옵션, SO: 코스닥 150옵션
시장분류코드를 입력하세요 (F,O,...,SO): F
종목코드를 입력하세요: 101V6000
Field Count = 12
+------------------+--------+
|       key        | value  |
+------------------+--------+
|       Sdpr       | 376.00 |
|       Prpr       | 371.35 |
|       Mxpr       | 406.05 |
|       Llam       | 345.95 |
|       Oprc       | 374.35 |
| SdprVrssMrktRate | -0.44  |
| PrprVrssOprcRate |        |
|       Hprc       | 375.60 |
| SdprVrssHgprRate | -0.11  |
|       Lprc       | 371.20 |
| SdprVrssLwprRate | -1.28  |
| PrprVrssLwprRate |        |
+------------------+--------+
'''
