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
        print("J : 주식, E : ETF, EN : ETN, W: ELW");
        print("F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물");
        print("O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, EU : 야간옵션, SO: 코스닥 150옵션");
        시장분류코드 = input('시장분류코드를 입력하세요 (J,E,...,SO): ')
        종목코드 = input('종목코드를 입력하세요: ')
        차트종류 = input('차트종류를 입력하세요 (1:틱, 2:분, 3:일, 4:주, 5:월): ')
        N봉 = input('N봉을 입력하세요: ') if 차트종류 == '1' or 차트종류 == '2' else ''
        
        response = None
        trcode = None
        if 차트종류 == '1': # 틱
            request = {
                'In': {
                    'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                    'InputIscd1': 종목코드, # 입력종목코드1
                    'InputDate1': '', # 입력날짜1
                    'InputDate2': '', # 입력날짜2
                    'InputDivXtick': N봉 # 틱분틱일별구분코드
                }
            }
            trcode = 'CHARTTICK'
        elif 차트종류 == '2': # 분
            request = {
                'In': {
                    'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                    'InputIscd1': 종목코드, # 입력종목코드1
                    'InputDate1': '', # 입력날짜1
                    'InputDate2': '', # 입력날짜2
                    'InputDivXtick': N봉 # 틱분틱일별구분코드
                }
            }
            trcode = 'CHARTMIN'
        elif 차트종류 == '3': # 일
            request = {
                'In': {
                    'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                    'InputIscd1': 종목코드, # 입력종목코드1
                    'InputDate1': '', # 입력날짜1
                    'InputDate2': '' # 입력날짜2
                }
            }
            trcode = 'CHARTDAY'
        elif 차트종류 == '4': # 주
            request = {
                'In': {
                    'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                    'InputIscd1': 종목코드, # 입력종목코드1
                    'InputDate1': '', # 입력날짜1
                    'InputDate2': '', # 입력날짜2
                    'InputPeriodDivCode': 'W' # 입력주
                }
            }
            trcode = 'CHARTWEEK'
        elif 차트종류 == '5': # 월
            request = {
                'In': {
                    'InputCondMrktDivCode': 시장분류코드, # 입력조건시장분류코드
                    'InputIscd1': 종목코드, # 입력종목코드1
                    'InputDate1': '', # 입력날짜1
                    'InputDate2': '', # 입력날짜2
                    'InputPeriodDivCode': 'M' # 입력일 - 월/년
                }
            }
            trcode = 'CHARTMONTH'
        if not trcode:
            print('잘못된 차트종류 입력')
            continue
        
        response = await api.request(trcode, request)
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
J : 주식, E : ETF, EN : ETN, W: ELW
F : 지수선물, JF : 주식선물, KF : 미니선물, CF : 상품선물, XF : 섹터선물, CM : 야간선물
O : 지수옵션, JO : 주식옵션, KO : 미니옵션, WO : K200위클리옵션, SO: 코스닥 150옵션
시장분류코드를 입력하세요 (J,E,...,SO): J
종목코드를 입력하세요: 005930
차트종류를 입력하세요 (1:틱, 2:분, 3:일, 4:주, 5:월): 3
Row Count = 400
+------+----------+-------+-------+-------+-------+----------+
| Hour |   Date   |  Prpr |  Oprc |  Hprc |  Lprc | AcmlVol  |
+------+----------+-------+-------+-------+-------+----------+
|      | 20240514 | 78300 | 78600 | 78800 | 77900 | 11763992 |
|      | 20240513 | 78400 | 79400 | 79900 | 77600 | 18652344 |
|      | 20240510 | 79200 | 80400 | 81100 | 78900 | 16976124 |
|      | 20240509 | 79700 | 81100 | 81500 | 79700 | 18759935 |
|      | 20240508 | 81300 | 80800 | 81400 | 80500 | 13089576 |
|      | 20240507 | 81300 | 79600 | 81300 | 79400 | 26238868 |
|      | 20240503 | 77600 | 79000 | 79000 | 77500 | 13151889 |
|      | 20240502 | 78000 | 77600 | 78600 | 77300 | 18900640 |
...
'''
