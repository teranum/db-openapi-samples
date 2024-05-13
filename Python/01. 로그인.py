import asyncio
import dbopenapi
from app_keys import appkey, appsecretkey, access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def main():
    api=dbopenapi.OpenApi()
    if not await api.login(appkey, appsecretkey, access_token=access_token, enable_wss=False): return print(f'연결실패: {api.last_message}')
    print('연결성공, 접속서버: ' + ('모의투자' if api.is_simulation else '실투자'))
    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())
