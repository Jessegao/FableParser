"""the model
{
   "fables": {
     "short": [
      {
         "title": "the story's text here"
      },
      {
         "title": "the story's text here"
      },
      {
         "title": "the story's text here"
      }
    ],
   "long": [
     {
       "title": "the story's text here"
     }
    ]
   }
}
the rest of this was written by Jesse Gao, the guy that spent 20 min figuring out how to 
scan for a title
"""
#file name goes here
fname = "grimm10a.txt"
longStoryThreshold = 30
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

with open(fname) as f:
	lines = [line.rstrip('\n') for line in f]
	json = "{\"fairy tales\": "
	short = []
	lon = [] #cant write long
	#tracks title detection
	detected = False
	story = ""
	countNewLines = 0 #counts how many newlines for detecting titles
	countStoryLength #counts lines in story

	for line in lines:
		"""if detected and line:
			json += ("\"" + line.replace("\"", "'") +  "\"},\n")
			detected = False
		elif detectTitle(line):
			json += ("{\"" + line +  "\":")
			if line =="\n":
				pass
				detected = True"""
		if !line:
			countNewLines += 1
		elif line and countNewLines == 3 and is_number(line[0]):
			if story:
				story = "fairy tale number " story + "\""
				if countStoryLength < longStoryThreshold:
					short.append([story])
				else:
					lon.append([story])
				story = ""
			#is title
			story += ("\"" + line +  "\":\"")
		else:
			story += ("" + line.replace("\"", "'") +  "\n")

	json += "\"short\": ["
	for s in short:
		json += "{" + s + "},"
	json += "]"

	json += "\"long\": ["
	for s in lon:
		json += "{" + s + "},"
	json += "]"

	json += "\n}"
	file = open('fairyTales.json', 'w+')
	file.write(json)
	file.close()
	print("done!")