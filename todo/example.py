#! usr/bin/env python3
# -*- coding:utf-8 -*-

from .Todo import choose_mode
from .Todo import add
from .Todo import finish
from .Todo import retry
from .Todo import show
from .Todo import Todo
import tkinter

class Example(object):
	def main(self):
		root = tkinter.Tk()
		root.title(u"Todoリスト")
		root.geometry("750x750")
		tkinter.Label(text=u'Mac OS Mojaveを使用している場合、windowをリサイズしないとボタン内の文字が読めません').pack()
		label = show()
		for todo_label in label:
			static = tkinter.Label(text=todo_label)
			static.pack()
		frame = tkinter.Frame(root, bd=2, relief="ridge")
		frame.pack(fill="x")
		tkinter.Button(frame, bg='black', text=u"add").pack()
		tkinter.Button(frame, text="finish").pack()
		tkinter.Button(frame, text="retry").pack()
		tkinter.Button(frame, text="exit", command=root.destroy).pack()
		
		while True:	
			
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
		#root.mainloop()
		
		return 0

if __name__ == "__main__":
	an_example = Example()
	import sys
	
	sys.exit(an_example.main())