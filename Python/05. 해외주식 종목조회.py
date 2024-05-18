import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

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
        
        alldata = []
        cont_yn = 'N'
        cont_key = ''
        req_count = 0
        while True:
            req_count += 1
            print(f'요청횟수: {req_count}')
            
            response = await api.request('FSTKCODES', request, cont_yn=cont_yn, cont_key=cont_key)
            if response is None:
                print(f'요청실패: {api.last_message}')
                break
            else:
                if 'Out' not in response.body:
                    print(f'응답데이터 없음: {response.body}')
                    break
                alldata += response.body['Out']
                cont_yn = response.cont_yn
                cont_key = response.cont_key
                if cont_yn != 'Y':
                    break
                recv_data_count = len(response.body['Out'])
                if recv_data_count != 400: # 수신갯수가 400개가 아닐시 루프종료
                    break
            
            await asyncio.sleep(0.5) # 초당제한 횟수 2회, 적당히 딜레이 준다
            pass # end while, 요청횟수만큼 반복
    
        print_table(alldata)
            
        pass # end while, 시장분류코드 입력받기 위한 무한루프
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
'''
시장분류코드를 입력하세요 (NY: 뉴욕, NA: 나스닥, AM: 아멕스): NA
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
요청횟수: 12
Row Count = 4487
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
...
...
...
...
|  ZNTL |                     젠테일스 파머슈티컬                      |     헬스케어     |      FN      |      1      |      1      |
|  ZOOZ |                          주즈 파워                           |        IT        |      FN      |      1      |      1      |
|  ZPTA |                     저파타 컴퓨팅 홀딩스                     |        IT        |      FN      |      1      |      1      |
|   ZS  |                          지스케일러                          |        IT        |      FN      |      1      |      1      |
|  ZTEK |                             젠텍                             |       소재       |      FN      |      1      |      1      |
|  ZUMZ |                           주미에즈                           |   경기 소비재    |      FN      |      1      |      1      |
|  ZURA |                         주라 바이오                          |     헬스케어     |      FN      |      1      |      1      |
| ZURAW |              주라 바이오 콜 워런트(2028-03-20)               |                  |      FN      |      1      |      1      |
|  ZVRA |                      지브러 테라퓨틱스                       |     헬스케어     |      FN      |      1      |      1      |
|  ZVSA |                     자이버사 테라퓨틱스                      |     헬스케어     |      FN      |      1      |      1      |
|  ZYME |                           자임웍스                           |     헬스케어     |      FN      |      1      |      1      |
|  ZYXI |                            지넥스                            |     헬스케어     |      FN      |      1      |      1      |
|  ZZZ  |     ONEFUND TRUST CYBER HORNET S&P 500 & BITCOIN 75/25 S     |                  |      FN      |      1      |      1      |
+-------+--------------------------------------------------------------+------------------+--------------+-------------+-------------+
'''
