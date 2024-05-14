import asyncio
import dbopenapi
from app_keys import appkey, appsecretkey # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
로그인
토큰발급을 왜 1분 제한 주는지 모르겠음...
https://openapi.db-fi.com/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=9e3097ab-7d39-4433-8002-00649604f0de
2024.05.14
'''

async def main():
    
    api=dbopenapi.OpenApi()
    if not await api.login(appkey, appsecretkey): return print(f'연결실패: {api.last_message}')
    
    print('access_token: ', api.access_token)
    print('연결성공, 접속서버: ' + ('모의투자' if api.is_simulation else '실투자'))
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())

# Output:
'''
연결성공, 접속서버: 실투자
'''