'''
Created on Jul 22, 2015

@author: Akshat Verma
Computing Id: av2zf
'''
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def create_list_from_file(file):
    with open(file) as f:
        words = f.readlines()
    return [word.strip() for word in words]

#Read data from the text files into python lists - city_list, state_list,company_list and job_description_list

city_list = create_list_from_file("city_list.txt")
state_list = create_list_from_file("state_list.txt")
company_list = create_list_from_file("company_list.txt")
job_description_list = create_list_from_file("job_description_list.txt")

#Generate histograms to plot the top 10 cities, states and companies and save them to png files.

labels, values = zip(*Counter(city_list).most_common(10))
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width, color='r')
plt.xticks(indexes + width * 0.5,labels,rotation = 45)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.savefig("jobs_by_city.png")

labels, values = zip(*Counter(state_list).most_common(10))
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5,labels,rotation = 45)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.savefig("jobs_by_state.png")

labels, values = zip(*Counter(company_list).most_common(10))
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5,labels,rotation = 45)
plt.tick_params(axis='both', which='major', labelsize=5)
plt.savefig("jobs_by_company.png")

'''
    loop over the job_descriptions list:
        (i). Split the job description textual data into words.
        (ii). Strip the words , ignore empty strings and add them to list , word_list if they are not stop words
    If two consecutive words form a word pair, remove both words from list and them to a different list
    Extend the word_list to include word_pair list
    Count the frequencies of the words/word pairs and generate a histogram to plot the top 30 words.

'''
    
stopwords = create_list_from_file("stop-words.txt") # Populate a list of stopwords by reading from stop-words.txt file
word_list = []
word_pairs = []
wordpair_list = create_list_from_file("wordpair.txt") # Populate a list of word pairs by reading from word-pair.txt file

for description in job_description_list:
    word_list.extend(([word.lower().strip().rstrip(",") for word in description.split(" ") if word.strip() and len(word) > 1 and word.lower() not in stopwords]))
i = 0
while i < len(word_list)-2:
    if (word_list[i]+" "+word_list[i+1]) in wordpair_list:
        word_pairs.append(word_list.pop(i)+" "+word_list.pop(i))
    else:
        i = i+1

word_list.extend(word_pairs)
labels, values = zip(*Counter(word_list).most_common(30))
indexes = np.arange(len(labels))
width = 2
plt.setp(labels)
plt.bar(indexes, values, width, color = 'r')
plt.xticks(indexes + width * 0.5,labels,rotation=45)
plt.tick_params(axis='both', which='major', labelsize=5)
plt.savefig("most_desired_skills.png")
