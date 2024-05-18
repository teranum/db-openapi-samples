import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    # 선물옵션 가정산예탁금 상세
    request = {
        'In': {
            'BnsDt': '99999999' # 매매일
        }
    }
    response = await api.request('CFOEQ11100', request)
    if response is None: print(f'선물옵션 가정산예탁금 상세 요청실패: {api.last_message}')
    else:
        print('선물옵션 가정산예탁금 상세')
        print_table(response.body['Out'])

    # 선물옵션 잔고 조회
    request = {
        'In': {}
    }
    response = await api.request('CFOAQ02500', request)
    if response is None: print(f'선물옵션 잔고 조회 요청실패: {api.last_message}')
    else:
        print('선물옵션 잔고 조회')
        print_table(response.body['Out'])
        print_table(response.body['Out1'])
   
    # 선물옵션 체결조회
    request = {
        'In': {
            'ExecTpCode': '2', # 체결구분코드 (0:전체, 1:체결, 2:미체결)
            'BnsTpCode': '0', # 매매구분코드 (0:전체, 1:매도, 2:매수)
            'IsuTpCode': '', # 종목구분코드 (전체: 빈문자열)
            'FnoIsuNo': '' # 선물옵션종목번호 (전체: 빈문자열)
        }
    }
    response = await api.request('CFOAQ04000', request)
    if response is None: print(f'선물옵션 체결조회 요청실패: {api.last_message}')
    else:
        print('선물옵션 체결조회')
        print_table(response.body['Out'])

    ... # 다른 작업 수행
    await api.close()


asyncio.run(main())


# Output:
'''
선물옵션 가정산예탁금 상세
Field Count = 98
+-------------------------+-------+
|           key           | value |
+-------------------------+-------+
|          AcntNm         |       |
|    OpnmkDpsamtTotamt    |   0   |
|         OpnmkDps        |   0   |
|      OpnmkMnyrclAmt     |   0   |
|      OpnmkSubstAmt      |   0   |
|          TotAmt         |   0   |
|           Dps           |   0   |
|        MnyrclAmt        |   0   |
|       SubstDsgnAmt      |   0   |
|         CsgnMgn         |   0   |
|        MnyCsgnMgn       |   0   |
|         MaintMgn        |   0   |
|       MnyMaintMgn       |   0   |
|        OutAbleAmt       |   0   |
|      MnyoutAbleAmt      |   0   |
|     SubstOutAbleAmt     |   0   |
|        OrdAbleAmt       |   0   |
|      MnyOrdAbleAmt      |   0   |
|     AddMgnOcrTpCode     |   0   |
|          AddMgn         |   0   |
|        MnyAddMgn        |   0   |
|       NtdayTotAmt       |   0   |
|         NtdayDps        |   0   |
|      NtdayMnyrclAmt     |   0   |
|      NtdaySubstAmt      |   0   |
|       NtdayCsgnMgn      |   0   |
|     NtdayMnyCsgnMgn     |   0   |
|      NtdayMaintMgn      |   0   |
|     NtdayMnyMaintMgn    |   0   |
|     NtdayOutAbleAmt     |   0   |
|    NtdayMnyoutAbleAmt   |   0   |
|   NtdaySubstOutAbleAmt  |   0   |
|     NtdayOrdAbleAmt     |   0   |
|    NtdayMnyOrdAbleAmt   |   0   |
|      NtdayAddMgnTp      |   0   |
|       NtdayAddMgn       |   0   |
|      NtdayMnyAddMgn     |   0   |
|       NtdaySettAmt      |   0   |
|     EvalDpsamtTotamt    |   0   |
|     MnyEvalDpstgAmt     |   0   |
| DpsamtUtlfeeGivPrergAmt |   0   |
|          TaxAmt         |   0   |
|        CsgnMgnrat       |  0.00 |
|      CsgnMnyMgnrat      |  0.00 |
|    DpstgTotamtLackAmt   |   0   |
|     DpstgMnyLackAmt     |   0   |
|        RealInAmt        |   0   |
|          InAmt          |   0   |
|          OutAmt         |   0   |
|      FutsAdjstDfamt     |   0   |
|      FutsThdayDfamt     |   0   |
|      FutsUpdtDfamt      |   0   |
|    FutsLastSettDfamt    |   0   |
|       OptSettDfamt      |   0   |
|        OptBuyAmt        |   0   |
|        OptSellAmt       |   0   |
|       OptXrcDfamt       |   0   |
|       OptAsgnDfamt      |   0   |
|      RealGdsUndAmt      |   0   |
|    RealGdsUndAsgnAmt    |   0   |
|     RealGdsUndXrcAmt    |   0   |
|         CmsnAmt         |   0   |
|         FutsCmsn        |   0   |
|         OptCmsn         |   0   |
|       FutsCtrctQty      |   0   |
|       FutsCtrctAmt      |   0   |
|       OptCtrctQty       |   0   |
|       OptCtrctAmt       |   0   |
|       FutsUnsttQty      |   0   |
|       FutsUnsttAmt      |   0   |
|       OptUnsttQty       |   0   |
|       OptUnsttAmt       |   0   |
|     FutsBuyUnsttQty     |   0   |
|     FutsBuyUnsttAmt     |   0   |
|     FutsSellUnsttQty    |   0   |
|     FutsSellUnsttAmt    |   0   |
|      OptBuyUnsttQty     |   0   |
|      OptBuyUnsttAmt     |   0   |
|     OptSellUnsttQty     |   0   |
|     OptSellUnsttAmt     |   0   |
|      FutsBuyctrQty      |   0   |
|      FutsBuyctrAmt      |   0   |
|       FutsSlctrQty      |   0   |
|       FutsSlctrAmt      |   0   |
|       OptBuyctrQty      |   0   |
|       OptBuyctrAmt      |   0   |
|       OptSlctrQty       |   0   |
|       OptSlctrAmt       |   0   |
|       FutsBnsplAmt      |   0   |
|       OptBnsplAmt       |   0   |
|      FutsEvalPnlAmt     |   0   |
|      OptEvalPnlAmt      |   0   |
|       FutsEvalAmt       |   0   |
|        OptEvalAmt       |   0   |
|     MktEndAfMnyInAmt    |   0   |
|    MktEndAfMnyOutAmt    |   0   |
|   MktEndAfSubstDsgnAmt  |   0   |
|   MktEndAfSubstAbndAmt  |   0   |
+-------------------------+-------+
선물옵션 잔고 조회
Field Count = 8
+-----------------+--------+
|       key       | value  |
+-----------------+--------+
|    TotBnsAmt    |   0    |
|    TotEvalAmt   |   0    |
|  TotEvalPnlAmt  |   0    |
|    TotErnrat    | 0.0000 |
|  ThdayRlzPnlAmt |   0    |
| EvalDpstgTotamt |   0    |
|    OrdAbleAmt   |   0    |
|     CmsnAmt     |   0    |
+-----------------+--------+
선물옵션 체결조회
'''
