class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use dfs, this is a graph problem. essentially checking if there is a cycle
        # use an adjacency list, represented with prerequisite hashmap
        # as we visit courses, remove prerequisites associated with them
        # detect loop using a set/array of visited, containg current list of courses in dfs

        prereqMap = { i:[] for i in range(numCourses) } # map of course (int) to prereqs (list), init empty
        for course, prereq in prerequisites: # populate prereq map
            prereqMap[course].append(prereq)
        
        visited = set() # track courses on curr dfs path
        def dfs(course):
            # base cases
            if course in visited: # ran into a loop of prereqs
                return False
            if prereqMap[course] == []: # no more prereqs to complete
                return True
            
            # keep searching thru prereqs
            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            
            # backtrack course from visited
            visited.remove(course)
            prereqMap[course] = [] # update map indicating no more prereqs to complete
            return True
        
        for course in range(numCourses): # manually check each course with dfs. make sure all prereqs check out
            if not dfs(course):
                return False
        return True