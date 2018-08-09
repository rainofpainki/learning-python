import pandas as pd
import locale

def number_format(num, places=0):
    '''
    통화를 표시하기 위해 Comma를 삽입하여 반환한다.
    :param num:
    :param places:
    :return:
    '''
    return locale.format("%.*f", (places, num), True)


if __name__ == "__main__":
    # Pandas를 이용하여 파일을 불러온다.
    df = pd.read_csv("calc.txt", skiprows=1, delimiter="|", names=['date', 'point', 'cost'])

    # map 과 lambda를 이용하여 Comma를 제거한다.
    df['cost'] = df['cost'].map(lambda c: int(c.replace(',', '')))
    print("--합계--")

    # C 로케일의 숫자 형식 범주를 선택합니다.
    locale.setlocale(locale.LC_NUMERIC, '')

    sum = df['cost'].sum()
    print(number_format(sum))
