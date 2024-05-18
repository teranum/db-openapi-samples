import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    request = {
        'In': {
            'InputDateClsCode': '0', # 입력일자구분코드 (당일:0, 전일:1, 주간:2, 월간:5)
            'InputRankSortClsCode1': '12', # 입력순위정렬구분코드1 (상승률:12, 하락율:11)
            'InputMrktClsCode': 'A', # 입력시장구분코드 (전체:A, 코스피:K, 코스닥:Q)
            'InputBstpIscd': '' # 입력업종코드 (입력시장구분코드 "A" 일시 입력 X, 코스피:1001, 코스닥:2001)
        }
    }
    response = await api.request('RANKLIST', request)
    if response is None: print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
Row Count = 400
+--------+------------------------------------------+----------+--------+--------------+----------+----------+
|  Iscd  |                 KorIsnm                  | DataRank |  Prpr  | PrdyVrssSign | PrdyVrss | PrdyCtrt |
+--------+------------------------------------------+----------+--------+--------------+----------+----------+
| 456010 |               아이씨티케이               |    1     | 28700  |      2       |   8700   |  43.50   |
| 003230 |                 삼양식품                 |    2     | 446500 |      1       |  103000  |  29.99   |
| 044480 |               블레이드 Ent               |    3     |  1331  |      1       |   307    |  29.98   |
| 033790 |           스카이문스테크놀로지           |    4     |  8070  |      1       |   1860   |  29.95   |
| 000390 |                삼화페인트                |    5     |  9770  |      1       |   2250   |  29.92   |
| 260970 |                 에스앤디                 |    6     | 39950  |      1       |   9200   |  29.92   |
| 294090 |                이오플로우                |    7     | 12290  |      1       |   2830   |  29.92   |
| 006620 |              동구바이오제약              |    8     |  7810  |      2       |   1320   |  20.34   |
| 322510 |                제이엘케이                |    9     | 15210  |      2       |   2450   |  19.20   |
| 298040 |                효성중공업                |    10    | 370500 |      2       |  56000   |  17.81   |
| 314130 |               지놈앤컴퍼니               |    11    |  9000  |      2       |   1360   |  17.80   |
| 005180 |                  빙그레                  |    12    | 88300  |      2       |  12700   |  16.80   |
| 091340 |                S&K폴리텍                 |    13    |  2765  |      2       |   395    |  16.67   |
| 053950 |                 경남제약                 |    14    |  1420  |      2       |   189    |  15.35   |
| 107600 |                  새빗켐                  |    15    | 52800  |      2       |   6900   |  15.03   |
| 099220 |                   SDN                    |    16    |  2115  |      2       |   245    |  13.10   |
| 296640 |                 이노룰스                 |    17    |  8400  |      2       |   940    |  12.60   |
...
'''
