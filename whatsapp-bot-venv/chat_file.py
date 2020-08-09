from model import *
import numpy
import nltk
import random
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

def bag_of_words(s,words):
   bag = [0 for _ in range(len(words))]
    
   s_words = nltk.word_tokenize(s)
   s_words = [stemmer.stem(word.lower()) for word in s_words]
    
   for se in s_words:
       for i,w in enumerate(words):
           if w == se:
               bag[i] = 1
                
   return numpy.array(bag)

def chat(inp):
   results = model.predict([bag_of_words(inp,words)])   
   results_index = numpy.argmax(results)
   tag = labels[results_index]
        
   for tg in data["intents"]:       
       if tg['tag'] == tag:
           responses = tg['responses']
            
   return (random.choices(responses))