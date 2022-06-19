
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5] # python字串(str)可以視作清單(list)
	name = s[0][5:] # 走到結尾(=結尾值不寫)
	
	print(name)