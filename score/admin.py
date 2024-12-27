# 선생님 계정 리스트업
def teacher_list(teach):
    print("="*60)
    print("선생님 계정")
    print("-"*60)
    for i in teach.keys():
        print(f"{teach[i]['id']} / {teach[i]['pw']}")
    print("="*60)
# 선생님 회원가입
def teacher_register():
    print("="*60)
    teacher_id = input("선생님 아이디를 입력 >> ")
    teacher_pw = input("선생님 비밀번호를 입력 >> ")
    print("-"*60)
    print("선생님 계정이 저장되었습니다.")
    print("="*60)
    return teacher_id,teacher_pw
# 변경된 선생님 아이디/비밀번호 텍스트 파일에 저장
def teach_put(teach):
    print("="*60)
    print(" ※ 선생님들의 계정을 저장하고 있습니다. ※ ")
    af = open("admin/list.txt", "w")
    for i in teach.keys():
        af.write("{}/{}\n".format(teach[i]['id'], teach[i]['pw']))
    af.close()
    print("-"*60)
    print("저장 완료")
    print("="*60)
def student_list(student):
    print("="*60)
    print("학생 리스트")
    print("-"*60)
    for i in student.keys():
        # 수정해야함
        if i.slice(0,3) == student[i]["학년"]+'-'+student[i]["반"]:
            print(f"{student[i]["학년"]}학년 {student[i]["반"]}반")
            for j in student.keys():
                if student[i]["학년"]+student[i]["반"] == student[j]["학년"]+student[j]["반"]:
                    print(f"{student[j]["번호"]}번 - {student[j]["이름"]}")
            print("-"*60)
        print("="*60)

# 관리자 첫 실행 영역
def main(teach,student):
    print("="*60)
    print(" ※ 관리자들이 관리하는 영역입니다. ※ ")
    print("-"*60)
    while True:
        print("1.교사 확인\t2.교사 입력\t3.학생 리스트\t0.나가기")
        print("-"*60)
        anum = input("입력 >> ")
        if anum == '1':
            teacher_list(teach)
        elif anum == '2':
            teach_add = teacher_register()
            teacher_info = {"id": teach_add[0], "pw": teach_add[1]}
            teach[teach_add[0]] = teacher_info
        elif anum == '3':
            student_list(student)
        elif anum == '0':
            teach_put(teach)
            break