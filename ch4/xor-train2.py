# pandas를 이용하여 데이터를 쉽게 분류한다
import pandas as pd
# metrics를 이용하여 정답률을 쉽게 구한다
from sklearn import svm, metrics

# XOR 연산
xor_input = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터를 분류하기
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:1] # 데이터 / 0에서 1번째 원소까지
xor_label = xor_df.ix[:,2] # 레이블 / 2번째 원소만

# 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(xor_data, xor_label) # 데이터를 학습한다
pre = clf.predict(xor_data) # 데이터를 예측한다

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", (ac_score*100), "%")