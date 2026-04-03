class TrieNode:
    def __init__(self):
        self.children = {} # hashmap of character to TrieNode
        self.endOfWord = False
    
    def addWord(self, word: str): # add word to search for
        curr = self
        for c in word: # iterate over word, creating nodes as needed
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True # cant forget to update this
    
    # slight optimization to avoid searching same word twice
    def removeWord(self, word: str): # remove word once found
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]

class Solution: # O()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # board dimensions and sets to hold result and visited board positions
        ROWS, COLS = len(board), len(board[0])
        res = set() # contains str
        visited = set() # contains (r, c)
        
        # set up Trie structure with all possible words to find
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        def backtrack(r, c, node, word):
            # base cases
            if ((r < 0 or c < 0 or r == ROWS or c == COLS) or # invalid board idx
                ((r, c) in visited) or # tile already used in curr word
                (board[r][c] not in node.children)): # char isnt in Trie
                return
            
            # add char to curr word, check if it's in the Trie
            ch = board[r][c]
            word += ch
            visited.add((r, c)) # as soon as we update word, add here

            node = node.children[ch]
            if node.endOfWord:
                res.add(word)
                #root.removeWord(word)

            # else keep searching, word isnt complete yet
            backtrack(r - 1, c, node, word) # up
            backtrack(r + 1, c, node, word) # down
            backtrack(r, c - 1, node, word) # left
            backtrack(r, c + 1, node, word) # right

            visited.remove((r, c)) # backtrack tile

        # brute force - run backtracking algo at each tile
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")

        return list(res) # turn set into a list