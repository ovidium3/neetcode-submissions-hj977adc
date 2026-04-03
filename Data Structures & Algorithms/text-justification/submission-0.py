class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        currLen = 0
        tmpWords = []

        i = 0
        while i < len(words):
            word = words[i]
            wordLen = len(word)

            # add the word to current line
            if currLen + wordLen + len(tmpWords) <= maxWidth:
                tmpWords.append(word)
                currLen += wordLen
                i += 1
            else: # completed line, add to output
                # add whitespace to existing words to fill char ct
                extra_space = maxWidth - currLen
                remainder = extra_space % max(1, (len(tmpWords) - 1))
                space = extra_space // max(1, (len(tmpWords) - 1))
                for j in range(max(1, len(tmpWords) - 1)):
                    tmpWords[j] += " " * space
                    if remainder:
                        tmpWords[j] += " "
                        remainder -= 1
                res.append("".join(tmpWords)) # since we alr put all spacing in it
                tmpWords, currLen = [], 0
                
        last_line = " ".join(tmpWords)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space
        res.append(last_line)
        return res
            