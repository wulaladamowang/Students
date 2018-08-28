from students_tools import is_exited,save_to_mongo,remove_mongo,find_in_mongo,change_mongo

class Student():
	#初始化学生信息
	def __init__(self):
		self.__name = ''
		self.__student_id = ''
		self.__gender = ''

	def add_student(self):
		print('您选择了添加学生信息功能')
		self.__name = input('请输入学生姓名')
		self.__student_id = input('请输入学生学号：')
		self.__gender = input('请输入性别：')
		if is_exited(self.__student_id):
			student={	
						'学号':self.__student_id,
						'姓名':self.__name,
						'性别':self.__gender
					}
			save_to_mongo(student)
			print(student)
		else:
			print('学号已经存在')

	def del_student(self):
		print('您选择了删除学生信息的功能')
		self.__student_id = input('请输入要删除的学生学号：')
		if is_exited(self.__student_id) == 0:
			infoes = find_in_mongo()
			for info in infoes:
				if self.__student_id == info['学号']:
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

	def change_student(self):
		print('您选择了修改学生信息的功能')
		self.__student_id = input('请输入要修改的学生的学号')
		if is_exited(self.__student_id) == 0:
			infoes = find_in_mongo()
			for info in infoes:
				if self.__student_id == info['学号']:
					print(info)
					print('是否确定修改该学生信息？')
					print('确认请按 1 ，取消请按 2 ')
					flag = 2
					while flag != 1:
						choose = int(input())
						if choose == 1:
							try:
								item = input('请输入要修改的学生的属性\n （输入 1 ,修改姓名，输入 2 ，修改性别）\n ')
								if int(item) == 1:
									value = input('请输入姓名：')
									change_mongo(self.__student_id,'姓名',value)
								elif int(item) == 2:
									value = input('请输入性别：')
									change_mongo(self.__student_id,'性别',value)
								else:
									print('输入有误')
							except:
								print('输入有误')
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

			
	def refer_student(self):
		print('你选择了查询学生信息的功能。')
		self.__student_id = input('请输入学号信息：')
		if is_exited(self.__student_id) == 0:
			infoes = find_in_mongo()
			for info in infoes:
				if self.__student_id == info['学号']:
					print('姓名:',info['姓名'])
					print('学号:',info['学号'])
					print('性别:',info['性别'])
		else:
			print('没有学号: %s 的信息'%self.__student_id)

	def all_students(self):
		print('你选择了遍历学生信息的功能')
		infoes = find_in_mongo()
		for info in infoes:
			print('姓名:%3s 学号:%9s 性别:%1s'%(info['姓名'],info['学号'],info['性别']))
			#print('姓名:',info['姓名'],'  学号:',info['学号'],'  性别:',info['性别'])
			
			



