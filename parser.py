"""the model
{  
   "fables": [  
      {  
         "title": "the story's text here"
      },
      {  
         "title": "the story's text here"
      },
      {  
         "title": "the story's text here"
      }
   ]
}
the rest of this was written by Jesse Gao, the guy that spent 20 min figuring out how to 
scan for a title
"""
#file name goes here
fname = "fab.mb"
#assumes that the main story comes after a title, so I will never scan an actual story
#the title doesnt have a period
def detectTitle(string):
	for c in reversed(string):
		if c == '.':
			return False
	return True

with open('filename') as f:
	lines = [line.rstrip('\n') for line in open('filename')]
	json = "{\"fables\": ["
	#tracks title detection
	detected = False
	for line in lines:
		if detected:
			json += ("\"" + line +  "\"}")
			detected = False
		elif detectTitle(line):
			json += ("{\"" + line +  "\":")
			detected = True
	json += "\n]\n}"
	file = open('fables.json', 'w+')
	file.write(json)
	file.close()