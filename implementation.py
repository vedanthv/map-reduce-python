import re
import pandas as pd

# Reading the input
inputfile = open(r'D:\University\Semester 6\map-reduce-python\input.txt',"r")
text = inputfile.read()

# Data Cleaning
def data_clean(text):
  NoNumbers = ''.join([i for i in text if not i.isdigit()]) # Removing numbers
  NoNumbers = text.lower() # Making the text to lower case
  onlyText = re.sub(r"[^a-z\s]+",' ',NoNumbers) # Removing punctuation
  finaltext = "".join([s for s in onlyText.strip().splitlines(True) if s.strip()]) # Removing the null lines
  return finaltext

# Split Data
def splitlines(text,limit):
  linessplit = text.splitlines() # Splitting the lines into a list
  split1 = linessplit[0:limit] # Creating the first split with the first limit number of lines into split 1
  split2 = linessplit[limit:] # Creating the second split with the first limit number of lines into split 2
  return split1,split2

# Mapper Function
def mapper(text,out_queue):
  keyval = []
  for i in text:
    wordsplit = i.split()
    for j in wordsplit:
      keyval.append([j,1]) # Append each word in the line and store it in k-v format like ["word",1] as a list
    out_queue.put(keyval)

# Sorting the Data
def sortedlists(list1,list2):
  out = list1 + list2 # Appending the two input lists into a single list
  out.sort(key= lambda x :x[0]) # Sorting the lists based on the first element of the list which is the "word"
  return out

# Partition 
def partition(sorted_list) :
 sort1out = []
 sort2out = []
 for i in sorted_list:
    if i[0][0] < 'n': # Partitioning the sorted word list into two separate lists 
      sort1out.append(i) # with first list containing words starting with a-m and n-z into second
    else : sort2out.append(i)
 return sort1out,sort2out    

# Reducer
def reducer(part_out1,out_queue) :
  sum_reduced = []
  count = 1
  for i in range(0,len(part_out1)): # for every word in the sentence
    if i < len(part_out1)-1: # until the whole word parsed
      if part_out1[i] == part_out1[i+1]:
       count = count+1 # count the number of words