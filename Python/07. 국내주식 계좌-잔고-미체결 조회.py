import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    # 계좌예수금조회
    request = {
        'In': {}
    }
    response = await api.request('CDPCQ00100', request)
    if response is None: print(f'계좌예수금조회 요청실패: {api.last_message}')
    else:
        print('계좌예수금조회')
        print_table(response.body['Out1'])

     # 주식잔고조회
    request = {
        'In': {
            'QryTpCode0': '2' # 조회구분코드0 (0:전체, 1:비상장제외, 2:비상장,코넥스,kotc 제외)
        }
    }
    response = await api.request('CSPAQ03420', request)
    if response is None: print(f'주식잔고조회 요청실패: {api.last_message}')
    else:
        print('주식잔고조회')
        print_table(response.body['Out'])
        print_table(response.body['Out1'])
   
    # 체결/미체결조회
    request = {
        'In': {
            'ExecYn': '2', # 체결여부 (0:전체, 1:체결, 2:미체결)
            'BnsTpCode': '0', # 매매구분 (0:전체, 1:매도, 2:매수)
            'IsuTpCode': '0', # 종목구분 (0:전체)
            'QryTp': '0' # 조회구분 (0:전체, 1:ELW , 2:ELW제외)
        }
    }
    response = await api.request('CSPAQ04800', request)
    if response is None: print(f'미체결조회 요청실패: {api.last_message}')
    else:
        print('미체결조회')
        print_table(response.body['Out'])
        print_table(response.body['Out1'])

    ... # 다른 작업 수행
    await api.close()


asyncio.run(main())


# Output:
'''
계좌예수금조회
Field Count = 50
+-----------------------+-------+
|          key          | value |
+-----------------------+-------+
|       DpsBalAmt       |   0   |
|         MgnMny        |   0   |
|       PldgCurAmt      |   0   |
|     AddCrdtPldgMny    |   0   |
|      RcvblEnsrAmt     |   0   |
|        SubstAmt       |   0   |
|        SubstMgn       |   0   |
|     PldgSubstAmt0     |   0   |
|    AddCrdtPldgSubst   |   0   |
|        RgtsbAmt       |   0   |
|        ChckAmt        |   0   |
|    UnSettEtcChckAmt   |   0   |
|    CrdtPldgRuseAmt    |   0   |
|         Imreq         |   0   |
|     DpslRestrcAmt     |   0   |
|      WthdwAbleAmt     |   0   |
|     SfaccMloanAmt     |   0   |
|     MktcplMloanAmt    |   0   |
|      MloanTotamt      |   0   |
|     SfaccSloanAmt     |   0   |
|     MktcplSloanAmt    |   0   |
|      SloanTotamt      |   0   |
|       MnyrclAmt       |   0   |
|     IntrstDlinqAmt    |   0   |
|         Etclnd        |   0   |
|     OldUnRfundAmt     |   0   |
|   DpspdgLoanEvalAmt   |   0   |
|   DpspdgLoanAbleLmt   |   0   |
|     DpspdgLoanBal     |   0   |
|   DpspdgLoanAbleAmt   |   0   |
|  DpspdgLoanIntdltAmt  |   0   |
|     PmLoanEvalAmt     |   0   |
|     PmLoanAbleLmt     |   0   |
|       PmLoanBal       |   0   |
|     PmLoanAbleAmt     |   0   |
|    PmLoanIntdltAmt    |   0   |
|     BuyAdjstAmtD1     |   0   |
|     SellAdjstAmtD1    |   0   |
|     RepayRqrdAmtD1    |   0   |
|      PrsmptDpsD1      |   0   |
| PrsmptMnyoutAbleAmtD1 |   0   |
|     BuyAdjstAmtD2     |   0   |
|     SellAdjstAmtD2    |   0   |
|     RepayRqrdAmtD2    |   0   |
|      PrsmptDpsD2      |   0   |
| PrsmptMnyoutAbleAmtD2 |   0   |
|     MnyRuseUseAmt     |   0   |
|     MnyRuseUseAmt1    |   0   |
|    SubstRuseUseAmt    |   0   |
|    SubstRuseUseAmt1   |   0   |
+-----------------------+-------+
주식잔고조회
Field Count = 10
+----------------+--------+
|      key       | value  |
+----------------+--------+
|   TotBuyAmt    |   0    |
|   TotEvalAmt   |   0    |
| TotEvalPnlAmt  |   0    |
|   TotErnrat    | 0.0000 |
|  ThdaySellAmt  |   0    |
|  ThdayBuyAmt   |   0    |
| ThdayRlzPnlAmt |   0    |
|   CrdtBnsAmt   |   0    |
|   DpsastAmt    |   0    |
|      Dps2      |   0    |
+----------------+--------+
미체결조회
Field Count = 4
+-------------+-------+
|     key     | value |
+-------------+-------+
| SellExecQty |   0   |
|  BuyExecQty |   0   |
| SellExecAmt |   0   |
|  BuyExecAmt |   0   |
+-------------+-------+
'''
