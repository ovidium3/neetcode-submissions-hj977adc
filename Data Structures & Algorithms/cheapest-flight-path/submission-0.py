class Solution: # O(E * k) time
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # weighted, directed graph - dijkstra's? run a BFS with minHeap PQ? not as easy since k stops limitation
        # Bellman-Ford algo - CAN incorporate at most k stops and do it efficiently. and negative weights (doesnt matter here)
        # usually runs in O(E * V) but since we only have k stops no point checking all
        # time complexity is the same as regular BFS, plus it is readable and easy to implement
        # not worth the slight performance boost for a lot of extra complication
        INF = float("inf") # positive infinity signifying unreachable node
        prices = [INF] * n # init prices array of source node to all other nodes
        prices[src] = 0 # dist to itself is 0

        for i in range(k + 1): # k + 1 layers since k stops means k + 1 flights between src and dst
            tempPrices = prices.copy() # where were gonna update, because of the k restriction we dont overwrite original
            for source, dest, price in flights: # need to check each edge
                if prices[source] != INF: # skip unreachable nodes
                    if prices[source] + price < tempPrices[dest]: # check if new cheapest path exists
                        tempPrices[dest] = prices[source] + price
            prices = tempPrices # update prices after checking conditions

        return prices[dst] if prices[dst] != INF else -1