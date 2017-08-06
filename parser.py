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
#file name goes here
fname = "fab.mb.txt"
newFile = "fables.json"
longStoryThreshold = 2000
#assumes that the main story comes after a title, so I will never scan an actual story
#the title doesnt have a period
def detectTitle(string):
	if not string:
		return False
	for c in reversed(string):
		if c == '.':
			return False
	return True

with open(fname) as f:
	lines = [line.rstrip('\n') for line in f]
	json = "{\"fables\": "
	short = []
	lon = [] #cant write long
	story = [] #stores stories
	title = [] #stores titles
	#countNewLines = 0 #counts how many newlines for detecting titles
	#countStoryLength = 0 #counts lines in story
	#s = "" #string that holds parts of the story

	for line in lines:
		if detectTitle(line):
			title.append(line.replace("\"", "'"))
		else:
			story.append(line.replace("\"", "'"))

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

	file = open(newFile, 'w+')
	file.write(json)
	file.close()
	print("done!")