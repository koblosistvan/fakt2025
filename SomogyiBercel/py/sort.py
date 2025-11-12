
from random import randint

def bubblesort(arr):
	ret = arr.copy()
	for i in range(len(ret)-1):
		for j in range(len(ret)-i-1):
			if ret[j] > ret[j+1]:
				ret[j], ret[j+1] = ret[j+1], ret[j]
	return ret


data = [randint(0,100) for i in range(100)]

print(data)

print(bubblesort(data))
