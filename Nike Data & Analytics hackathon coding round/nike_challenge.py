def nike_challenge_solution():
	ip = input() 
	ip = ip.split(' ')
	(N, cash) = (int(ip[0]), int(ip[1])) # Convert to integer
	prices = input()
	try:
    		prices = prices.split(' ')
    		prices = sorted(list(map(int,prices))) # Sort prices in ascending order
	except:
    		prices = list(int(prices)) # If just one item, append it into an empty list
	count = 0
	if cash <= 0:
     		print(0) 
     		return 0 # If there is no cash, 0 objects can be bought

	while cash > 0:
    		for i in range(len(prices)):
        		#print(cash, prices[i])
        		if (cash - prices[i]) < 0: # If current object can't be bought, cash is exhausted
            			cash = -1
            			print(count)
						break
        		else:
            			cash -= prices[i] # If we can buy the object, reduce the cash reserve
            			count += 1 # Increment counter for objects bought
	return count

nike_challenge_solution()