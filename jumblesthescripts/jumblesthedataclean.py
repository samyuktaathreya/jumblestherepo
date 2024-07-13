import csv
import datetime
import math

#this python file converts the scrambles in jumblestheclown.txt into a csv file

#extract relevant values from the lines
def getJumbles(line):
    jumbles = []
    line = line.strip()
    line = line[2:len(line) - 2]
    for jumble in line.split(','):
        jumble = jumble.lower()
        jumbles.append(jumble.strip())
    return jumbles
def getDate(line):
    line = line.strip()
    print(line)
    line = line[:len(line) - 1]
    
    #check if it's AM or PM
    if line.find('PM') != -1: #PM
        pmInd = line.find('PM') #gives index of P
        colonInd = line.find(':') #gives index of clock colon
        minutes = int(line[colonInd + 1:pmInd].strip())
        spaceInd = line.find(' ')
        hours = int(line[spaceInd + 1:colonInd].strip())
        if hours != 12:
            hours += 12
    else: #AM
        pmInd = line.find('AM') #gives index of A
        colonInd = line.find(':') #gives index of clock colon
        minutes = int(line[colonInd + 1:pmInd].strip())
        spaceInd = line.find(' ')
        hours = int(line[spaceInd + 1:colonInd].strip())
    
    #get date
    date = line[:spaceInd]
    date = date.split('/')
    print(line)
    print(date)
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    if math.log(year, 10) + 1 < 4:
        year = 2000 + year
    return(datetime.datetime(year,month,day,hours,minutes))
def identifyWord(line):
    line = line.strip()
    #line is a string
    #to identify a word: the word is either after a number or the number is after a word
    #so need to look for something of the format "13." being in the line
    #1. find a number being in the line
    dotInd = line.find('.')
    #2. extract the word
    #two scenarios: the number before the word and the number after the word
    if dotInd > 4: #the number is after the word
        i = dotInd - 1
        while not(line[i].isalpha()):
            i -= 1
        word = line[:i + 1]
    else:
        word = line[dotInd + 2:]
    #3. return the word
    return word.lower()

def makeRowForCSV(lines):
#input 'lines' is the string separated by each date
#compile values into a list of the format [date, word, jumbles] where
#date : the date the word was inputted
#word : the word to be scrambled
#jumbles : scrambles of the word
    lines = lines.strip()
    lines = lines.splitlines()
    date = getDate(lines[0])
    lines = lines[1:]
    result = []
    while len(lines) >= 2:
        word = identifyWord(lines[0])
        jumbles = getJumbles(lines[1])
        result.append([date,word,jumbles])
        lines = lines[2:]
    return(result)

def combJumbles(input_file):
#goes through jumblestheclown.txt and returns the values in a nice 2D list, 
#perfect for creating your csv file today at www.jumblestheadvertisement.com
    with open(input_file, mode='r', encoding='utf-8') as file:
        content = file.read()
    lines = str(content)
    #want to split the lines by dates
    result = [['date', 'word', 'jumbles']]
    i = 0
    lines = lines.split('[')
    for line in lines:
        line = line.strip()
        if len(line) < 1:
            continue
        result = result + makeRowForCSV(line)
    return result

def writeToCsv(data, output_file):
#write the jumblestheclown data into a csv file
    with open(output_file, mode='w', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

input_file = 'jumblesthefiles\jumblestheclown.txt'  #the text file with all scrambles
output_file = 'jumblesthefiles\jumblesthedata.csv'  #the csv file with all scrambles neatly formatted

data = combJumbles(input_file)
writeToCsv(data,output_file)