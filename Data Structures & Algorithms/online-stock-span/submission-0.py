class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        pointer = len(self.stack) - 1
        start = pointer
        while pointer >= 0:
            if self.stack[pointer] <= price:
                pointer -= 1
            else:
                break
        self.stack.append(price)
        return start - pointer + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)