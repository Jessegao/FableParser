"""the model
{
   "fables": {
     "short": [
      {
         "title": "title here",
         "text": "text here
      },
    ],
   "long": [
     {
         "title": "title here",
         "text": "text here
     }
    ]
   }
}
the rest of this was written by Jesse Gao, the guy that spent 20 min figuring out how to 
scan for a title
"""
import codecs
#file name goes here
name = input("Please type the name of the file to be scanned (without the .txt part): ")
#write-to file name goes here
newFile = name + ".json"
fname = name + ".txt"
longStoryThreshold = 2000
lineSpacing = 4 #this is the amount of line spacing between each story
#assumes that the main story comes after a title, so I will never scan an actual story
#the title doesnt have a period
def detectTitle(string):
	if not string:
		return False
	for c in reversed(string):
		if c == '.':
			return False
	return True
# credit: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open(fname, encoding = "utf8") as f:
	lines = [line.rstrip('\n') for line in f]
	json = "{\"fairy tales\": "
	short = []
	lon = [] #cant write long
	#tracks title detection
	detected = False
	story = []
	title = []
	countNewLines = 0 #counts how many newlines for detecting titles
	countStoryLength = 0 #counts lines in story
	s = "" #string that holds parts of the story

	for line in lines:
		"""if detected and line:
			json += ("\"" + line.replace("\"", "'") +  "\"},\n")
			detected = False
		elif detectTitle(line):
			json += ("{\"" + line +  "\":")
			if line =="\n":
				pass
				detected = True"""
		if not line:
			countNewLines += 1
			if countNewLines == lineSpacing and s:
				story.append(s)
				s = ""
		elif line and countNewLines == lineSpacing :
			"""if story:
				story = "fairy tale number " + story + "\""
				if countStoryLength < longStoryThreshold:
					short.append([story])
				else:
					lon.append([story])
				story = """
			#is title
			#story += ("\"title\": \"" + line.replace("\"", "'") +  "\":\"")
			title.append(line.replace("\"", "'"))
			countNewLines = 0
		else:
			s += line.replace("\"", "'") + " \n"
			countNewLines = 0

	"""json += "\"short\": ["
				for s in short:
					json += "{" + s + "},"
				json += "]"
			
				json += "\"long\": ["
				for s in lon:
					json += "{" + s + "},"
				json += "]"""

	if len(title) != len(story) :
		print("your list lengths don't match")

	for t, s in zip(title, story):
		formatted = "{\"title\": \"%s\",\"text\": \"%s\"},"%(t,s)
		if len(formatted) < longStoryThreshold:
			short.append(formatted)
		else:
			lon.append(formatted)

	print(str(len(lon)) + str(len(short)))

	json += "{\"short\": ["
	for s in short:
		json += s
	json += "]},"

	json += "{\"long\": ["
	for s in lon:
		json += s
	json += "]}"
	json += "\n}"

	file = codecs.open(newFile, 'w+', "utf-8")
	file.write(json)
	file.close()
	print("done!")