import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
마스터 요청인데... 400개만 던져줌, 연속조회하면 무한에서 빠져 나오지도 않음 (cont_yn이 Y로 나옴)
마스터 데이터를 끊어서 던져주는건 이해가 안됨.
모의투자에서는 조회되지도 않음
주식(J)만 조회됨, ETF, ETN은 조회하면 주식을 돌려줌
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    시장분류코드 = input('시장분류코드를 입력하세요 (J:주식, E:ETF, EN:ETN): ')
    request = {
        'In': {
            'InputCondMrktDivCode': 시장분류코드,
        }
    }

    alldata = []
    cont_yn = 'N'
    cont_key = ''
    req_count = 0
    while True:
        req_count += 1
        print(f'요청횟수: {req_count}')
            
        response = await api.request('JCODES', request, cont_yn=cont_yn, cont_key=cont_key)
        if response is None:
            print(f'요청실패: {api.last_message}')
            break
        else:
            alldata += response.body['Out']
            cont_yn = response.cont_yn
            cont_key = response.cont_key
            if cont_yn != 'Y':
                break
            recv_data_count = len(response.body['Out'])
            if recv_data_count != 400: # 수신갯수가 400개가 아닐시 루프종료
                break
            
        await asyncio.sleep(0.5) # 초당제한 횟수 3회, 적당히 딜레이 준다
        pass # end while, 요청횟수만큼 반복
        
    print_table(alldata)
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (J:주식, E:ETF, EN:ETN): J
요청횟수: 1
요청횟수: 2
요청횟수: 3
요청횟수: 4
요청횟수: 5
요청횟수: 6
요청횟수: 7
요청횟수: 8
요청횟수: 9
요청횟수: 10
요청횟수: 11
Row Count = 4050
+--------+--------------+------------------------------------------+-------------+
|  Iscd  |   StndIscd   |                 KorIsnm                  | MrktClsCode |
+--------+--------------+------------------------------------------+-------------+
| 000020 | KR7000020008 |                 동화약품                 |      1      |
| 000040 | KR7000040006 |                 KR모터스                 |      1      |
| 000050 | KR7000050005 |                   경방                   |      1      |
| 000070 | KR7000070003 |                삼양홀딩스                |      1      |
| 000075 | KR7000071001 |               삼양홀딩스우               |      1      |
| 000080 | KR7000080002 |                하이트진로                |      1      |
| 000087 | KR7000082008 |              하이트진로2우B              |      1      |
| 000100 | KR7000100008 |                 유한양행                 |      1      |
| 000105 | KR7000101006 |                유한양행우                |      1      |
| 000120 | KR7000120006 |                CJ대한통운                |      1      |
| 000140 | KR7000140004 |             하이트진로홀딩스             |      1      |
| 000145 | KR7000141002 |            하이트진로홀딩스우            |      1      |
...
'''
