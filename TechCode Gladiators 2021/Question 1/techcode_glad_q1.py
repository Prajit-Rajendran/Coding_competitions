def solution_virus_outbreak():
	V = input()
	n = int(input())
	
	for i in range(n):
    		cur = input()

	words = cur.split(' ')

	for i in range(n):
    		cur = words[i]
    		V_cur = V
    		print(i, cur, V_cur)
    		flag = 0
    		for c in cur:
        		try:
            			idx = V_cur.index(cur[0])
       			except:
            			flag = 1
            			break
        		if len(cur) > 1:
            			cur = cur[1:]
            			V_cur = V_cur[idx:]
    		if flag == 0:
        		print('POSITIVE')
			return 'POSITIVE'
    		else:
        		print('NEGATIVE')
			return 'NEGATIVE'