class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        max_stop = max(max(route) for route in routes)
        if max_stop<target:
            return -1

        n = len(routes)
        buses = [float('inf')] * (max_stop + 1)
        buses[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                minn = float('inf')
                for stop in route:
                    minn = min(minn, buses[stop])
                minn +=1
                for stop in route:
                    if buses[stop] > minn:
                        buses[stop] = minn
                        flag = True
        return buses[target] if buses[target] < float('inf') else -1
