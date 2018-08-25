# Importations
import random as r
from msvcrt import getch
# Chosing which function to run
#
#
def chooseFunction():
	while True:
		dataPull = open('Assets.txt','r').read()
		choice, x, y, z = dataPull.split('/')
		try:
			choice = int(choice)
			if choice == 1:
				return 1
			elif choice == 2:
				return 2
			elif choice == 3:
				return 3
			else:
				continue
		except:
			continue
#
# Need to run 1, 10, 100, 1000, 10k, 100k, 1m for each
#
# Defining the plotting
#
#
# Run random choice for a/b, all survive
#
def normal(popSize, genNumb):
	totString = ""
	writeString = ""
	dataPull = open('Assets.txt','r').read()
	x, y, probA, z = dataPull.split('/')
	probA = float(probA)
	probB = float(1 - probA)
	numberOfGenerations = 1
	k=0
	while numberOfGenerations <= int(genNumb):
		for j in range(round(2*popSize)):
			if r.random() < probA:
				totString = totString + "A"
			else:
				totString = totString + "B"
		totA = float(totString.count("A"))
		totB = float(totString.count("B"))
		probA = float(totA/(2*popSize))
		probB = float(totB/(2*popSize))
		if numberOfGenerations%10**k == 0:
			print(len(totString))
			print("Probability of dominant at " + str(numberOfGenerations) + " generation(s): " + str(probA))
			print("Probability of recessive " + str(numberOfGenerations) + " generation(s): " + str(probB))
			print("---------------------------------------------------------")
			k = k+1
		#
		# Writing to text doc
		#

		writeString = writeString + (str(probA) + '/' + str(probB) + '/' + str(numberOfGenerations) + '###')
		doc = open("APBioWriteDoc.txt",'w+')
		doc.write(writeString)

		doc2 = open("colorDepic.txt",'w')
		doc2.write(str(round(probA)) + '00' + str(round(probB)))
		
		numberOfGenerations = numberOfGenerations + 1
		totString = ""
	return 0
#
# BB die
#
def recessiveDisadvantage(popSize, genNumb):
	totString = ""
	writeString = ""
	dataPull = open('Assets.txt','r').read()
	x, y, probA, z = dataPull.split('/')
	probA = float(probA)
	probB = float(1 - probA)
	numberOfGenerations = 1
	k=0
	while numberOfGenerations <= int(genNumb):
		j=1
		while j <= popSize:
			if r.random() < probA:
				if r.random() < probA:
					totString = totString + "AA"
				else:
					totString = totString + "AB"
			else:
				if r.random() < probA:
					totString = totString + "AB"
				else:
					j = j - 1
			j = j+1
		totA = float(totString.count("A"))
		totB = float(totString.count("B"))
		probA = float(totA/(2*popSize))
		probB = float(totB/(2*popSize))
		if numberOfGenerations%10**k == 0:
			print(len(totString))
			print("Probability of dominant at " + str(numberOfGenerations) + " generation(s): " + str(probA))
			print("Probability of recessive " + str(numberOfGenerations) + " generation(s): " + str(probB))
			print("---------------------------------------------------------")
			k = k+1

		writeString = writeString + (str(probA) + '/' + str(probB) + '/' + str(numberOfGenerations) + '###')
		doc = open("APBioWriteDoc.txt",'w+')
		doc.write(writeString)

		numberOfGenerations = numberOfGenerations + 1
		totString = ""
	return 0
#
# AA 50% chance of survival, AB survive, BB die
#
def heteroAdvantage(popSize, genNumb):
	totString = ""
	writeString = ""
	dataPull = open('Assets.txt','r').read()
	x, y, probA, z = dataPull.split('/')
	probA = float(probA)
	probB = float(1 - probA)
	numberOfGenerations = 1
	k=0
	while numberOfGenerations <= int(genNumb):
		j=1
		while j <= popSize:
			if r.random() < probA:
				if r.random() < probA:
					if r.random() < .5:
						continue
					else:
						totString = totString + "AA"
				else:
					totString = totString + "AB"
			else:
				if r.random() < probA:
					totString = totString + "AB"
				else:
					j = j - 1
			j = j+1
		totA = float(totString.count("A"))
		totB = float(totString.count("B"))
		probA = float(totA/(2*popSize))
		probB = float(totB/(2*popSize))
		if numberOfGenerations%10**k == 0:
			print(len(totString))
			print("Probability of dominant at " + str(numberOfGenerations) + " generation(s): " + str(probA))
			print("Probability of recessive " + str(numberOfGenerations) + " generation(s): " + str(probB))
			print("---------------------------------------------------------")
			k = k+1
		writeString = writeString + (str(probA) + '/' + str(probB) + '/' + str(numberOfGenerations) + '###')
		doc = open("APBioWriteDoc.txt",'w+')
		doc.write(writeString)

		numberOfGenerations = numberOfGenerations + 1
		totString = ""
	return 0
#
#
#
#
#
#
# Blank space
for i in range(30):
	print("")
#
# Defining animations
#
def animate(i):
	pullData = open('APBioWriteDoc.txt', 'r').read()
	dataArray = pullData.split('aaa')
	print(dataArray)
	xar = []
	x2ar = []
	yar = []
	for line in dataArray:
		print(line)
		x, x2, y = line.split('/')
	ax1.clear()
	ax1.plot(xar, yar)
#
# Calling
#
choiceInput = chooseFunction()
pullData2 = open('Assets.txt', 'r').read()
x, popSize, y, GenNumbPulled = pullData2.split('/')
popSize = int(popSize)
if choiceInput == 1:
	normal(popSize, GenNumbPulled)
elif choiceInput ==2:
	recessiveDisadvantage(popSize, GenNumbPulled)
else:
	heteroAdvantage(popSize, GenNumbPulled)