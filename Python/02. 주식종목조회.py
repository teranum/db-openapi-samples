import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
마스터 요청인데... 400개만 던져줌, 연속조회하면 무한에서 빠져 나오지도 않음
마스터 데이터를 끊어서 던져주는건 이해가 안됨.
모의투자에서는 조회되지도 않음
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    request = {
        'In': {
            'InputCondMrktDivCode': 'J', # 시장분류코드 (J: 주식, E: ETF, EN: ETN)
        }
    }
    response = await api.request('JCODES', request)
    if response is None:
        print(f'요청실패: {api.last_message}')
    else:
        print_table(response.body['Out'])
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
Row Count = 400
+--------+--------------+------------------------+-------------+
|  Iscd  |   StndIscd   |        KorIsnm         | MrktClsCode |
+--------+--------------+------------------------+-------------+
| 000020 | KR7000020008 |        동화약품        |      1      |
| 000040 | KR7000040006 |        KR모터스        |      1      |
| 000050 | KR7000050005 |          경방          |      1      |
| 000070 | KR7000070003 |       삼양홀딩스       |      1      |
| 000075 | KR7000071001 |      삼양홀딩스우      |      1      |
| 000080 | KR7000080002 |       하이트진로       |      1      |
| 000087 | KR7000082008 |     하이트진로2우B     |      1      |
| 000100 | KR7000100008 |        유한양행        |      1      |
| 000105 | KR7000101006 |       유한양행우       |      1      |
| 000120 | KR7000120006 |       CJ대한통운       |      1      |
| 000140 | KR7000140004 |    하이트진로홀딩스    |      1      |
| 000145 | KR7000141002 |   하이트진로홀딩스우   |      1      |
| 000150 | KR7000150003 |          두산          |      1      |
| 000155 | KR7000151001 |         두산우         |      1      |
| 000157 | KR7000152009 |        두산2우B        |      1      |
| 000180 | KR7000180000 |      성창기업지주      |      1      |
| 000210 | KR7000210005 |           DL           |      1      |
| 000215 | KR7000211003 |          DL우          |      1      |
| 000220 | KR7000220004 |        유유제약        |      1      |
| 000225 | KR7000221002 |      유유제약1우       |      1      |
| 000227 | KR7000222000 |      유유제약2우B      |      1      |
| 000230 | KR7000230003 |       일동홀딩스       |      1      |
...
'''
