def my_student_info_list(student_info):
    print("****************************")
    print("* 학생이름:", student_info[0])
    print("* 학급번호:", student_info[1])
    print("* 전화번호:", student_info[2])
    print("****************************")


student1_info = ["현아", "01", "010-1231-1222"]
my_student_info_list(student1_info)

my_student_info_list(["수리", "02", "010-2222-3434"])