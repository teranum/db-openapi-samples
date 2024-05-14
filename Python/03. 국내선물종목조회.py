import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
지수선물 외 다른거 먹히지도 않음
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    while True:
        시장분류코드 = input('시장분류코드를 입력하세요 (F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물): ')

        request = {
            'In': {
                'InputCondMrktDivCode': 시장분류코드,
            }
        }
        response = await api.request('FCODES', request)
        if response is None:
            print(f'요청실패: {api.last_message}')
        else:
            print_table(response.body['Out'])
    
        pass # end while, 무한루프
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물): F
Row Count = 13
+----------+--------------+-------------------+--------+
|   Iscd   |   StndIscd   |      KorIsnm      |  Sdpr  |
+----------+--------------+-------------------+--------+
| 101V6000 | KR4101V60002 |   K200 F 202406   | 371.65 |
| 101V9000 | KR4101V90009 |   K200 F 202409   | 373.85 |
| 101VC000 | KR4101VC0004 |   K200 F 202412   | 375.30 |
| 101W3000 | KR4101W30003 |   K200 F 202503   | 375.00 |
| 101W6000 | KR4101W60000 |   K200 F 202506   | 377.30 |
| 101WC000 | KR4101WC0003 |   K200 F 202512   | 381.70 |
| 401V66CS | KR4401V66CS9 | K200 SP 2406-2612 |  0.00  |
| 401V6V9S | KR4401V6V9S1 | K200 SP 2406-2409 |  0.00  |
| 401V6VCS | KR4401V6VCS3 | K200 SP 2406-2412 |  0.00  |
| 401V6W3S | KR4401V6W3S3 | K200 SP 2406-2503 |  0.00  |
| 401V6W6S | KR4401V6W6S6 | K200 SP 2406-2506 |  0.00  |
| 401V6WCS | KR4401V6WCS1 | K200 SP 2406-2512 |  0.00  |
| A016C000 | KR4A016C0004 |   K200 F 202612   | 386.95 |
+----------+--------------+-------------------+--------+
'''
