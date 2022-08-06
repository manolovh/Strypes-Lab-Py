import sys

first_range = int(sys.argv[1])
second_range = int(sys.argv[2])

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

num_list = []
for i in range(20):
    num_list.append(fibonacci(i))

print(num_list[first_range-1:second_range+1])
