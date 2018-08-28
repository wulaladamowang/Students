from students_tools import info_collection,save_to_mongo,is_exited,find_in_mongo,remove_mongo
#添加学生信息
def add_students():
	print('您选择了添加学生信息功能')	
	name,student_id,gender = info_collection()
	if is_exited(student_id):
		student={	
					'学号':student_id,
					'姓名':name,
					'性别':gender
				}
		save_to_mongo(student)
		print(student)
	else:
		print('学号已经存在')

def del_students():
	print('您选择了删除学生信息的功能')
	student_id = input('请输入要删除的学生学号：')
	if is_exited(student_id) == 0:
		infoes = find_in_mongo()
		for info in infoes:
			if student_id == info['学号']:
				print(info)
				print('是否确定删除该学生信息？')
				print('确认请按 1 ，取消请按 2 ')
				flag = 2
				while flag != 1:
					choose = int(input())
					if choose == 1:
						remove_mongo(info)
						flag = 1
					elif choose == 2:
						print('已经取消')
						flag = 1
					else:
						print('请重新选择')
						print('确认请按 1 ，取消请按 2 ')
						flag = 2
	else:
		print('没有该学号')
		






