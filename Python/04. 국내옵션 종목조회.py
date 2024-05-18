import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
지수옵션외 다른거 안먹힘.
400 개만 던져주고, 연속조회하면 무한 요청됨, 끝나지 않음...
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    while True:
        시장분류코드 = input('시장분류코드를 입력하세요 (O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, EU : 야간옵션, SO: 코스닥 150옵션): ')

        request = {
            'In': {
                'InputCondMrktDivCode': 시장분류코드,
            }
        }
        response = await api.request('OCODES', request)
        if response is None:
            print(f'요청실패: {api.last_message}')
        else:
            print_table(response.body['Out'])
            
        pass # end while, 시장분류코드 입력받기 위한 무한루프
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, EU : 야간옵션, SO: 코스닥 150옵션): O
Row Count = 400
+----------+--------------+----------------+------------+-----------------+
|   Iscd   |   StndIscd   |    KorIsnm     | AtmClsCode |      TrMltl     |
+----------+--------------+----------------+------------+-----------------+
| 201V6160 | KR4201V61602 | C 202406 160.0 |     2      | 250000.00000000 |
| 201V6162 | KR4201V61628 | C 202406 162.5 |     2      | 250000.00000000 |
| 201V6165 | KR4201V61651 | C 202406 165.0 |     2      | 250000.00000000 |
| 201V6167 | KR4201V61677 | C 202406 167.5 |     2      | 250000.00000000 |
| 201V6170 | KR4201V61701 | C 202406 170.0 |     2      | 250000.00000000 |
| 201V6172 | KR4201V61727 | C 202406 172.5 |     2      | 250000.00000000 |
| 201V6175 | KR4201V61750 | C 202406 175.0 |     2      | 250000.00000000 |
| 201V6177 | KR4201V61776 | C 202406 177.5 |     2      | 250000.00000000 |
| 201V6180 | KR4201V61800 | C 202406 180.0 |     2      | 250000.00000000 |
| 201V6182 | KR4201V61826 | C 202406 182.5 |     2      | 250000.00000000 |
| 201V6185 | KR4201V61859 | C 202406 185.0 |     2      | 250000.00000000 |
| 201V6187 | KR4201V61875 | C 202406 187.5 |     2      | 250000.00000000 |
| 201V6190 | KR4201V61909 | C 202406 190.0 |     2      | 250000.00000000 |
| 201V6192 | KR4201V61925 | C 202406 192.5 |     2      | 250000.00000000 |
| 201V6195 | KR4201V61958 | C 202406 195.0 |     2      | 250000.00000000 |
| 201V6197 | KR4201V61974 | C 202406 197.5 |     2      | 250000.00000000 |
| 201V6200 | KR4201V62006 | C 202406 200.0 |     2      | 250000.00000000 |
| 201V6202 | KR4201V62022 | C 202406 202.5 |     2      | 250000.00000000 |
| 201V6205 | KR4201V62055 | C 202406 205.0 |     2      | 250000.00000000 |
...
'''
