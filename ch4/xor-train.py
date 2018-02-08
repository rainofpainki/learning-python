from sklearn import svm

# XOR의 계산 결과 데이터
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 학습을 위해 데이터와 레이블 분리하기
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    # data 리스트에는 "학습시키기 위한 데이터 변수"를 삽입한다.
    data.append([p, q])
    # label 리스트에는 "정답 레이블 변수"를 삽입한다.
    label.append(r)

# 데이터 학습시키기
clf = svm.SVC() # SVM 객체를 생성한다.
# fit 메서드를 이용해 데이터를 학습시킨다. 첫번째 매개변수로 학습할 데이터 배열을,
# 두번째 매개변수로 레이블 배열을 전달한다.
clf.fit(data, label)

# 데이터 예측하기
# 학습한 결과를 기반으로 데이터를 예측시킨다.
pre = clf.predict(data)
print("예측 결과 : ", pre)

# 결과 확인하기
ok = 0
total = 0

for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1
print("정답률 : ", ok, "/", total, " = ", (ok/total)*100, '%')

