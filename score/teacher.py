def main(teach,student):
    print("="*60)
    print(" ※ 선생님들이 관리하는 영역입니다. ※ ")
    print("-"*60)
    while True:
        teacher_id = input("계정 아이디를 입력해주세요.(나가려면 0번 입력) >> ")
        if teacher_id in teach.keys():
            teacher_pw = input("계정 비밀번호를 입력해주세요. >> ")
            if(teacher_pw == teach[teacher_id]['pw']):
                break
            else:
                print("비밀번호가 다릅니다.")
                continue
        else:
            print("계정 아이디를 다시 입력해주세요.")
            continue
        if teacher_id == '0':
            break
    while True:
        print("어떤 작업을 하시겠습니까?\n1.")
        tnum = input("입력 >> 1.학생 등록\t2.학생들 점수 보기")
        if tnum == '1':
            print("good")