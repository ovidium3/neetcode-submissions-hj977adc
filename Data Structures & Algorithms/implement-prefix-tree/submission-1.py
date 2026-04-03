class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c in cur.children: # simply move down to next char
                cur = cur.children[c]
            else: # need to create a new entry
                cur.children[c] = TrieNode()
                cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return True
        