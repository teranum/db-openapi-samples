import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    # 예탁자산현황
    request = {
        'In': {
            'Date': '99999999' # 조회일자 (YYYYMMDD) (99999999 입력시 당일 날짜로 조회)
        }
    }
    response = await api.request('ph131501o', request)
    if response is None: print(f'예탁자산현황 요청실패: {api.last_message}')
    else:
        print('예탁자산현황')
        print_table(response.body['Out'])
        print_table(response.body['Out1'])
        print_table(response.body['Out2'])
    
    # 예탁잔고현황
    request = {
        'In': {
            'Date': '99999999' # 조회일자 (YYYYMMDD) (99999999 입력시 당일 날짜로 조회)
        }
    }
    response = await api.request('ph131601o', request)
    if response is None: print(f'예탁잔고현황 요청실패: {api.last_message}')
    else:
        print('예탁잔고현황')
        print_table(response.body['Out'])
        print_table(response.body['Out1'])
    
    # 해외주식 체결내역조회
    request = {
        'In': {
            'QrySrtDt': '', # 조회시작일자 (YYYYMMDD) (미입력시 당일조회)
            'QryEndDt': '', # 조회종료일자 (YYYYMMDD) (미입력시 당일조회)
            'AstkIsuNo': '', # 해외주식종목번호 (미입력시 전체조회)
            'AstkBnsTpCode': '0', # 해외주식매매구분코드 (0:전체, 1:매도, 2:매수)
            'OrdxctTpCode': '2', # 주문체결구분코드 (0:전체, 1:체결, 2:미체결)
            'StnlnTpCode': '0', # 정렬구분코드 (0:역순, 1:정순)
            'QryTpCode': '0', # 조회구분코드 (0:합산별, 1:건별)
            'OnlineYn': '0', # 온라인여부 (0:전체, Y:온라인, N:오프라인)
            'CvrgOrdYn': '0', # 반대매매주문여부 (0:전체, Y:반대매매주문, N:일반주문)
            'WonFcurrTpCode': '1' # 원화외화구분코드 (1:원화, 2:외화)
        }
    }
    response = await api.request('CAZCQ00100', request)
    if response is None: print(f'해외주식 체결내역조회 요청실패: {api.last_message}')
    else:
        print('해외주식 체결내역조회')
        if 'Out' in response.body: print_table(response.body['Out'])
        if 'Out1' in response.body: print_table(response.body['Out1'])

    ... # 다른 작업 수행
    await api.close()


asyncio.run(main())


# Output:
'''
예탁자산현황
Field Count = 17
+------+----------+
| key  |  value   |
+------+----------+
| Date | 20240517 |
| Pamt |    0     |
| Tamt |    0     |
| Camt |    0     |
| Clpl |    0     |
| Feea |    0     |
| Inpl |    0     |
| Bamt |    0     |
| Opta |    0     |
| Appa |    0     |
| Outa |    0     |
| Orda |    0     |
| Uncl |    0     |
| Daly |    0     |
| Omrg |    0     |
| Umrg |    0     |
| Amrg |    0     |
+------+----------+
Field Count = 4
+------+-------+
| key  | value |
+------+-------+
| Ikey |   0   |
| Sdir |       |
| Aflg |       |
| Nrow |  0001 |
+------+-------+
Row Count = 1
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| Curr | Pamt | Tamt | Camt | Clpl | Feea | Inpl | Bamt | Opta | Appa | Outa | Orda | Uncl | Daly | Omrg | Umrg | Amrg |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| KRW  |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
예탁잔고현황
Field Count = 4
+------+-------+
| key  | value |
+------+-------+
| Ikey |   0   |
| Sdir |       |
| Aflg |       |
| Nrow |  0001 |
+------+-------+
Row Count = 1
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| Curr | Pamt | Tamt | Camt | Clpl | Feea | Inpl | Bamt | Opta | Appa | Outa | Orda | Uncl | Daly | Omrg | Umrg | Amrg | Outh |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| KRW  |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
해외주식 체결내역조회
'''
