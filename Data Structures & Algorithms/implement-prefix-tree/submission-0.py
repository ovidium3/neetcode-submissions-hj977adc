class TrieNode:
    def __init__(self):
        self.children = {} # 26 possible children. easier to use hashmap than array
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root # pointer to root, will be updated as you iterate thru

        for c in word: # create or iterate through each node representing each character
            if c not in curr.children: # create a TrieNode for this character if it doesnt exist
                curr.children[c] = TrieNode()
            curr = curr.children[c] # update curr ptr to child node at current letter index
        
        curr.endOfWord = True # after reaching end of word, update bool

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children: # stop iterating and just return False
                return False
            curr = curr.children[c]
        
        return curr.endOfWord # will let us know if we found the exact word or not
 
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children: # stop iterating and return False
                return False
            curr = curr.children[c]
        
        return True # no need to check if it is the end word or not. just need substring
        