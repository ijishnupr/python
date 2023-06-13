import random
array = ['a','e','i','o','u']
possible = [['aeiou']]

q = 1
print("possible combination of 'a','e','i','o','u'")
print(''.join(array))
while q <120:
	random.shuffle(array)
	for x in possible:
		if ''.join(array) not in possible:
			possible.append(''.join(list(array)))
			print(''.join(array))
			q += 1
