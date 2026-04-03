class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word: # iterate over each char in word, creating a new node if necessary
            if c not in curr.children: # create new node for character if it doesnt exist
                curr.children[c] = TrieNode()
            curr = curr.children[c] # update curr to its respective child
        
        curr.endOfWord = True # mark char as being end of word

    def search(self, word: str) -> bool:
        def dfs(root, i): # i represents index of word to start comparing at
            curr = root

            for j in range(i, len(word)):
                c = word[j]
                if c == ".": # recursively check since "." can be any letter
                    for child in curr.children.values(): # check all letters in case of "."
                        if dfs(child, j + 1):
                            return True
                    return False # else none matched
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.endOfWord # finally must check again if it is even a valid word
        
        return dfs(self.root, 0)
