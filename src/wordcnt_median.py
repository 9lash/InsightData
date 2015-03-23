import glob
import string
from collections import defaultdict
import sys

#Takes input argument from the user. 
input_in = sys.argv[1]
output1 = sys.argv[2]
output2 = sys.argv[3]

# Defining a median function:
def median(a):
	n = len(a)
	if(n%2==0):
		return (float((a[(n/2)] + a[(n/2) - 1])/2.0))
	else: 
		return float(a[n/2])

		
wordsperline=[]
runningmedian=[]
word_count = defaultdict(int) 

#Searching all the files 
files = glob.glob(input_in+'/*.txt')
files.sort()

#Wordcount & Running Median
for j in range(0,len(files)):
	with open(files[j],'r') as fp:
		for line in fp:
			x = line.lower().translate(None, string.punctuation).strip().split()
			for word in x:
				word_count[word] +=1 
			wordsperline.append(len(x))
			wordsperline.sort()
			runningmedian.append(median(wordsperline))

		
keylist = word_count.keys()
keylist.sort()
fp.close()

#Wordcount Output File:
f = open( output1 ,'w')	
for index in keylist:
	f.write('{}\t\t{}\n'.format(index, word_count[index]))
f.close()
	
#Running Median Output File:
f = open(output2, 'w')
for i in range(0, len(runningmedian)):
	f.write('{}\n'.format(runningmedian[i]))
		

		
	



	

