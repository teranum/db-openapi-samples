import asyncio
import dbopenapi
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
HTS에서 시세신청 후 요청^^ (HTS : [7325] 해외주식 실시간 시세 신청)
실시간 등록은 되는데, 체결시세 날라오지 않음. ()
2024.05.17
'''
async def main():
    api=dbopenapi.OpenApi()
    api.on_message = on_message
    api.on_realtime = on_realtime
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    종목코드 = input('종목코드를 입력하세요 (ex. AAPL): ')
 
    # 해외주식시세 실시간 요청
    if not await api.add_realtime('V60', 종목코드): print(f'실시간 등록 실패: {api.last_message}')
    
    # 10분후 실시간 시세 중지
    print('10분동안 실시간 작동중...');
    await asyncio.sleep(600)
    if not await api.remove_realtime('V60', 종목코드): print(f'실시간 중지 실패: {api.last_message}')
    await asyncio.sleep(1)
    
    ... # 다른 작업 수행
    await api.close()
    

def on_message(api, msg:str): print(f'on_message: {msg}')

def on_realtime(api, trcode, key, realtimedata):
    if trcode == 'V60':
        print(f'체결시세: {trcode}, {key}, {realtimedata}')
    else:
        print(f'실시간: {trcode}, {key}, {realtimedata}')
        
asyncio.run(main())

# Output:
'''
종목코드를 입력하세요 (ex. AAPL): AAPL
10분동안 실시간 작동중...
'''