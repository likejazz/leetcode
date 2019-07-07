# 207-course-schedule.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make skeleton vertex graph.
        graph = {k[1]: [] for k in prerequisites}
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])

        visited = set()  # Visited vertex set for permanent storage
        traced = set()   # Traced vertex set for temporary storage.

        def visit(vertex):
            if vertex in visited:
                return False

            traced.add(vertex)
            visited.add(vertex)
            if vertex in graph:
                for neighbour in graph[vertex]:
                    if neighbour in traced or visit(neighbour):
                        return True  # cyclic!
            traced.remove(vertex)
            return False

        for v in graph:
            if visit(v):
                return False

        return True
