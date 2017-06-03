class FileEdit(object):

	@classmethod
	def add(self,file,writee):
		with open(file, "a") as f:
			f.write(writee)
			f.write("\n")
  
	@classmethod
	def rewrite(self,file,writee):
		with open(file, "w") as f:
			f.write(writee)
			f.write("\n")

	@classmethod
	def read(self,file):
		with open(file, "r") as f:
			f.read(file)
