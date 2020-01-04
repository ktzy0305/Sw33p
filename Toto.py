import random
import datetime
import itertools
import operator
import csv

numberList = []
draw_results = []

class DrawResult:
    def __init__(self, date, numbers):
        self.date = date
        self.numbers = numbers

def initApp():
    for i in range(100):
        generateNumbers()
    return 

def getResults():
    for result in draw_results:
        date = str(result.date)
        winning_numbers = ""
        with open('result.csv', mode='a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(result.numbers)
        for numbers in result.numbers:
            numberList.append(numbers)
            winning_numbers += "{0}\t".format(numbers)
        print("#"*(len(date)+len(winning_numbers)))
        print("{0}\n{1}".format(date,winning_numbers))
        print("\n")
    return 

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
        count += 1
        min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def generateNumbers():
    numList = random.sample(range(1, 49), 7)
    numList.sort()
    draw_results.append(DrawResult(datetime.datetime.now(), numList))
    return

def PopularSevenNumbers(numberList):
    common_nums = []
    popular_num_result = ""
    for i in range(7):   
        common_nums.append(most_common(numberList))
        numberList = list(filter(lambda a: a != most_common(numberList), numberList))
    common_nums.sort()
    for number in common_nums:
        popular_num_result += "{0}\t".format(number)
    print("Popular Numbers : {0}".format(popular_num_result))
    return

initApp()
getResults()
PopularSevenNumbers(numberList)
print("Most Common Number : {0}".format(most_common(numberList)))