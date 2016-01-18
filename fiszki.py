#!/bin/python
from random import randint
import random
import sys
import os

f	=	open(sys.argv[1], 'r')
tab	=	[]
correct	=	0
rest	=	0
all	=	0

os.system("clear")

for line in f:
	if line.find(':') != -1:
		ang	=	line.split(':')[0]
		pol	=	line.split(':')[1][:-1]
		count	=	0
		rest	=	rest + 1
		tab.append([ang, pol, count, 0])

random.shuffle(tab)

while len(tab) > 0:

	nr	=	randint(0, min(10, len(tab) - 1))
	ang	=	tab[nr][0]
	pol	=	tab[nr][1]
	count	=	tab[nr][2]

	print pol + " (" + str(count) + ")"

	answer = raw_input().rstrip()

	os.system("clear")


	if answer == ang:
		correct = correct + 1
		tab[nr][2] = count + 1
		rest = rest - 1

		if tab[nr][3] == 0 or tab[nr][2] == 3:
			tab.remove(tab[nr])
	else:
		
		tab[nr][3] = 1
		if len(answer) > 0:
			print answer
		print ang + " = " + pol
	all = all + 1
	print "Correct " + str((correct * 100) / all) + "% (" + str(rest) + " rest)"
