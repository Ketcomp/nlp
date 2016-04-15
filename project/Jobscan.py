import sys
import pprint
import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
from collections import Counter
meaning = []

# with open('resume.txt', 'r') as resume:
#     for line in resume:
#         #pprint.pprint(line.split())
#         # tokens = nltk
#         pprint.pprint(1)

if __name__ == '__main__':
    job_des_words = []
    resume_words = []
    if(3 == len(sys.argv)):
        script, job_des_file, resume_file = sys.argv

        with(open(job_des_file)) as jdf:
            description = jdf.read()
            job_des_words = description.split(" ")
        with(open(resume_file)) as rf:
            resume = rf.read()
            resume_words = resume.split(" ")
        print(job_des_words[0])
        print(lesk(description, job_des_words[0]))
    else:
        print("No input present, exiting.")