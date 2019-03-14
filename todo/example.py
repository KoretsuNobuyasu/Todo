#! usr/bin/env python3
# -*- coding:utf-8 -*-

from .Todo import choose_mode
from .Todo import add
from .Todo import finish
from .Todo import retry
from .Todo import show
from .Todo import Todo

class Example(object):
	def main(self):
		while True:
			show()
			mode = choose_mode()
			if(mode == 'exit'):
				print('break break break !!!')
				break
			else:
				title = str(input('enter the title =>'))
				task = Todo(title)
				if(mode == 'add'):
					add(task)
				elif(mode == 'finish'):
					finish(task)
				elif(mode == 'retry'):
					retry(task)
				else:
					pass
		return 0

if __name__ == "__main__":
	an_example = Example()
	import sys
	sys.exit(an_example.main())