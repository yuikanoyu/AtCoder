word_list = [ 'dream','dreamer','erase','eraser' ]
s = input()
char_count = len(s)
result_message = 'NO'

end_flag = False
while not end_flag:
	for word in word_list:
		word_len = len(word)
		if s[char_count-word_len:char_count] == word:
			char_count -= word_len
			if char_count == 0:
				result_message = 'YES'
				end_flag = True
			break
		elif word == word_list[-1]:
			end_flag = True
		else:
			pass
print(result_message)