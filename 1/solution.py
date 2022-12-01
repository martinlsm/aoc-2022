import heapq

inp = open('input', 'r')

total_weights = []
nums = [0]
res = 0
for line in inp:
    line = line.strip()
    if len(line) == 0:
        total_weights.append(sum(nums))
        nums = []
        continue
    nums.append(int(line))

inp.close()

total_weights.append(sum(nums))

heapq._heapify_max(total_weights)

n1 = heapq.heappop(total_weights)
heapq._heapify_max(total_weights)
n2 = heapq.heappop(total_weights)
heapq._heapify_max(total_weights)
n3 = heapq.heappop(total_weights)

print(n1 + n2 + n3)
