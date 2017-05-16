#This is a simple personality test.#

def determine_energy():
#Ask user if they are introverted or extraverted.#

	user_options = """
	\nWhen do you feel most energized?
	A. After getting much need alone time to rest or be instrospective
	B. After spending time with a big group of friends or at a fun event
	>>>"""

	user_input = raw_input(user_options)
	if user_input.upper() == "A":
		four_letters = four_letters.append("I")
		print "You might be introverted!"
	elif user_input.upper() == "B":
		four_letters = four_letters.append("E")
		print "You might be extraverted!"
	else:
		print "Not a valid entry. Choose either option A or B."

	return four_letters

def determine_information():
#Ask user if they are sensing or intuitive.#

	user_options = """
	\n When you are learning something for the first time, do you:
	A. Prefer to grasp the nitty gritty details of how each part might be connected
	B. Prefer to understand the big picture of what might be happening
	>>> """

	user_input = raw_input(user_options)
	if user_input.upper() == "A":
		four_letters = four_letters.append("S")
		print "You might be sensing!"

	elif user_input.upper() == "B":
		four_letters = four_letters.append("N")
		print "You might be intuitive!"
	else:
		print "Not a valid entry. Choose either option A or B."

def determine_decisions():
#Ask user if they are feeling or thinking.#

	user_options = """
	\n If you could only choose one, which option would you choose?
	A. To raise a child who is fair and just
	B. To raise a child who is kind and compassionate
	>>> """

	user_input = raw_input(user_options)
	if user_input.upper() == "A":
		four_letters = four_letters.append("T")
		print "You might be a thinker!"

	elif user_input.upper() == "B":
		four_letters = four_letters.append("F")
		print "You might be a feeler!"
	else:
		print "Not a valid entry. Choose either option A or B."

def determine_lifestyle(lifestyle):
#Ask user if they are perceiving or judging.#

	user_options = """
	\n When attending a conference or summer program, do you:
	A. Prefer to know the itinerary beforehand so you can plan for what exactly will take place
	B. Prefer to approach the schedule with spontaneity and figure things out as you go
	>>> """

	user_input = raw_input(user_options)
	if user_input.upper() == "A":
		four_letters = four_letters.append("J")
		print "You might be a judger!"
	elif user_input.upper() == "B":
		four_letters = four_letters.append("P")
		print "You might be a peceiver!"
	else:
		print "Not a valid entry. Choose either option A or B."

def define_personality(personality):
#Create dictionary that ties four letter key to personality type name and description value.#

	personality = {
		"INTJ": ["Architect.", "Your type has been described as imaginative and strategic thinkers, with a plan for everything."],
		"INTP": ["Logician.", "Your type has been described as innovative inventors with an unquencable thirst for knowledge."],
		"INFJ": ["Advocate.", "Your type has been described as quiet and mystical, yet very inspiring and tireless idealists."],
		"INFP": ["Mediator.", "Your type has been described as poetic, kind and altruistic people, always eager to help a good cause."],
		"ISTJ": ["Logistician.", "Your type has been described as practical and fact-minded individuals, whose reliability cannot be doubted."],
		"ISFJ": ["Defender.", "Your type has been described as very dedicated and warm protectors, always ready to defend their loved ones."],
		"ISTP": ["Virtuoso.", "Your type has been described as bold and practical experimenters, masters of all kinds of tools."],
		"ISFP": ["Adventurer.", "Your type has been described as flexible and charming artists, always ready to explore and experience something new."],
		"ESTP": ["Entrepreneur.", "Your type has been described as smart, energetic and very perceptive people, who truly enjoy living on the edge."],
		"ESFP": ["Entertainer.", "Your type has been described as spontaneous, energetic and enthusiastic people - life is never boring around them."],
		"ESTJ": ["Executive.", "Your type has been described as excellent administrators, unsurpassed at managing things - or people."],
		"ESFJ": ["Consul.", "Your type has been described as extraordinarily caring, social and popular people, always eager to help."],
		"ENFJ": ["Protagonist.", "Your type has been described as charismatic and inspiring leaders, able to mesmerize their listeners."],
		"ENFP": ["Campaigner.", "Your type has been described as enthusiastic, creative and sociable free spirits, who can always find a reason to smile."],
		"ENTJ": ["Commander.", "Your type has been described as bold, imaginative and strong-willed leaders, always finding a way - or making one."],
		"ENTP": ["Debater.", "Your type has been described as smart and curious thinkers who cannot resist an intellectual challenge."]
				}
	#keys = ["INTJ", "INTP",	"INFJ", "INFP", "ISTJ", "ISFJ", "ISTP", "ISFP", "ESTP", "ESFP", "ESTJ", "ESFJ", "ENFJ", "ENFP", "ENTJ", "ENTP"]
	#values = ["Architect", "Logician", "Advocate", "Mediator", "Logistician", "Defender", "Virtuoso", "Adventurer", "Entrepreneur", "Entertainer", "Executive", "Consul", "Protagonist", "Campaigner", "Commander", "Debater"]
	#personality = dict(keys,values)

def personality_reveal():
#Let the user know what personality type they match and how that type is described.#

	for key in personality:
		if str.join(four_letters) == key:
			print "Your personality type is the " + key + "! This type is known as the " + personality.key()

#Main code here.#

four_letters = [""] #Bug with four_letters. Tried adding it to function, but empty string would need to be added to every function. What do do??""
determine_energy()
determine_information()
determine_decisions()
determine_lifestyle()
define_personality()

