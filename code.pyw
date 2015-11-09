#
# All coordinates assume a screen resolution of 1280x1024, and Firefox
# maximized with the Bookmarks Toolbar disabled.
#
# For the image grab function
import ImageGrab, os
from time import time, sleep
# For the mousing around function
import win32api, win32con
# For random number generation
import random
from random import randint
import webbrowser
from subprocess import Popen
import time
import pyscreenshot as ImageGrab

# ---Globals---
# Number of Categories
NUM_OF_CATEGORIES = 15
NUM_OF_ADDITIONAL_CATEGORIES = 11
# top left corner of the screen
xCo = 78
yCo = 0
# to bottom right corner of the screen
xDif = 919
yDif = 1078
		# list of coordinate positions
		# format :  0  1  2
		#           3  4  5
		#           6  7  8
		#           9  10 11
		#           12 13 14
		#           15 16 17
pos = [(314, 361), (585, 361), (854, 361),
	   (314, 614), (585, 614), (854, 614),
	   (314, 870), (585, 870), (854, 870),
	   (314, 764), (585, 764), (854, 764),
	   (314, 1020), (585, 1020), (854, 1020),
	   (314, 1030), (585, 1030), (854, 1030)]


class Video():
	def __init__(self, cord, time, name):
		self.cord = cord
		self.time = time
		self.done = False
		self.name = name
		self.screenDown = Video.setScreenDown(self)
	@property
	def isVideoDone(self):
		return self.done
	@property
	def returnCord(self):
		return self.cord
	@property
	def returnTime(self):
		return self.time
	@property
	def returnName(self):
		return self.name
	def setScreenDown(self):
		if (self.cord == pos[9] or self.cord == pos[10] or self.cord == pos[11] or self.cord == pos[12] or self.cord == pos[13] or self.cord == pos[14]):
			return 1
		elif(self.cord == pos[15] or  self.cord == pos[16] or self.cord == pos[17]):
			return 2
		else:
			return 0
	def watchingVideo(self):
		print("watching: " + self.name)
	def videoDone(self):
		self.done = True
		print("done")
	def watchTheVideo(self, videoCategory):
		self.watchingVideo()

		watchVideoAndReturn(self.cord, self.time,videoCategory.returnCategoryPos, self.screenDown)
		self.videoDone()
	#def nextVideo(self):

class Cord:

	# Web browser
	back = (16, 60)
	screenRight = (888, 1071)
	screenLeft = (9, 1070)
	screenUp = (912, 92)
	screenDown = (912, 1053)
	soundOff = (859, 66)
	closeTab = (207, 32)
	closeFireFox = (897, 16)
	firefoxCrash = (373, 568)

	# change video quality
	HDButton = (876, 699)  # screen is one click to the right
	lowestVideoQuality = (870, 574)  # screen is one click to the right

	# Categories
	catShowMore = (31, 814)
	catCareers = "http://www.swagbucks.com/watch/playlists/1/careers"
	catComedy = "http://www.swagbucks.com/watch/playlists/457/comedy"
	catEntertainment = "http://www.swagbucks.com/watch/playlists/133/entertainment"
	catFashion = "http://www.swagbucks.com/watch/playlists/98/fashion"
	catFitness = "http://www.swagbucks.com/watch/playlists/101/fitness"
	catFood = "http://www.swagbucks.com/watch/playlists/101/fitness"
	catHealth = "http://www.swagbucks.com/watch/playlists/4/health"
	catHobbies = "http://www.swagbucks.com/watch/playlists/650/hobbies"
	catHomeAndGarden = "http://www.swagbucks.com/watch/playlists/12/home-garden"
	catMusic = "http://www.swagbucks.com/watch/playlists/447/music"
	catNewsAndPolitics = "http://www.swagbucks.com/watch/playlists/333/news-politics"
	catParenting = "http://www.swagbucks.com/watch/playlists/138/parenting"
	catPersonalFinance = "http://www.swagbucks.com/watch/playlists/1999/personal-finance"
	catPetsAndAnimals = "http://www.swagbucks.com/watch/playlists/91/pets-animals"
	catShopping = "http://www.swagbucks.com/watch/playlists/692/shopping"
	catSports = "http://www.swagbucks.com/watch/playlists/17/sports"
	catTechnology = "http://www.swagbucks.com/watch/playlists/22/technology"
	catTravel = "http://www.swagbucks.com/watch/playlists/129/travel"
	catWedding = "http://www.swagbucks.com/watch/playlists/120/wedding"

class Category():
	def __init__(self, categoryName, category, tuple):
		self.totalVideos = len(tuple)
		self.category = categoryName
		self.categoryPos = category
		self.watchedVideos = 0
		self.categoryFinished = False
		self.videos = tuple
	@property
	def exposeVideos(self):
		return self.videos
	@property
	def isCategoryFinished(self):
		return self.categoryFinished
	@property
	def returnCategory(self):
		return self.category
	@property
	def returnTotalVideos(self):
		return self.totalVideos
	def returnCategoryPos(self):
		return self.categoryPos
	def categoryIsFinished(self):
		self.categoryFinished = True
		mousePos(Cord.closeFireFox)
		leftClick()
		mousePos(Cord.firefoxCrash)
		leftClick()
		webbrowser.get("firefox").open("www.swagbucks.com")
		sleep(3)
		mousePos(Cord.soundOff)
		leftClick()
		leftClick()
	def returnWatchedVideos(self):
		return self.watchedVideos
	def goToClassCategory(self):
		webbrowser.get("firefox").open_new_tab(self.categoryPos)
		sleep(3)


def screenGrab():
	box = ()
	im = ImageGrab.grab()
	im.save(os.getcwd() + '\\full_snap__' + str(int(time())) + '.png', 'PNG')

#Function: mouse down for .1s then mouse up.
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#Function: mouse down for at least .1s
def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	sleep(.1)

#Function: mouse up and nothing for .1s
def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	sleep(.1)

#Function: set mouse position to the given mouse coordinates
#Arguements: string - coordinates format:
def mousePos(cord):
	win32api.SetCursorPos((xCo + cord[0], yCo + cord[1]))

#Function: gets the mouse's current coordinates and prints them
def getCords():
	x, y = win32api.GetCursorPos()
	x = x - xCo
	y = y - yCo
	print x, y

#Function: Set the web page to the top left corner
def resetWindow():
	mousePos(Cord.screenLeft)
	sleep(3)
	leftClick()
	leftClick()
	leftClick()
	mousePos(Cord.screenUp)
	sleep(3)
	leftClick()
	leftClick()
	leftClick()

#Function: Perform video watching operation and set the web client back to the watch page
def watchVideoAndReturn(cord, time, category, screenDown):
	# if the video isn't currently visible, scroll down then proceed
	if screenDown == 1:
		mousePos(Cord.screenDown)
		leftClick()
		leftClick()
		leftClick()
		leftClick()
		leftClick()
		leftClick()
	elif screenDown == 2:
		mousePos(Cord.screenDown)
		for i in range (0,10):
			leftClick()
		sleep(3)
	# Click on the video and let the page load
	mousePos(Cord.back)
	sleep(3)
	mousePos(cord)
	leftClick()
	sleep(3)

	#    # Set the quality to minimum
	#    mousePos(Cord.screenRight)
	#    leftClick()
	#    mousePos(Cord.HDButton)
	#    mousePos(Cord.lowestVideoQuality)
	#    leftClick()

	# Sleep until the video is over + 50s buffer, return to the video page
	#sleep(3)
	sleep(time + 30)
	# close the last tab in the list
	mousePos(Cord.closeTab)
	sleep(1)
	leftClick()
	sleep(2)
	mousePos(Cord.back)

def watchCategory(totalClassVideos,videoCategory, tuple):
	watchedClassVideos = 0

	while watchedClassVideos < totalClassVideos:
		upperBound = totalClassVideos - 1
		i = random.randint(0, upperBound)
		if tuple[i].isVideoDone == True:
			i = 0
			while tuple[i].isVideoDone == True:
				if i >= totalClassVideos:
					break
				else:
					if i >= upperBound:
						break
					i += 1



		if tuple[i].isVideoDone == False:
			videoCategory.goToClassCategory()
			tuple[i].watchTheVideo(videoCategory)
			watchedClassVideos += 1

#Function: Once in watch section, go through each category and call their watch each video
def goToCategories():
	sleep (5)
	resetWindow()
	mousePos(Cord.catShowMore)
	leftClick()

		# list of coordinate positions
		# format :  0  1  2
		#           3  4  5
		#           6  7  8
		#           9  10 11
		#           12 13 14
		#           15 16 17
	car = (	Video(pos[1], 230, "the life of a janitor"),
			Video(pos[4], 230, "consider fishing"),
			Video(pos[5], 260, "odd student situations"),
			Video(pos[6], 230, "marketing your business"),
	        Video(pos[14], 260, "amazingAccomplishments"))

	aCar = ( Video(pos[2], 330, "It's the worlds oldest profession"),
	         Video(pos[3], 400, "Be a firefighter"),
	         Video(pos[7], 330, "school dinners are hit and miss"),
	         Video(pos[15], 620, "stealing gets you nowhere"))

	com = ( Video(pos[5], 380, "top 10 fun facts - comedians"),
			Video(pos[2], 500, "some burglars are extra stupid"),
			Video(pos[7], 575, "comedy time 4"),
			Video(pos[8], 620, "comedy time 3"),
			Video(pos[9], 450, "comedy time 2"),
			Video(pos[10], 450, "comedy time 1"),
			Video(pos[11], 230, "marijuana gets hidden in odds places"))
	#aCom = ( Video(pos[4], 230, ""))

	fas = ( Video(pos[15], 145, "buying shoes is never straightforward"),
			Video(pos[14], 315, "got your valentines day lingerie"))
	aFas = (Video(pos[7], 330, "women's style in mimi ..."),
	        Video(pos[9], 400, "get your handbag"),
	        Video(pos[10], 410, "are you wearing your bra correctly?"),
	        Video(pos[11], 410, "weird shoes"),
	        Video(pos[17], 460, "wardrobe tips"))

	fit = ( Video(pos[7], 300, "cycling is good for you"),
			Video(pos[8], 825, "fitness through sensual dance"),
			Video(pos[14], 585, "women's self-defense"))
	aFit = (Video(pos[15], 260, "kundalini yoga"),
			Video(pos[16], 585, "women's self-defense"))

	hea = ( Video(pos[7], 230, "cannibalism really occurs"),
	        Video(pos[12], 230, "get some sleep"),
			Video(pos[16], 275, "what does your meat eat"),
			Video(pos[15], 820, "brain science"),
	        Video(pos[17], 260, "how to avoid over eating"))
	aHea = (Video(pos[5], 520, "unorthodox prosthetics"),
	        Video(pos[6], 330, "incredible people in wheelchairs"),
	        Video(pos[7], 330, "are supplements worthwhile"),
	        Video(pos[8], 330, "mosquitos can buzz off"),
	        Video(pos[10], 330, "do you want plastic surgery"),
	        Video(pos[14], 330, "how to ruin your brain"))

	hom = ( Video(pos[12], 520, " weird chairs"),
			Video(pos[15], 70, "10 sec tips - in the home"),
			Video(pos[16], 70, "10 sec tips - outside"),
			Video(pos[17], 270, "10 sec tips - DIY"),
			Video(pos[2], 260, "careful with your laundry"),
			Video(pos[6], 260, "apartment stories"))
	aHom = (Video(pos[3], 330, "helpful home hacks"),
	        Video(pos[4], 330, "the triffids are coming"),
	        Video(pos[6], 330, "with neighbors like these"))

	new = ( Video(pos[0], 200, "queen elizabeth doing things"),
	        Video(pos[1], 720, "global warming is real"),
			Video(pos[2], 270, "florida man"),
			Video(pos[3], 70, "politician's fun facts"),
			Video(pos[4], 530, "people getting arrested for the oddest things"),
			Video(pos[5], 270, "unusual news"),
			Video(pos[6], 160, "Obama and the White House"),
			Video(pos[7], 270, "quirky news"),
			Video(pos[8], 300, "news from around the world"),
			Video(pos[9], 280, "pulse on China"))

	par = ( Video(pos[3], 140, "buy Hannah Montana DVDs"),
			Video(pos[4], 240, "you affect your child's development"),
			Video(pos[10], 220, "caring for a newborn"),
			Video(pos[8], 340, "probably don't do these things"),
			Video(pos[14], 260, "teenagers"),
			Video(pos[15], 260, "kid troubles"),
			Video(pos[16], 200, "parenting tips"))
	aPar = (Video(pos[5], 400, "dress your girl"),
	        Video(pos[6], 330, "dress your boy"),
	        Video(pos[8], 260, "breastfeeding issues"),
	        Video(pos[9], 330, "changing diapers"))

	per = ( Video(pos[0], 260, "you might get your wallet back"),
			Video(pos[1], 260, "keep your credit score high"),
			Video(pos[5], 260, "traffic cameras are expensive"),
			Video(pos[6], 260, "odd driving tickets"),
			Video(pos[7], 200, "who needs savings"),
			Video(pos[8], 200, "what to do when you're in dept"),
			Video(pos[10], 260, "lawsuits are big business"),
			Video(pos[12], 200, "go for gold"))
	aPer = (Video(pos[2], 640, "don't get scammed"),
	        Video(pos[3], 330, "got your taxes done?"),
	        Video(pos[4], 330, "lottery highs and lows"),
	        Video(pos[9], 260, "diamonds are everybody's best friend"),
	        Video(pos[11], 580, "money makes the world go round"))

	pet = ( Video(pos[0], 260, "weird australian animals"),
			Video(pos[1], 200, "panda bears are rare"),
			Video(pos[4], 260, "are dolphins smarter than us?"),
			Video(pos[9], 260, "donkeys get it left, right, and center"),
	        Video(pos[15], 260, "horses do the darndest things"))
	aPet =( Video(pos[2], 380, "big cats"),
	        Video(pos[3], 350, "whales are endangered"),
	        Video(pos[5], 260, "monkey' are great"),
	        Video(pos[6], 520, "snakes on planes"),
	        Video(pos[7], 330, "bear news"),
	        Video(pos[8], 330, "cows are funny creatures"),
	        Video(pos[10], 330, "leave that kitten alone"),
	        Video(pos[11], 330, "don't be mean to puppies"),
	        Video(pos[12], 640, "dog tales"),
	        Video(pos[13], 260, "elephant news"),
	        Video(pos[14], 260, "rodent appreciation playlist"))

	sho = ( Video(pos[1], 200, "to be a store clerk"),
			Video(pos[2], 260, "IKEA wants to make everybody have"),
			Video(pos[3], 260, "do you spend too much money on"),
			Video(pos[4], 330, "Craigslist offers some odd deals"),
			Video(pos[5], 260, "interesting products"))

	spo = ( Video(pos[1], 720, "interesting products"),
			Video(pos[2], 330, "some facts from the london olympics"))

	tec = ( Video(pos[4], 520, "james bond 007 video games"),
			Video(pos[5], 260, "how do you deal with email?"),
			Video(pos[9], 410, "weird tales from outer space"),
			Video(pos[11], 410, "wifi news"),
			Video(pos[13], 140, "expensive cars"),
			Video(pos[13], 210, "video games have their uses"),
			Video(pos[14], 150, "check out this BMX gaming"),
			Video(pos[15], 260, "cool stuff happens on twitter"))
	aTec = (Video(pos[5], 330, "3d print your way through life"),
	        Video(pos[6], 520, "robots are on the rise"),
	        Video(pos[7], 260, "weird nasa news"),
	        Video(pos[9], 260, "solar power is the future"))

	tra = ( Video(pos[5], 270, "Do you fly first class"),
			Video(pos[8], 270, "visit mexico"),
			Video(pos[9], 270, "discover alaska"),
			Video(pos[10], 270, "chateaus of the world"),
			Video(pos[14], 220, "helicopter news"),
			Video(pos[16], 210, "gas station woes"),
			Video(pos[17], 480, "airport oddities"))
	#,Video(pos[18], 480, "want to live on mars?")
	aTra = (Video(pos[4], 520, "hotel tips"),
	        Video(pos[11], 400, "africa is a continent"),
	        Video(pos[12], 565, "go down under"),
	        Video(pos[15], 400, "visit bangkok"))
	#,Video(pos[16], 330, "fun facts special places")
	wed = ( Video(pos[7], 260, "wedding ring difficulties"),
			Video(pos[8], 260, "wedding disasters"),
			Video(pos[2], 230, "wedding-oriented movies"))
	aWed = (Video(pos[2], 260, "wedding jewelery"),
	        Video(pos[3], 260, "where did you give birth?"),
	        Video(pos[4], 260, "get the right wedding cake"),
	        Video(pos[5], 525, "some people shouldn't get married"))

	careersCategory = Category("Careers", Cord.catCareers, car)
	comedyCategory = Category("Comedy", Cord.catComedy, com)
	fashionCategory = Category("Fashion", Cord.catFashion, fas)
	fitnessCategory = Category("Fitness", Cord.catFitness, fit)
	healthCategory = Category("Health", Cord.catHealth, hea)
	homeAndGardenCategory = Category("Home And Garden", Cord.catHomeAndGarden, hom)
	newsAndPoliticsCategory = Category("News And Politics", Cord.catNewsAndPolitics, new)
	parentingCategory = Category("Parenting", Cord.catParenting, par)
	personalFinanceCategory = Category("Personal Finance", Cord.catPersonalFinance, per)
	petsAndAnimalsCategory = Category("Pets And Animals", Cord.catPetsAndAnimals, pet)
	shoppingCategory = Category("Shopping", Cord.catShopping, sho)
	sportsCategory = Category("Sports", Cord.catSports, spo)
	technologyCategory = Category("Technology", Cord.catTechnology, tec)
	travelCategory = Category("Travel", Cord.catTravel, tra)
	weddingCategory = Category("Wedding", Cord.catWedding, wed)

	videoCategory = (careersCategory, comedyCategory, fashionCategory, fitnessCategory,
					 healthCategory, homeAndGardenCategory, newsAndPoliticsCategory,
					 parentingCategory, personalFinanceCategory, petsAndAnimalsCategory,
					 shoppingCategory, sportsCategory, technologyCategory, travelCategory,
					 weddingCategory)
	watchedCategories = 0
	while watchedCategories < NUM_OF_CATEGORIES:
		#Generate random number for I
		upperBound = NUM_OF_CATEGORIES - 1
		i = random.randint(0, upperBound)
		#If the category has been watched
		while videoCategory[i].isCategoryFinished == True:
			if i >= NUM_OF_CATEGORIES:
				break
			else:
				if i >= upperBound:
					break
				i += 1

		if videoCategory[i].isCategoryFinished == False:
			print "working in: " + videoCategory[i].returnCategory
			watchCategory(videoCategory[i].returnTotalVideos, videoCategory[i], videoCategory[i].exposeVideos)
			videoCategory[i].categoryIsFinished()
			watchedCategories += 1

	addCareersCategory = Category("Careers", Cord.catCareers, aCar)
	#addComedyCategory = Category("Comedy", Cord.catComedy, aDom)
	addFashionCategory = Category("Fashion", Cord.catFashion, aFas)
	addFitnessCategory = Category("Fitness", Cord.catFitness, aFit)
	addHealthCategory = Category("Health", Cord.catHealth, aHea)
	addHomeAndGardenCategory = Category("Home And Garden", Cord.catHomeAndGarden, aHom)
	#addNewsAndPoliticsCategory = Category("News And Politics", Cord.catNewsAndPolitics, aNew)
	addParentingCategory = Category("Parenting", Cord.catParenting, aPar)
	addPersonalFinanceCategory = Category("Personal Finance", Cord.catPersonalFinance, aPer)
	addPetsAndAnimalsCategory = Category("Pets And Animals", Cord.catPetsAndAnimals, aPet)
	#addShoppingCategory = Category("Shopping", Cord.catShopping, aSho)
	#addSportsCategory = Category("Sports", Cord.catSports, aSpo)
	addTechnologyCategory = Category("Technology", Cord.catTechnology, aTec)
	addTravelCategory = Category("Travel", Cord.catTravel, aTra)
	addWeddingCategory = Category("Wedding", Cord.catWedding, aWed)

	additionalVideoCategory = (addCareersCategory, addFashionCategory, addFitnessCategory,
						addHealthCategory, addHomeAndGardenCategory, addParentingCategory,
						addPersonalFinanceCategory,addPetsAndAnimalsCategory,
						addTechnologyCategory,addTravelCategory,addWeddingCategory)

	filePrintout = time.strftime("%dI%mI%Y") + '.png'
	ImageGrab.grab_to_file(filePrintout)

	sleepTimer = random.randint(0, 600)
	print "sleeping for: " + sleepTimer
	sleep(sleepTimer)
	watchedAdditionalCategories = 0
	print "in Additional Area"
	while watchedAdditionalCategories < NUM_OF_ADDITIONAL_CATEGORIES - 5:
		# Generate random number to decide the category to watch
		upperBoundA = NUM_OF_ADDITIONAL_CATEGORIES - 1
		i = random.randint(0, upperBoundA)
		#If the category has been watched
		while additionalVideoCategory[i].isCategoryFinished == True:
			if i >= NUM_OF_ADDITIONAL_CATEGORIES:
				break
			else:
				if i >= upperBoundA:
					break
				i += 1

		if additionalVideoCategory[i].isCategoryFinished == False:
			print "working in: " + additionalVideoCategory[i].returnCategory
			watchCategory(additionalVideoCategory[i].returnTotalVideos, additionalVideoCategory[i], additionalVideoCategory[i].exposeVideos)
			additionalVideoCategory[i].categoryIsFinished()
			watchedAdditionalCategories += 1

#### - Main - ####
def main():
	#A = randint(200,360)
	#if A %3 == 0:
	#	A = randint(420,1080)
	#	print A
	#	sleep(A)
	#elif A%3 == 1:
	#	A = randint(1080,1440)
	#	print A
	#	sleep(A)
	#else:
	#	A = randint(1440,1640)
	#	print A
	#print "sleeping for: " + A;
	filePrintout = time.strftime("%dI%mI%Y") + "III" + time.strftime("%HI%MI%S") + '.png'
	ImageGrab.grab_to_file(filePrintout)
	#sleep(A)


	webbrowser.get("firefox").open("www.swagbucks.com")
	print "hi"
	sleep (5)
	mousePos(Cord.catShowMore)
	leftClick()
	goToCategories()
	##########################################################
	filePrintout = time.strftime("%dI%mI%Y") + "III" + time.strftime("%HI%MI%S") + '.png'
	ImageGrab.grab_to_file(filePrintout)

if __name__ == '__main__':
	main()

# now all I need to do is expose the tuples within each category to the watchCategory function