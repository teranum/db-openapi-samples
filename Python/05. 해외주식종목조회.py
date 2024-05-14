import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    while True:
        시장분류코드 = input('시장분류코드를 입력하세요 (NY: 뉴욕, NA: 나스닥, AM: 아멕스): ')

        request = {
            'In': {
                'InputDataCode': 시장분류코드,
            }
        }
        response = await api.request('FSTKCODES', request)
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
시장분류코드를 입력하세요 (NY: 뉴욕, NA: 나스닥, AM: 아멕스): NA
Row Count = 400
+-------+--------------------------------------------------------------+------------------+--------------+-------------+-------------+
|  Iscd |                           KorIsnm                            |   BstpLargName   | ExchClsCode2 | SelnVolUnit | ShnuVolUnit |
+-------+--------------------------------------------------------------+------------------+--------------+-------------+-------------+
|  AACG |                 ATA 크리에티비티 글로벌(ADR)                 |   경기 소비재    |      FN      |      1      |      1      |
|  AACI |                       아마다 애퀴지션                        |       금융       |      FN      |      1      |      1      |
| AACIU |                     아마다 애퀴지션 유닛                     |       금융       |      FN      |      1      |      1      |
|  AADI |                     AADI 바이오사이언스                      |     헬스케어     |      FN      |      1      |      1      |
|  AADR |   ADVISORSHARES TRUST ADVISORSHARES DORSEY WRIGHT ADR ETF    |                  |      FN      |      1      |      1      |
|  AAGR |                  아프리칸 애그리컬처 홀딩스                  |   필수 소비재    |      FN      |      1      |      1      |
|  AAL  |                   아메리칸 에어라인스 그룹                   |      산업재      |      FN      |      1      |      1      |
|  AAME |                      애틀랜틱 아메리칸                       |       금융       |      FN      |      1      |      1      |
|  AAOI |                 어플라이드 옵토일렉트로닉스                  |        IT        |      FN      |      1      |      1      |
|  AAON |                          에이에이온                          |      산업재      |      FN      |      1      |      1      |
|  AAPB |        GRANITESHARES ETF TRUST 2X LONG AAPL DAILY ETF        |                  |      FN      |      1      |      1      |
|  AAPD |       DIREXION SHARES ETF TRUST DAILY AAPL BEAR 1X SHS       |                  |      FN      |      1      |      1      |
|  AAPL |                             애플                             |        IT        |      FN      |      1      |      1      |
|  AAPU |              DIREXION DAILY AAPL BULL 2X SHARES              |                  |      FN      |      1      |      1      |
|  AAXJ |       ISHARES TRUST MSCI ALL COUNTRY ASIA EX JAPAN ETF       |                  |      FN      |      1      |      1      |
|  ABAT |                  아메리칸 배터리 테크놀로지                  |       소재       |      FN      |      1      |      1      |
|  ABCB |                       아메리스 뱅코프                        |       금융       |      FN      |      1      |      1      |
|  ABCL |                    앱셀레라 바이오로직스                     |     헬스케어     |      FN      |      1      |      1      |
|  ABCS |   EA SERIES TRUST ALPHA BLUE CAP US SM-MID CAP DYNAMIC ETF   |                  |      FN      |      1      |      1      |
|  ABEO |                     아베오나 테라퓨틱스                      |     헬스케어     |      FN      |      1      |      1      |
|  ABIO |                       ARCA 바이오파머                        |     헬스케어     |      FN      |      1      |      1      |
|  ABL  |                       애버커스 라이프                        |       금융       |      FN      |      1      |      1      |
| ABLLL |        애버커스 라이프 선순위채권(2028-11-15 9.875%)         |                  |      FN      |      1      |      1      |
|  ABLV |                       에이블 뷰 글로벌                       |      산업재      |      FN      |      1      |      1      |
|  ABNB |                          에어비앤비                          |   경기 소비재    |      FN      |      1      |      1      |
|  ABOS |                     애커먼 파머슈티컬스                      |     헬스케어     |      FN      |      1      |      1      |
|  ABSI |                            압사이                            |     헬스케어     |      FN      |      1      |      1      |
...
'''
