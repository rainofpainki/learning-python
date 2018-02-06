import pandas as pd

# 엑셀 파일 열기
filename = "stat_104102.xls" # 파일 이름
sheet_name = "Sheet0" # 시트 이름
book = pd.read_excel(filename, sheet_name=sheet_name, header=2) # 첫번째 줄부터 헤더

# 2016년 인구로 정렬
book = book.sort_values(by='2016', ascending=False)

# 하지만 출력 결과에 정렬이 제대로 되지 않는다.
# 그 이유는 값을 쉼표가 있는 문자열로 인식하기 때문..
print(book)