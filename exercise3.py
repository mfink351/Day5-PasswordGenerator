target = int(input())
sum = 0

for i in range(0, target+1):
  if i % 2 == 0:
    sum += i

print(f"Sum of all integers 0 to {target} is {sum}.")