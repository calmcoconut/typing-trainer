import word_prompt, sys

USEROPTIONS = {"typing_length":"20"}

def main(argv):
	"""
	take user arguments on startup. if no argument, prompt the user to select basic settings
	"""
	if len(argv) > 1:
		parseFlags(argv[1:])
	else:
		promptOptions()
	# start program with option

def parseFlags(argv):
	for a in argv:
		if "$20" in a:
			words = "20"
		elif "$50" in a:
			words = "50"
		elif "$100" in a:
			words = "100"
		else:
			words = "20"
	USEROPTIONS["typing_length"] = words

def promptOptions():
	words = input("Welcome! please select an option:\n\ta.) 20 words\n\tb.)50 words\n\tc.) 50 words")
	if "a" in words:
		words = "$20"
	elif "b" in words:
		words = "$50"
	elif "c" in words:
		words = "$100"
	else:
		words = "$20"
	parseFlags([words])

if __name__ == "__main__":
	main(sys.argv)