# poemgen.py - Allison Nelson
# a simple poetry generator that makes "poems" based on parts of speech


nouns = []
nounfile = open("nounlist.txt")
for word in nounfile:
	nouns.append(word.rstrip('\n'))
	
verbs = ["feel","is","smell","touch","taste","smile","wave","run","live"]; #2
articles = ["the","a"]; #3
prepositions = ["on","with","under","in","to","into"]; #4
adjectives = ["beautiful","shining","slow","lovely","lively","nice","sad"]; #5
gerunds = ["leaping","growing","loving","shaking","making","living","being","thinking","doing","building","singing"]; #6
conjunctions = ["and","or"]; #7

#each number refers to a part of speech listed above, commas are interpreted literally, numbers in parentheses are optional
sentence_structures = ["35124351","314351","64351","63514351,676","3517351,6","6351,676","3512","3124351"];

from random import choice;
struct = choice(sentence_structures);

line = []

def parse_structs(structs):
	for i in range(0,len(struct)):
		curr = struct[i]
		if curr.isdigit():
			if curr == '1':
				line.append(choice(nouns));
			elif curr == '2':
				line.append(choice(verbs));
			elif curr == '3':
				line.append(choice(articles));
			elif curr == '4':
				line.append(choice(prepositions));
			elif curr == '5':
				line.append(choice(adjectives));
			elif curr == '6':
				line.append(choice(gerunds));
			elif curr == '7':
				line.append(choice(conjunctions));
			else:
				print "Invalid part of speech";
		else:
			curr = struct[i]
			if curr == ',':
				line.append(",");
	return line;

import sys
sys.stdout.write("\n");

for i in range(0,5):
	struct = choice(sentence_structures);
	line = [];
	line = parse_structs(sentence_structures);
	for i in range(0,len(line)):
		sys.stdout.write(line[i] + " ")
	sys.stdout.write("\n")
sys.stdout.write("\n")
	



