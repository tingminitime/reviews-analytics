data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 100000 == 0: # %求餘數
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])

#文字計數
word_count = {}
for d in data:
	words = d.split() # split預設值是空白鍵
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

# print(len(word_count))
# print(word_count['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in word_count:
		print(word, '出現過的次數為: ',word_count[word])
	else:
		print('這個字沒有出現在留言中喔!')
print('感謝使用本查詢功能')

sum_len = 0
new = []
# good = []
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
	# print(sum_len)

	if len(d) < 100: # 把長度低於100的留言裝至new清單
		new.append(d)

	# if 'good' in d:
	# 	good.append(d)

print('留言的平均長度為', sum_len / len(data))
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
# print('一共有', len(good), '筆留言含有good')

good = [1 for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data] # 運算
print(bad)
# bad = []
# for d in data:
# 	bad.append('bad' in d)
