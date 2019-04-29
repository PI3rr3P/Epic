
if __name__ == '__main__':
	RED = "\033[41m"
	BLACK = "\033[40m"
	GREEN = "\033[42m"
	YELLOW = "\033[43m"
	BLUE = "\033[44m"
	MAGENTA = "\033[45m"
	CYAN = "\033[46m"
	LIGHT_GREY = "\033[47m"
	DARK_GREY = "\033[100m"
	LIGHT_RED = "\033[101m"
	LIGHT_GREEN = "\033[102m"
	LIGHT_YELLOW = "\033[103m"
	LIGHT_BLUE = "\033[104m"
	LIGHT_MAGENTA = "\033[105m"
	LIGHT_CYAN = "\033[106m"
	WHITE = "\033[107m"
	END = '\033[0m'
	SQUARE = '  '
	BLOCK = '\u25A9'

	file = "minas.txt"
	symbolMap = [] # [x][y]= str color
	with open(file, 'r') as inputFile:
		for lines in inputFile:
			symbolMap.append([word for word in lines if word != '\n'])
	for i, line in enumerate(symbolMap):
		raw = ""
		for j, square in enumerate(line):
			if square == 'b':
				raw += DARK_GREY + SQUARE
			else:
				if (abs(j - i + 1) % 2 == 0):
					raw += LIGHT_GREY + SQUARE
				else:
					raw += BLACK + SQUARE
		raw += END
		print(raw)