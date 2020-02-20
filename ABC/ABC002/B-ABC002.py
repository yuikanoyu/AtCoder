ng_list = ['a','i','u','e','o']
w = input()
output = ''
for c in w:
	if c not in ng_list:
		output+=c
print(output)