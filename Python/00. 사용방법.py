﻿'''
패키지 설치
pip install dbopenapi

(일부 샘플은 prettytable, padas, ta, matplotlib 패키지 필요)

dbopenapi 모듈사용
프로퍼티:
    connected -> bool: 연결여부 (연결: True, 미연결: False)
    is_simulation -> bool: 모의투자인지 여부 (모의투자: True, 실거래: False))
    access_token -> str: 접속토큰(로그인 성공시 설정됨, 당일 재 로그인에 이용가능)
    last_message -> str: 마지막 메시지
    mac_address -> str: MAC주소 (법인인 경우 필수 세팅)
    
메소드:
    login(appkey:str, appsecretkey:str,
                *, access_token:str=None, wss_domain:str=None
            ) -> bool: 로그인
        appkey:str - 앱키
        appsecretkey:str - 앱시크릿키
        * - access_token, wss_domain는 옵션(기본값으로 설정됨)
        access_token:str - 접속토큰 (재로그인시 사용가능), 기본값: None
        wss_domain:str - 웹소켓 주소 (해외선물옵션 경우 필수세팅 'wss://openapi.db-fi.com:7071/websocket'), 기본값: None
        reutrn: bool - 로그인 성공여부 (성공: True, 실패: False)
        
    request(tr_cd:str, data:dict, *, path:str=None, cont_yn:str='N', cont_key:str='0') -> None: 요청
        tr_cd:str - TR 코드
        data:dict - 요청 데이터
        * - path, cont_yn, cont_key는 옵션(기본값으로 설정됨)
        path:str - PATH경로, 기본값: None, 설정 필요시 URL값으로 세팅 ex) '/api/v1/trading/kr-stock/order'
        cont_yn:str - 연속조회여부 (연속조회: 'Y', 단순조회: 'N'), 기본값: 'N'
        cont_key:str - 연속조회키 (연속조회여부가 'Y'인 경우 필수 세팅), 기본값: '0'
        return: 응답 데이터 (dict), 요청 실패시 None

        * 국내선물옵션시세의 경우, 주식시세와 TR코드가 겹칠 시 앞에 'F'를 붙여서 사용 (ex. 'PRICE' -> 'FPRICE')
        (FCODES, FPRICE, FHOGA, FDAYTRADE, FCONCLUSION)
    
    add_realtime(tr_cd:str, tr_key:str) -> bool: 실시간 등록
        tr_cd:str - TR 코드
        tr_key:str - 키
        return: bool - 성공여부 (성공: True, 실패: False)
        
    remove_realtime(tr_cd:str, tr_key:str) -> bool: 실시간 해제
        tr_cd:str - TR 코드
        tr_key:str - 키
        return: bool - 성공여부 (성공: True, 실패: False)
        
    close() -> None: 연결 종료
        
이벤트:
    on_message(msg:str): 메시지 수신 이벤트 (오류 또는 웹소켓 끊김시 발생)
        msg - 메시지
        
    on_realtime(trcode:str, key:str, realtimedata:dict): 실시간 수신 이벤트 (실시간 데이터 수신시 발생)
        trcode:str - TR 코드
        key:str - 키
        realtimedata - 실시간 데이터
    
샘플 코드 이용
1. 샘플폴더에 app_keys.py 파일 생성
    app_keys.py 파일에 아래와 같이 변수 세팅
    appkey = '발급받은 앱Key'
    appsecretkey = '발급받은 앱 비밀Key'
    또는 샘플 01.로그인.py 실행결과로 출력된 access_token을 등록해 사용
        saved_access_token = '새로 발급받은 access_token'
        
2. 샘플코드 실행

01. 로그인.py 파일 실행 후 발급된 access_token을 app_keys.py 파일에 등록 (saved_access_token 변수에 세팅)
다음 샘플코드에서는 로그인시 access_token을 사용하여 로그인

01 ~ 로그인, 종목조회, 계좌조회
10 ~ 시세 및 차트조회
20 ~ 웹소켓 을 이용한 실시간 시세
30 ~ PyQt6를 이용한 GUI 샘플코드
40 ~ 기타 샘플코드


'''
