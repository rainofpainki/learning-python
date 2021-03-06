import struct

# 파일명와 개수를 인자로 지정한다.
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/"+name+".csv", "w", encoding="utf-8")

    # 헤더 정보 읽기
    # struct 모듈로 리틀 에디안 데이터를 읽을 때는 ">" 기호를 지정한다.
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    # 이미지 데이터를 읽고 CSV로 저장하기
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            # 글자 파일로 이미지를 나타낼 수 있게 pgm 포맷으로 저장한다.
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)

    csv_f.close()
    lbl_f.close()
    img_f.close()

# 결과를 파일로 출력하기
to_csv("train", 1000)
to_csv("t10k", 500)

