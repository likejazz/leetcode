# 399-evaluate-division.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Make bidirectional skeleton graph.
        graph = {e[0]: [] for e in equations}
        graph.update({e[1]: [] for e in equations})

        for k, v in enumerate(equations):
            graph[v[0]].append({v[1]: values[k]})
            graph[v[1]].append({v[0]: 1 / values[k]})

        answers = []

        def dfs(fr, to, answer) -> bool:
            if fr not in graph:
                return False

            if fr == to:
                answers.append(answer)
                return True

            # Calculate multiplication via graph order.
            while graph[fr]:
                to_list = graph[fr].pop()
                key = list(to_list.keys())[0]

                answer *= to_list[key]
                if dfs(key, to, answer):
                    return True
                answer /= to_list[key]
            return False

        for q in queries:
            graph_backup = copy.deepcopy(graph)
            # Start dfs to find two variables given.
            if not dfs(q[0], q[1], answer=1):
                answers.append(-1)
            graph = graph_backup

        return answers
