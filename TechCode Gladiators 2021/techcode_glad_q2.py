import math

def is_prime(n):
   if n <= 1:
      return False
   elif n == 2:
      return True
   elif n > 2 and n % 2 == 0:
      return False
   else:
      for i in range(3, int(math.sqrt(n)) + 1, 2):
         if n % i == 0:
            return False
      return True

def solution_prime_game():
	N = int(input())
	num_ranges = []
	for i in range(N):
		num_ranges.append(input())
	for i in range(len(num_ranges)):
    		cur = num_ranges[i].split(' ')
    		(start, end) = (int(cur[0]), int(cur[1]))
    		primes = []
    		for j in range(start, end+1):
        		if is_prime(j):
            			primes.append(j)
    		if len(primes) == 0:
        		print(-1)
    		elif len(primes) == 1:
        		print(0)
    		else:
       			print(primes[-1] - primes[0])

solution_prime_game()