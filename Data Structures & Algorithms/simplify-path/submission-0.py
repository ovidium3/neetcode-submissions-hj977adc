class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for p in path:
            if p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            elif p == "":
                # we mightve accidentally split the path too much
                # i.e. /// -> /, /, /
                continue
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)