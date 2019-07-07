# 332-reconstruct-itinerary.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Make skeleton vertex graph.
        graph = collections.defaultdict(list)
        for fr, to in tickets:
            graph[fr].append(to)
        # You should return the itinerary that has the smallest lexical order.
        for fr in graph:
            graph[fr].sort()

        route = []

        def dfs(fr):
            while graph[fr]:
                to = graph[fr].pop(0)
                dfs(to)
            route.append(fr)

        dfs("JFK")
        return route[::-1]
