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
		self.root = tkinter.Tk()
		self.root.title(u"Todoリスト")
		self.root.geometry("750x750")
		self.var = tkinter.StringVar()
		self.var.set('Mac OS Mojaveを使用している場合、windowをリサイズしないとボタン内の文字が読めません')
		tkinter.Label(textvariable=self.var).pack()
		label = show()
		for todo_label in label:
			static = tkinter.Label(text=todo_label)
			static.pack()
		frame = tkinter.Frame(self.root, bd=2, relief="ridge")
		frame.pack(fill="x")
		tkinter.Button(frame, bg='black', text=u"add", command=self.pushed_add).pack()
		tkinter.Button(frame, text="finish").pack()
		tkinter.Button(frame, text="retry").pack()
		tkinter.Button(frame, text="exit", command=self.root.destroy).pack()
		
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
		self.root.mainloop()
		
		return 0

	def pushed_add(self):
		tkinter.Label(self.root, text="pushed add").pack()
		self.var.set("変更")
		self.root.update()


if __name__ == "__main__":
	an_example = Example()
	import sys
	
	sys.exit(an_example.main())