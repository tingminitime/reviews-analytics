data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: # %求餘數
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

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
