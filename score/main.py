import admin
import teacher
import score

#교사 정보 및 점수 저장
teach = {}
teach_nums = 0
af = open("admin/list.txt","r")
while True:
    teacher_info = {}
    teacher_line = af.readline()
    teacher_line = teacher_line.rstrip("\n")
    if teacher_line=="":
        break
    #line 변수에 있는 데이터들을 /로 나눠서 st_list에 배열 저장
    teacher_list = teacher_line.split("/")
    teacher_info["id"] = teacher_list[0]
    teacher_info["pw"] = teacher_list[1]
    teach[teacher_list[0]] = teacher_info
#학생 정보 및 점수 저장
student = {}
student_term = {}
sf = open("student/list.txt", "r")
while True:
    student_list = {}
    student_score = []
    # line 변수에 파일 한 줄씩 읽어오기
    line = sf.readline()
    # line 변수 속 \n(엔터) 제거
    line = line.rstrip("\n")
    # line이 빈 값이면 빠져나와라
    if line == "":
        break
    # line 변수에 있는 데이터들을 /로 나눠서 st_list에 배열 저장
    st_list = line.split("/")
    student_list["학년"] = st_list[0]  #학년
    student_list["반"] = st_list[1]  #반
    student_list["번호"] = st_list[2]  #번호
    student_list["이름"] = st_list[3]  #이름
    student_score.append(st_list[0])  #학년
    student_score.append(st_list[1])  #반
    student_score.append(st_list[2])  #번호
    student_score.append(st_list[3])  #이름
    student_score.append(st_list[4])  #국어
    student_score.append(st_list[5])  #수학
    student_score.append(st_list[6])  #영어
    student_score.append(st_list[7])  #종류
    student[st_list[0]+'-'+st_list[1]+'-'+st_list[2]] = student_list
    student_term[st_list[0]+'-'+st_list[1]+'-'+st_list[2]+'-'+st_list[6]] = student_score
#2,9,16
# menu 불러오기
while True:
    print(" ※ 실행할 메뉴를 선택하세요. ※ ")
    print("="*60)
    print("1.관리자\t2.교사 관리\t3.점수 관리\t9.종료")
    print("-"*60,end="\n")
    select_num = input('선택 >> ')

    #관리자(교사 등록)
    if select_num == '1':
        #tmp에 pay.py의 main 메서드 실행 값 저장
        admin.main(teach,student)

    #교사 관리(학생 등록 및 학생 점수)
    elif select_num == '2':
        teacher.main(teach,student_term)

    #점수 관리(학생 점수, 중간, 기말 총점, 평균)
    elif select_num == '3':
        score.main(student_term)

    # 프로그램 종료 전에 메모리에 있는 정보를 텍스트 파일로 저장
    elif select_num == '9':
        break
    else:
        print("다시 선택 하세요\n")
        print("-"*60)
print("="*60)
print("System down")
print("="*60)
