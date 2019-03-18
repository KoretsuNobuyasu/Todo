path = 'todo/todo.txt'
finish_path = 'todo/todo_finish.txt'

class Todo:
	def __init__(self, title):
		self.title = title
		with open(path) as f:
			while True:
				line = f.readline()
				line_ = line.split(',')
				if(title == line_[0]):
					self.status = line_[1]
					break
				else:
					self.status = False
				if not line:
					break
		
	def finish(self):
		self.status = True
		
	def retry(self):
		self.status = False

	
def show():
	label = ["_________ToDoリスト__________"]
	print('_________ToDoリスト__________')
	with open(path) as f:
		label.append(f.read())
		print(f.read())
	print('____________________________')
	label.append('____________________________')
	print('\n'*5)

	print('_______終了済みTodoリスト_______')
	label.append("_______終了済みTodoリスト_______")
	with open(finish_path) as f:
		print(f.read())
		label.append(f.read())
	print('______________________________')
	label.append('______________________________')
	return label
	
	
	
def choose_mode():
	print('choose mode')
	print('a = Add\nf = task finish\nr = retry')
	mode = input('choose mode =>')
	print(mode)
	if(mode == 'a'):
		print('add')
		return 'add'
	elif(mode == 'f'):
		print('choose finish task')
		return 'finish'
	elif(mode == 'r'):
		print('choose retry finish task')
		return 'retry'
	elif(mode == 'exit'):
		return 'exit'
	else:
		print('choose fuck you')
		
		
def add(task):
	print(task.title)
	info = '{},{},\n'.format(task.title, task.status)
	with open(path, mode='a+') as f:
		f.write(info)

def finish(task):
	"""If the task is done, store in another file"""
	print('in the finish function')
	data = []
	with open(path) as f:
		while True:
			line = f.readline()
			line_ = line.split(',')
			if(task.title == line_[0]):
				task.status = 'True'
			else:
				data.append(line)
			if not line:
				break
	
	info = '{},{},\n'.format(task.title, task.status)
	with open(path, mode='w') as f:
		for row in data:
			f.write(row)
	with open(finish_path, mode='a+') as f:
		f.write(info)

def retry(task):
	print('in the retry function')
	data = []
	with open(finish_path) as f:
		while True:
			line = f.readline()
			line_ = line.split(',')
			if(task.title == line_[0]):
				task.status = 'False'
			else:
				data.append(line)
			if not line:
				break
	
	info = '{},{},\n'.format(task.title, task.status)
	with open(finish_path, mode='w') as f:
		for row in data:
			f.write(row)
	with open(path, mode='a+') as f:
		f.write(info)
