#LastName: Trierweiler
#FirstName: Nick
#Email: siroccomask@gmail.com

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node
        #self.letter = None


    def addWord(self, w, pos = 0):
        letter = w[pos]
        if letter not in self.next:
            self.next[letter] = MyTrieNode(False)
        if(pos + 1 == len(w)): #reached the last letter
            self.next[letter].word = w
            self.next[letter].isWordEnd = True
            self.next[letter].count += 1
        else:
            self.next[letter].addWord(w, pos + 1)

    

    # test 
    # def printDict(self):
    #     #made just for funzies, was interesting in seeing this print recursively
    #     #prints the prefixes, and then the suffixes due to the way it is being called onto the stack
    #     for key, value in self.next.items():
    #         print (key, value)
    #         self.next[key].printDict()



    def lookupWord(self, w, pos = 0):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        # YOUR CODE HERE
        #A little sloppier than I wanted but those edge cases were hard to debug!!!

        if pos == len(w):
            if self.isWordEnd == True:
                return (self.count)
            else:
                return(0)
        
        letter = w[pos]
        if letter not in self.next: #NOT FOUND
            return(0) 
        else: #is letter is in self.text
            if pos == len(w) and self.isWordEnd == True:
                return (self.next[letter].count)
            else:
                return (self.next[letter].lookupWord(w, pos + 1))


        #return 0  # TODO: change this line, please

 

    def autoComplete(self, w, pos = 0):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        #YOUR CODE HERE
            arr = []
            if(len(w) > 1 + pos):
                letter = w[pos]
                if letter in self.next:
                    return(self.next[letter].autoComplete(w, pos+1))
                else:
                    return ((w, 0))
            else:
                if(w[len(w)-1] in self.next):
                    return(self.next[w[len(w)-1]].dfsComplete(w, arr))
                else:
                    return([])
            
        
    def dfsComplete(self, acc, res,  pos = 0):
        if self.next == []:
            return
        if self.isWordEnd:
            res.append((acc, self.count))
        for key in self.next:
            self.next[key].dfsComplete(acc+key, res)
        return(res)





    
    

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['ad', 'ad', 'ado','ade','adp', 'test','testament','palandrome','palandrome','testing','ping','pin','pink','pine','pint','testing','pinetree']
    #ade causes ado to break, this is a problem!!
    for w in lst1:
        t.addWord(w)
        t.printDict
    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    j4 = t.lookupWord('test') #should return 1
    j5 = t.lookupWord('palandrome') #should return 2
    j6 = t.lookupWord('ado') #should return 1
    j7 = t.lookupWord('ado') #should return 1
    j8 = t.lookupWord('ad') #should return 2
    j9 = t.lookupWord('test')
    #print(j, j2, j3, j4, j5, j6, j7, j8, j9)
    #print(0,0,2,1,2,1,1,2, 1)
    
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    lst5 = t.autoComplete('test')
    print('Completions for \"test\" are : ')
    print(lst5)
    
    
     
