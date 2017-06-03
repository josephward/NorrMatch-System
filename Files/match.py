def ch_checks():
	checks += 1
	print "Check One:   True  [T]"

def ch_idlist():
	if isinstance(idlist, list) == False:
		checks += 1
	print "Check Two:  ", isinstance(idlist, list), "[F]"
	
def ch_idlist2():
	if isinstance(uselist, str) == True:
		checks += 1
	print "Check Three:", isinstance(uselist, str), " [T]"

def initialize():
	filelist=["storematch.txt","storeteam.txt"]
	for x in filelist:
		if os.path.exists(x):		
			#collapse empty lines
			with open(x, "rU") as f:
				for line in f:
					line.rstrip('\n')
		else:
			con.rewrite(x,'')
	#Special Case for Storelist Startup
	if os.path.exists("storelist.txt"):
		if os.stat("storelist.txt").st_size == 0:
			con.rewrite("storelist.txt","[0]")
	else:
		con.rewrite("storelist.txt","[0]")


def startupchecks():
	#Setup for Checks
	checks = 0
	print "="*20
	
	#checks
	##Ch_Checks
	checks += 1
	print "Check One:   True  [T]"
	##Ch_Idlist
	if isinstance(uselist, list) == False:
		checks += 1
	print "Check Two:  ", isinstance(uselist, list), "[F]"
	##Ch_Idlist2
	if isinstance(uselist, str) == True:
		checks += 1
	print "Check Three:", isinstance(uselist, str), " [T]"

	
	with open("startup.py") as f:
		tree = ast.parse(f.read())
		numbchecks = sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)	
	#Finish Setup
	print "-"*20,"\nSystem Status: {0}/{1}".format(checks, numbchecks) 
	#Change the second number to match number of checks
	print "="*20,"\nReady For Boot"


	

print "Initizalizing...\n"
initialize()
startupchecks()
initialize()
print "\nStartup finished, begin program"

"""
-----------------------BODY CODE--------------------------
"""

#Match ID system 
class NorrMatch(object):
	def __init__(self,matchID,team1,team2,matchname='Unnamed'):
		self.matchID  	= matchID
		self.team1    	= team1
		self.team2    	= team2
		self.matchname  = matchname

	@classmethod
	def creatematch(self,matchname='Unnamed'):
		#Creates new ID in idlist
		with open("storelist.txt", "r") as f:
			uselist = f.read().replace('\n', '').replace('[', '').replace(']', '').replace(',', '')
			#Uselist is a String	
		uselist = map(int, uselist.split())
		listnumb = uselist[-1]
		listnumb += 1
		#Maps uselist to a list
		uselist.append(listnumb)
		expandnumb = '%04d' % listnumb
		#Creates new NorrMatch instance from new ID
		classbegin = 'ID'+'%s' % expandnumb
		newidclass = "{0} = NorrMatch('{1}','team1','team2','{2}')".format(classbegin, expandnumb, matchname)
		with open("storematch.txt", "a") as f:
			f.write(newidclass)
			f.write("\n")
		if "idlist =" not in uselist:
			idlist = "{0}".format(uselist)
		else: 
			idlist = uselist
		with open("storelist.txt", "w") as f:
			f.write(idlist)
			f.write("\n")

		#Prints the new ID to confirm success

		print "Match ID created:",
		print '%04d' % listnumb 
   
#Team ID system
class NorrTeam(object):
	def __init__(self):
		self.name   = name
		self.goals  = goals
  
	@classmethod
	def newteam(self):
		#inputs
		teamid    = raw_input("Enter a team identifier: ").lower()
		teamname  = raw_input("Enter the team's official name: ")
		teamgoals = 0

		#team class creation
		teamclass = "{0} = NorrTeam('{1}','{2}')".format(teamid, teamname, teamgoals)
		write.append("storeteam.txt",teamclass)

		#confermation
		print "Norrland Team created: ",teamname
    
""" TESTING """

def severalIDs(x=10):
	#meant to test the storematch file system, generates x classes of IDs
	while x > 0:
		NorrMatch.creatematch()
		x -= 1
    
    
""" Startup Procedures"""
def initialize():
	filelist=["storematch.txt","storelist.txt","storeteam.txt"]
	for x in filelist:
		if x == "storelist.txt":
			#Check if file is empty
			if os.stat("storelist.txt").st_size == 0:
				#If it is, write 0
				with open(x, "w") as f:
					f.write('[0]')
			else: 
				continue
		else:		
			#collapse empty lines
			with open(x, "rU") as f:
				for line in f:
					line.rstrip('\n')
	with open("storelist.txt", 'r') as f:
		listID = f.readlines()
		print listID
	#listID = [x.strip() for x in listID]

if __name__ == '__main__':
	print "Initizalizing..."
	initialize()
	print "Startup finished"
