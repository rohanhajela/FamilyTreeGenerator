class Person:
	def __init__(self, name, linkedin, cohort, family, parent, head):
		self.name = name
		self.linkedin = linkedin
		self.cohort = cohort
		self.family = family
		self.parent = parent
		self.children = []
		self.head = bool(int(head))

	def getName(self):
		if self.isHead():
			return "👑" + self.name
		else:
			return self.name

	def getLinkedin(self):
		return self.linkedin

	def getCohort(self):
		return self.cohort

	def getFamily(self):
		return self.family

	def getParent(self):
		return self.parent

	def getParentName(self):
		if self.parent is None:
			return None
		else:
			return self.parent.getName()

	def isHead(self):
		return self.head

	def hasChildren(self):
		return len(self.children) != 0

	def getChildren(self):
		return self.children

	def addChild(self, person):
		self.children.append(person)

	def __str__(self):
		return str(self.name) + "," + str(self.linkedin) + "," + str(self.cohort) + "," + str(self.family) + "," + str(self.getParentName())

#read family info
f = open("family.txt","r")

people = {}

origin = None

for line in f.readlines():
	line = line.rstrip().split(",")
	curPerson = line[0]
	curLinkedin = line[1]
	curCohort = line[2]
	curFam = line[3]
	curParent = line[4]
	curHead = line[5]

	if curParent == "None":
		cur = Person(curPerson, curLinkedin, curCohort, curFam, None, curHead)
		origin = cur
	else:
		cur = Person(curPerson, curLinkedin, curCohort, curFam, people[curParent], curHead)
		people[curParent].addChild(cur)

	people[curPerson] = cur

f.close()


def printFamily(person, tabs, output):

	color = "CEA00F"
	if (person.getFamily() == "FUEGO"):
		color = "F30000"
	elif (person.getFamily() == "VIZ"):
		color = "0009b3"
	elif (person.getFamily() == "PLAY"):
		color = "086e02"
	elif (person.getFamily() == "LIT"):
		color = "ffe226"

	output.write(tabs + "<a style=\"--b: 2px solid #" + color + "\" href=\"" + person.getLinkedin() + "\">" + "<font color=\"black\">" + "<b>" + person.getName() + "</b>" + "<br>" + "<i>" + person.getCohort() + "</i>" + "</font></a>\n")
	if(person.hasChildren()):
		output.write(tabs +  "<ul>\n")
		for child in person.children:
			output.write(tabs + "\t<li>\n")
			printFamily(child, "\t\t" + tabs, output)
			output.write(tabs + "\t</li>\n")
		output.write(tabs + "</ul>\n")		


def createTree(person, output):
	output.write("<div class=\"scrollmenu\">")
	output.write("<div class=\"tree\" style=\"width:1600px\">\n")
	output.write("\t<ul>\n")
	output.write("\t\t<li>\n")




	printFamily(person, "\t\t\t", output)
	output.write("\t\t</li>\n")
	output.write("\t</ul>\n")
	output.write("</div>\n")
	output.write("</div>\n")

def insertHTMLStyle(output):
	f = open("style.html","r")
	for line in f.readlines():
		output.write(line.rstrip() + "\n")
	f.close()

output = open("output.txt","w")



insertHTMLStyle(output)
createTree(people["Fuego Fam"], output)
createTree(people["Vizionaries"], output)
createTree(people["Playmakers"], output)
createTree(people["Lituation"], output)
#createTree(origin, output)

output.close()
