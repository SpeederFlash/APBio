from tkinter import *
from tkinter import font
import os
from sys import executable, exit
from subprocess import call, Popen, CREATE_NEW_CONSOLE

pruning = open("APBioWriteDoc.txt",'w').write("")
class Booter:

	def __init__(self, master):
		frame1 = Frame(master)
		frame1.pack(padx=20, pady=20)
		frame1_5 = Frame(master)
		frame1_5.pack()
		frame2 = Frame(master)
		frame2.pack()
		frame3 = Frame(master)
		frame3.pack()
		frame4 = Frame(master)
		frame4.pack()
		frame5 = Frame(master)
		frame5.pack()

		self.OpenGraph = Button(frame1, text='Open Grapher', command=self.openProg2)
		self.OpenGraph.pack(side=LEFT, padx=5)

		self.Simulator = Button(frame1, text='Start Simulation', command=self.openProg1)
		self.Simulator.pack(side=LEFT, padx=5)

		self.QuitButton = Button(frame1, text='Quit', command=self.Quitter)
		self.QuitButton.pack(side=LEFT, padx=5)

		self.ParamLabel = Label(frame1_5, text='Parameters')
		self.ParamLabel.pack(fill=X, pady=5)
		config = font.Font(self.ParamLabel, self.ParamLabel.cget('font'))
		config.configure(underline=True)
		self.ParamLabel.configure(font=config)

		self.Label1 = Label(frame2, text='Operation: ', justify=LEFT, width=15)
		self.Label1.pack(side=LEFT, padx=5, pady=5)

		global oper

		oper = Entry(frame2)
		oper.pack(fill=X, padx=5, pady=5)
		oper.delete(0,END)
		oper.insert(0, 1)

		self.Label2 = Label(frame3, text='Population Size: ', justify=LEFT, width=15)
		self.Label2.pack(side=LEFT, padx=5, pady=5)

		global pop

		pop = Entry(frame3)
		pop.pack(fill=X, padx=5, pady=5)
		pop.delete(0,END)
		pop.insert(0, 10000)

		self.Label3 = Label(frame4, text='Allele Frequency: ', justify=LEFT, width=15)
		self.Label3.pack(side=LEFT, padx=5, pady=5)

		global ratio

		ratio = Entry(frame4)
		ratio.pack(fill=X, padx=5, pady=5)
		ratio.delete(0,END)
		ratio.insert(0, float(0.5))

		self.Label4 = Label(frame5, text='Generations: ', justify=LEFT, width=15)
		self.Label4.pack(side=LEFT, padx=5, pady=5)

		global gener

		gener = Entry(frame5)
		gener.pack(fill=X, padx=5, pady=5)
		gener.delete(0,END)
		gener.insert(0, 1000000)
		

	def Quitter(self):
		os.system('taskkill /im python.exe')

	def openProg1(self):
		transfer1 = oper.get()
		transfer2 = pop.get()
		transfer3 = ratio.get()
		transfer4 = gener.get()
		open('Assets.txt', 'w').write(str(transfer1) + '/' + str(transfer2) + '/' + str(transfer3) + '/' + str(transfer4))
		Popen([executable, 'APBio.py'], creationflags=CREATE_NEW_CONSOLE)


	def openProg2(self):
		Popen([executable, 'APBioGrapher.py'], creationflags=CREATE_NEW_CONSOLE)

root = Tk()
root.geometry("400x400")
root.title('Booter')
runner = Booter(root)
root.mainloop()