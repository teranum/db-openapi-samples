import asyncio
import dbopenapi
from app_keys import appkey, appsecretkey # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
로그인
토큰발급은 1분에 1건으로 제한됨
https://openapi.db-fi.com/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=9e3097ab-7d39-4433-8002-00649604f0de
2024.05.14
'''

async def main():
    api=dbopenapi.OpenApi()
    
    logined:bool = False
    logined = await api.login(appkey, appsecretkey)
    
    # 옵션1: 당일 발급받은 access_token 이 있는 경우, access_token 으로 로그인
    # logined = await api.login('', '', access_token=saved__access_token)
    
    # 옵션2: 모의투자 일 경우 is_simulation 옵션을 True 로 설정
    # logined = await api.login(appkey, appsecretkey, is_simulation=True)
    
    # 옵션3: 해외선물옵션인 경우 wss_domain 옵션을 dbopenapi.WSS_URL_GLOBAL 로 설정
    # logined = await api.login(appkey, appsecretkey, wss_domain=dbopenapi.WSS_URL_GLOBAL)

    if not logined:
        print(f'연결실패: {api.last_message}')
        return
    
    print('연결성공, 접속서버: ' + ('모의투자' if api.is_simulation else '실투자'))
    
    # 발급된 access_token 출력
    print('access_token: ', api.access_token)
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())

# Output:
'''
연결성공, 접속서버: 실투자
'''