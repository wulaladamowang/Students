from students import Student

def showInfo():
	print('-'*30)
	print('       学生管理系统        v1.0')
	print('1、添加学生信息')
	print('2、删除学生信息')
	print('3、修改学生信息')
	print('4、查询学生信息')
	print('5、遍历学生信息')
	print('6、退出系统')
	print('-'*30)


def main():
	student = Student()
	showInfo()
	while True:
		key = int(input("请选择功能（序号）"))
		if key == 1:
			student.add_student()
		if key == 2:
			student.del_student()
		if key == 3:
			student.change_student()
		if key == 4:
			student.refer_student()
		if key == 5:
			student.all_students()
		if key == 6:
			break

main()