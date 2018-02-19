from sklearn import model_selection, svm, metrics

# CSV 파일을 읽어 들이고 가공하기
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            # , 문자로 배열화하여 첫번째열을 labels 데이터로 대입한다.
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))

            # 이미지 데이터의 각 픽셀은 0부터 255까지의 정수이기 때문에,
            # 이를 256으로 나누어서 0 이상이고, 1 미만인 실수 벡터로 대입한다.
            # map 내장 함수를 이용하여 모든 cols에 해당 lambda 함수를 실행한다.
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

# 학습하기
clf = svm.SVC()
clf.fit(data["images"], data["labels"])

# 예측하기
predict = clf.predict(test["images"])

# 결과 예측하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)

# 1000개를 학습시킨 경우 정답률이 78.6% 정도가 나오며, 모든 CSV 데이터를 학습시키면 정답률이 94% 정도 까지 오른다.
print("정답률 = ", ac_score)
print("<리포트>")
print(cl_report)
