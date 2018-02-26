"""
언어 판별 프로그램

lang 디렉토리에 존재하는 학습 데이터 20개, 테스트 데이터 8개를 이용한다.
"""
from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어 들이고 출현 빈도 조사하기
def check_freq(fname):
    name = os.path.basename(fname)
    # 알파벳 소문자가 2회 이상 반복하는 값을 찾는다
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자로

    # 숫자 세기 변수(cnt) 초기화 / 0~25의 원소를 가진 List 생성
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a") # 문자를 아스키 코드 번호로 변환
    code_z = ord("z")

    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1

    # 정규화하기
    total = sum(cnt)
    # 알파벳의 출현 횟수를 글자수의 합계로 나누어 출현 횟수를 출현 빈도로 바꾼다.
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)

# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    # 해당 경로의 파일 목록을 가져온다.
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

# 학습용 데이터
data = load_files("./lang/train/*.txt")
# 테스트용 데이터
test = load_files("./lang/test/*.txt");
# JSON으로 결과 데이터 저장하기
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 예측하기
predict = clf.predict(test["freqs"])

# 결과 테스트하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 = ", ac_score)
print("[리포트]")
print(cl_report)