
from random import randint

def bubblesort(arr, key=lambda x:x):
	ret = arr # .copy()
	for i in range(len(ret)-1):
		for j in range(len(ret)-i-1):
			if key(ret[j]) > key(ret[j+1]):
				ret[j], ret[j+1] = ret[j+1], ret[j]
	return ret

"""
def __quicksort_part(arr, l, h, key: callable = None):
	if key is None:
		key = lambda x: x
	
	p = key(arr[h])

	i = l

	for j in range(l, h):
		if key(arr[j]) <= p:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	
	arr[i], arr[h] = arr[h], arr[i]
	return i
"""

def quicksort_part(arr, l, h, key = None):
	if key is None:
		key = lambda x: x
	
	p = key(arr[l])

	i = l - 1
	j = h + 1

	while True:
		i += 1
		while key(arr[i]) < p:
			i += 1
		
		j -= 1
		while key(arr[j]) > p:
			j -= 1
		
		if i >= j:
			return j
		
		arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, l = 0, h = None, key = None):
	if h is None:
		h = len(arr)-1
	
	if l >= h or l < 0:
		return
	
	p = quicksort_part(arr, l, h, key=key)

	quicksort(arr, l, p-1, key=key)
	quicksort(arr, p+1, h, key=key)

"""
data = [randint(0,100) for i in range(100)]

quicksort(data, key=lambda x: -x)

# print(quicksort(data))
print(data)
"""