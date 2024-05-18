import asyncio
import dbopenapi
from common import *
from app_keys import appkey, appsecretkey, saved_access_token # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

'''
없어요^^
API가이드에 해외선물옵션 종목마스터 조회 방법 없음...
2024.05.14
'''
async def main():
    api=dbopenapi.OpenApi()
    # if not await api.login(appkey, appsecretkey, wss_domain=dbopenapi.WSS_URL_GLOBAL): return print(f'연결실패: {api.last_message}')
    if not await api.login('', '', access_token=saved_access_token, wss_domain=dbopenapi.WSS_URL_GLOBAL): return print(f'연결실패: {api.last_message}')

    
    ... # 다른 작업 수행
    await api.close()

asyncio.run(main())


# Output:
