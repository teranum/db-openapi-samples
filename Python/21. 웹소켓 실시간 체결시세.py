import asyncio
import dbopenapi
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
실시간 등록은 되는데, 체결시세 날라오지 않음. ()
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    api.on_message = on_message
    api.on_realtime = on_realtime
    # if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token): return print(f'연결실패: {api.last_message}')

    # 삼성전자 주식 실시간 시세 요청
    await api.add_realtime('S00', 'J '+'005930')
    
    # 10분후 실시간 시세 중지
    print('10분동안 실시간 작동중...');
    await asyncio.sleep(600)
    await api.remove_realtime('S00', 'J '+'005930')
    await asyncio.sleep(1)
    
    ... # 다른 작업 수행
    await api.close()
    

def on_message(api, msg:str): print(f'on_message: {msg}')

def on_realtime(api, trcode, key, realtimedata):
    if trcode == 'S00':
        print(f'체결시세: {trcode}, {key}, {realtimedata}')
    else:
        print(f'실시간: {trcode}, {key}, {realtimedata}')
        
asyncio.run(main())

# Output:
'''
10분동안 실시간 작동중...
on_message: S00(1): 정상처리되었습니다.
체결시세: S00, None, {'tr_key': ['J 005930']}

'''