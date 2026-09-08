from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list:
        # course -> prerequisites it depends on
        prereq = {i: [] for i in range(numCourses)}

        for course, requirement in prerequisites:
            prereq[course].append(requirement)

        visiting = set()
        checked = set()

        def dfs(course):
            # Course is already in current DFS path -> cycle
            if course in visiting:
                return False

            # Already fully checked and safe
            if course in checked:
                return True

            # Start exploring this course
            visiting.add(course)

            for requirement in prereq[course]:
                if not dfs(requirement):
                    return False

            # Finished this course safely
            visiting.remove(course)
            checked.add(course)

            return True

        # Need to check every course because graph can be disconnected
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True