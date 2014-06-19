import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)    
    ###############################################
    #build dictionary
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
  		term, score  = line.split("\t") 
  		scores[term] = float(score)

    ###############################################
    atweetfile = open(sys.argv[2])
    tweet_text = []
    for line in atweetfile:
        try:
            tweet_text.append(json.loads(line)["text"].encode('utf-8'))
        except:
            pass

    tot_sentiment=[]
    words_new=[]
    words_new_scores={}
    words_new_count={}
    for item in tweet_text:
        words = []
        words = item.split()
        total = 0
        #dictionary to track if a word has been counted
        word_ind = {}
        for everyword in words:
            word_ind[everyword]=0
            if everyword in scores.keys():                           
                total += scores[everyword]
            #if word is not in the list of new words, add it and initialize counters
            elif everyword not in words_new:
                    words_new.append(everyword)
                    words_new_scores[everyword]=0
                    words_new_count[everyword]=0
        #output individual tweet sentiment
#        sys.stdout.write(str(total) + '\n')
        #compute sentiment of tweet using existing dictionary            
        tot_sentiment.append(total)
        #set current tweet sentiment to words not in dictionary
        #only count the word once per tweet
        for everyword in words:
            if everyword in words_new:
                if word_ind[everyword]==0:
                    words_new_scores[everyword] += total
                    words_new_count[everyword] += 1
                    word_ind[everyword]=1
#                    sys.stdout.write(everyword)
#                    sys.stdout.write(str(words_new_scores[everyword])+'\n')
                
    for item in words_new:
        scores[item]=round(words_new_scores[item]/words_new_count[everyword])
        sys.stdout.write(item + '' + str(scores[item]) + '\n')
#        
	

if __name__ == '__main__':
    main()