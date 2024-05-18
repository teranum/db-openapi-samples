from pandas import DataFrame
from prettytable import PrettyTable

def print_table(data):
    '''data를 표로 출력하는 함수'''
    if data is None:
        return
    if isinstance(data, dict):
        table = PrettyTable(['key','value'])
        fields = data.items()
        table.add_rows([list(x) for x in fields])
        print(f'Field Count = {len(fields)}')
        print(table)
    elif isinstance(data, list):
        if len(data) == 0:
            return
        if isinstance(data[0], dict):
            table = PrettyTable()
            table.field_names = data[0]
            table.add_rows([x.values() for x in data])
            print(f'Row Count = {len(data)}')
            print(table)
        else:
            table = PrettyTable(['value'])
            for x in data:
                table.add_row([x])
            print(f'Row Count = {len(data)}')
            print(table)
    elif isinstance(data, DataFrame):
        table = PrettyTable()
        table.field_names = data.columns
        table.add_rows(data.values)
        print(f'Row Count = {len(data)}')
        print(table)


def TOHLCV_to_csv(file_path, data):
    '''data를 csv로 저장하는 함수'''
    # 데이터프레임 생성
    df = DataFrame(data)
    # 컬럼명 변경
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    # 파일 저장
    df.to_csv(file_path, index=False, encoding='utf-8-sig')

def csv_to_TOHLCV(file_path):
    '''csv 파일을 데이터프레임으로 변환하는 함수'''
    # 파일 읽기
    df = DataFrame.from_csv(file_path, encoding='utf-8-sig')
    # 데이터프레임을 리스트로 변환
    data = df.values.tolist()
    return data

