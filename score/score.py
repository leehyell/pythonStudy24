def middle_score(student):
    print("번호\t이름\t국어\t수학\t영어\t총점\t평균")
    for i in student:
        snum = student[i]["번호"]
        name = student[i]["이름"]
        kor = student[i]["국어"]
        math = student[i]["수학"]
        eng = student[i]["영어"]
        tot = kor + math + eng
        avg = float(tot / 3)
        kind = student[i]["종류"]
        print(f"{snum}\t{name}\t{kor}\t{math}\t{eng}\t{tot}\t{avg}\t{kind}")

def main(student):
    print("학생들의 점수를 리스트업, 관리하는 영역입니다.")
    print(student)
    while True:
        print(("1.중간고사 점수\t2.기말고사 점수\t3.중간+기말\t0.나가기"))
        score_num = input("입력 >> ")
        if score_num == '1':
            middle_score(student["종류"])
        elif score_num == '0':
            break