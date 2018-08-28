#mongo数据库
import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)
db = client['Students']
my_dbstd = db['students']
#输出所有mongo中的信息
def find_in_mongo():
	infoes = db.students.find()
	return infoes
#将信息存储在mongo中
def save_to_mongo(student):
	try:
		if db['students'].insert(student):
			print('存储到mongo成功')
	except:
		print('存储失败')
#将信息从mongo中删除
def remove_mongo(info):
	try:
		db.students.remove(info)
		print('已经删除')
	except:
		print('删除失败')
#修改mongo中学生信息 info:属性 value:修改之后的值
def change_mongo(student_id,info,value):
	try:
		my_dbstd.update({'学号':student_id},{'$set':{info:value}})
		print('更新成功')
	except:
		print('更新',info,'失败')
#检查学号是否存在
def is_exited(student_id):
	student_ids = []
	infoes = find_in_mongo()
	for info in infoes:
		student_ids.append(info['学号'])
	if student_id in student_ids:
		return 0
	else:
		return 1



