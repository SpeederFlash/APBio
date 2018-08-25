# Grapher
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(2,1,2)
ax2 = fig.add_subplot(2,1,1)

plt.axis([0,1000000,0,1])

def anitmate(i):
	extract = open("APBioWriteDoc.txt",'r').read()
	dataArray = extract.split('###')
	yar = []
	y2ar = []
	xar = []
	for line in dataArray:
		if len(line)>1:
			x, x2, y = line.split('/')
			yar.append(float(x))
			y2ar.append(float(x2))
			xar.append(float(y))
	
	ax1.clear()
	ax2.clear()
	plt.subplot(212)
	plt.xlabel('Generations ')
	plt.ylabel('Allele frequency (Dominant)')
	plt.subplot(211)
	plt.xlabel('Generations  ')
	plt.ylabel('Allele frequency (Recess')
	ax1.plot(xar, yar)
	ax2.plot(xar, y2ar, color='red')
	
plt.subplots_adjust(hspace=.5)
ani = animation.FuncAnimation(fig,anitmate, interval=10)
plt.show()