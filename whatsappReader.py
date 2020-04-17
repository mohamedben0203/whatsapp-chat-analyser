import sys
import codecs
import operator
from prettytable import PrettyTable
import matplotlib.pyplot as plt

#take input from the command line
fileName = str(sys.argv[1])

#object which contains the message the metadata
class Message():
    def __init__(self, text, sender, dateTime):
        self.text = text
        self.words = text.split()
        self.sender = sender
        self.dateTime = dateTime
        self.date = dateTime[0].replace('[', '')
    
    def numberOfWords(self):
        return len(self.words)

allMessages = []

#loop through each message in the file
with codecs.open(fileName, encoding='utf-8') as chat:
    for message in chat:
        dateTime = message[1:21].split(",")
        message = message[23:]
        index = message.find(':')
        name = message[:index]
        text = message[index + 2:]
        newMessage = Message(text, name, dateTime)
        allMessages.append(newMessage)

firstUser = allMessages[0].sender
firstUserMessages = []
firstUserWords = 0
secondUserMessages = []
secondUserWords = 0

dates = dict()
firstUserDates = dict()
secondUserDates = dict()

for message in allMessages:

    if message.date in dates:
        dates[message.date] += 1
    else:
        dates[message.date] = 1

    if message.sender == firstUser:
        firstUserMessages.append(message)
        firstUserWords = firstUserWords + message.numberOfWords()
        if message.date in firstUserDates:
            firstUserDates[message.date] += 1
        else:
            firstUserDates[message.date] = 1
    else:
        secondUserMessages.append(message)
        secondUser = message.sender
        secondUserWords = secondUserWords + message.numberOfWords()
        if message.date in secondUserDates:
            secondUserDates[message.date] += 1
        else:
            secondUserDates[message.date] = 1

totalMessages = len(firstUserMessages) + len(secondUserMessages)
totalWords = firstUserWords + secondUserWords
firstUserAvgWords = round(firstUserWords/len(firstUserMessages), 2)
secondUserAvgWords = round(secondUserWords/len(secondUserMessages), 2)

firstUserWordsPercent = round(100 * firstUserWords/totalWords,2)
secondUserWordsPercent = round(100 *secondUserWords/totalWords, 2)

firstUserMsgPercent = round(100 * len(firstUserMessages)/totalMessages, 2)
secondUserMsgPercent = round(100 * len(secondUserMessages)/totalMessages, 2)

firstDate = allMessages[0].dateTime[0]
firstTime = allMessages[0].dateTime[1][1:]

t = PrettyTable(['Data', firstUser, secondUser, 'total'])
t.add_row(['messages sent', len(firstUserMessages), len(secondUserMessages), totalMessages])
t.add_row(['words used', firstUserWords, secondUserWords, totalWords])
t.add_row(["ratio of words used", str(firstUserWordsPercent) +
           "%", str(secondUserWordsPercent) + "%", "100"])
t.add_row(["ratio of messages sent", str(firstUserMsgPercent) +
           "%", str(secondUserMsgPercent) + "%", "100"])
t.add_row(["average words per message", firstUserAvgWords, secondUserAvgWords, round(totalWords/totalMessages,2)])

sorted_d = dict(sorted(dates.items(), key=operator.itemgetter(1), reverse = True))
mostTextsDay = next(iter(sorted_d))
mostTextInDay = dates[mostTextsDay]

sorted_d = dict(sorted(firstUserDates.items(), key=operator.itemgetter(1), reverse=True))
firstUserMostTextsDay = next(iter(sorted_d))
firstUserMostTextInDay = firstUserDates[firstUserMostTextsDay]

sorted_d = dict(sorted(secondUserDates.items(), key=operator.itemgetter(1), reverse=True))
secondUserMostTextsDay = next(iter(sorted_d))
secondUserMostTextsInDay = secondUserDates[secondUserMostTextsDay]

t.add_row(["Most texts sent was on", firstUserMostTextsDay,
           secondUserMostTextsDay, mostTextsDay])

t.add_row(["Most texts in one day", firstUserMostTextInDay,
           secondUserMostTextsInDay, mostTextInDay])

print("------------------------------------------------------------------------")
print(f"This data is for the messages between {firstUser} and {secondUser}")
print(f"The first message was sent by {firstUser} on {firstDate} at {firstTime}")
print(t)
