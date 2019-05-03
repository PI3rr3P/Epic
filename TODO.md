# Tutorial link for multiplayer mode
	https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1
	https://www.raywenderlich.com/2613-multiplayer-game-programming-for-teens-with-python-part-2
	librayry pour creer un serveur = PodSixNet 
	https://github.com/chr15m/PodSixNet/ 
	or pip install PodSixNet
# Ressources :
	+ https://www.chessprogramming.org/Getting_Started
# Games ideas:
	+ severals kings
	+ tree and rock, tree can be destroyed
	+ dragon piece (~Knight extended)
	    | | |x| | | | |
		| |x| | |x|x| |
		| |x| |x| | |x|
		| | |x|D|x| | |
		|x| | |x| |x| | 
		| |x|x| | |x| |
		| | | | |x| | |
	+ allow alliances
	+ color for people
	+ AI with hive mind
	+ individual AI
	+ ~skin for camp (hu vs ud)
# Making a map editor:
	+ map editor allow placing block/tree (map stuff)
	+ allow placing initial pieces
	+ must choose color of the stuff
	+ define Xmax, Ymax and number of players (not the kind of)
	+ save as 2D list of [x][y](type, color)
	+ use pickle to save and load the map
# Poblems still unsolve:
	+ In rule/pieces
		- check : must see if a given move avoid the checkmate
		- loosing : special pre-running function, must detect is any move can be down to avoid checkmate