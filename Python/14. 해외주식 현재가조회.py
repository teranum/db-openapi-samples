import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
일봉 거래량 필드 매뉴얼과 다름
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    while True:
        시장분류코드 = input('시장분류코드를 입력하세요 (FY:뉴욕, FN:나스닥, FA:아멕스): ')
        종목코드 = input('종목코드를 입력하세요 (ex.AAPL): ')
        
        # 해외주식현재가조회
        request = {
            'In': {
                'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                'InputIscd1': 종목코드 # 입력종목코드1
            }
        }
        response = await api.request('FSTKPRICE', request)
        if response is None: print(f'요청실패: {api.last_message}')
        else:
            print_table(response.body['Out'])
            
        pass # end while, 시장분류코드 입력받기 위한 무한루프
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (FY:뉴욕, FN:나스닥, FA:아멕스): FN
종목코드를 입력하세요 (ex.AAPL): AAPL
Field Count = 13
+------------------+----------+
|       key        |  value   |
+------------------+----------+
|       Sdpr       | 189.8400 |
|       Prpr       | 189.7159 |
|       Mxpr       |  0.0000  |
|       Llam       |  0.0000  |
|       Oprc       | 189.8400 |
| SdprVrssMrktRate |   0.00   |
| PrprVrssOprcRate |          |
|       Hprc       | 190.8100 |
| SdprVrssHgprRate |   0.51   |
| PrprVrssHgprRate |          |
|       Lprc       | 189.2200 |
| SdprVrssLwprRate |  -0.33   |
| PrprVrssLwprRate |          |
+------------------+----------+
'''
