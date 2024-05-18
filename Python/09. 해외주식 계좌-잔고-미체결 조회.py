import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    # 해외주식 예수금상세
    request = {
        'In': {}
    }
    response = await api.request('CAZCQ01400', request)
    if response is None: print(f'해외주식 예수금상세 요청실패: {api.last_message}')
    else:
        print('해외주식 예수금상세')
        response.body: print_table(response.body['Out'])
        response.body: print_table(response.body['Out1'])
    
    # 해외주식 잔고/증거금 조회
    request = {
        'In': {
            'TrxTpCode': '2', # 처리구분코드 (1:외화잔고, 2:주식잔고상세, 3:주식잔고(국가별), 9:당일실현손익)
            'CmsnTpCode': '0', # 수수료구분코드 (0:전부 미포함, 1:매수제비용만 포함, 2:매수제비용+매도제비용)
            'WonFcurrTpCode': '1', # 원화외화구분코드 (1:원화, 2:외화)
            'DpntBalTpCode': '0' # 소수점잔고구분코드 (0: 전체, 1: 일반, 2: 소수점)
        }
    }
    response = await api.request('CAZCQ00400', request)
    if response is None: print(f'해외주식 잔고/증거금 조회 요청실패: {api.last_message}')
    else:
        print('해외주식 잔고/증거금 조회')
        if 'Out' in response.body: print_table(response.body['Out'])
        if 'Out1' in response.body: print_table(response.body['Out1'])
        if 'Out2' in response.body: print_table(response.body['Out2'])
        if 'Out3' in response.body: print_table(response.body['Out3'])
   
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
해외주식 예수금상세
Field Count = 6
+------------+----------+
|    key     |  value   |
+------------+----------+
| OtptItemNm | 결제일자 |
| DpsBaseDt0 | 20240517 |
| DpsBaseDt1 | 20240520 |
| DpsBaseDt2 | 20240521 |
| DpsBaseDt3 | 20240522 |
| DpsBaseDt4 | 20240523 |
+------------+----------+
Row Count = 1
+----------+------------+-------------+-------------+-------------+-------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+
| CrcyCode | CrcyCodeNm | OtptItemNm0 | OtptItemNm1 | OtptItemNm2 | OtptItemNm3 | AstkDps0 | AstkBnsAmt0 | AstkUnsttBuyAmt0 | AstkUnsttSellAmt0 | AstkDps1 | AstkBnsAmt1 | AstkUnsttBuyAmt1 | AstkUnsttSellAmt1 | AstkDps2 | AstkBnsAmt2 | AstkUnsttBuyAmt2 | AstkUnsttSellAmt2 | AstkDps3 | AstkBnsAmt3 | AstkUnsttBuyAmt3 | AstkUnsttSellAmt3 | AstkDps4 | AstkBnsAmt4 | AstkUnsttBuyAmt4 | AstkUnsttSellAmt4 |
+----------+------------+-------------+-------------+-------------+-------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+
|   KRW    |    원화    |    예수금   |   매매결제  |   매수결제  |   매도결제  | 0.000000 |   0.000000  |     0.000000     |      0.000000     | 0.000000 |   0.000000  |     0.000000     |      0.000000     | 0.000000 |   0.000000  |     0.000000     |      0.000000     | 0.000000 |   0.000000  |     0.000000     |      0.000000     | 0.000000 |   0.000000  |     0.000000     |      0.000000     |
+----------+------------+-------------+-------------+-------------+-------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+----------+-------------+------------------+-------------------+
해외주식 잔고/증거금 조회
해외주식 체결내역조회
'''
