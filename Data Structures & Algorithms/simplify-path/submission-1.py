class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for p in path:
            if p == ".":
                # treat as a noop
                continue
            elif p == "..":
                # ../ --> parent dir, so we pop from stack if it exists
                # otherwise treat it as a noop
                if stack:
                    stack.pop()
            elif p == "":
                # we mightve accidentally split the path too much
                # i.e. /// -> /, /, /
                # or there is nothing to be added here since it was garbage
                continue
            else:
                # directory name so we want to add to stack
                stack.append(p)
        
        # add leading "/" to our output
        return "/" + "/".join(stack)