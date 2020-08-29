# 684-redundant-connection.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Make skeleton graph.
        graph = {ed[0]: [] for ed in edges}
        graph.update({ed[1]: [] for ed in edges})

        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])

        graph_backup = copy.deepcopy(graph)
        visited = set()

        def is_cyclic(edge) -> bool:
            visited.add(edge)

            while graph[edge]:
                # Remove visited graph.
                new_edge = graph[edge].pop()
                graph[new_edge].remove(edge)

                if new_edge in visited or is_cyclic(new_edge):
                    return True

            return False

        for ed in edges[::-1]:  # Loop inverse order.
            graph[ed[0]].remove(ed[1])
            graph[ed[1]].remove(ed[0])

            is_cycled = False
            for key in graph:
                if is_cyclic(key):
                    is_cycled = True

            if not is_cycled:
                return ed

            visited = set()
            graph = copy.deepcopy(graph_backup)

        return []
