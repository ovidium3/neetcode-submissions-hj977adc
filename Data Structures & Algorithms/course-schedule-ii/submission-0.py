class Solution: # O(E + V) where E = prereqs, V = numCourses
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same idea as course schedule, but building output with dfs - topological sort
        # cross out a node once we visit it since we never need to revisit
        # if we detect a cycle, return empty list - topological sort not possible

        # a course has 3 possible states:
        # visited -> course has been added to output
        # visiting -> course not added to output, but added to cycle
        # unvisited -> course not added to output or cycle
        prereqMap = { i:[] for i in range(numCourses) } # course mapping to list of prereqs
        for course, prereq in prerequisites: # populate prereq map
            prereqMap[course].append(prereq)
        
        res = []
        visited, cycle = set(), set() # track current path, and a set to detect a cycle
        def dfs(course: int):
            # base cases
            if course in cycle: # cycle detected
                return False
            if course in visited: # already in output, no need to keep checking back
                return True
            
            # now do dfs on all prereqs of the course
            cycle.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False # break out of dfs if cycle detected
            
            # after verifying course prereqs, add course itself to res and mark as visited
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return [] # return empty list if cycle detected
        return res # if no cycle detected, can safely return res