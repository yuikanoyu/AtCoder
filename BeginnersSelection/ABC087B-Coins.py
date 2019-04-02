class coins:
	def __init__(self, count_500, count_100, count_50):
		self.count_500 = count_500
		self.count_100 = count_100
		self.count_50 = count_50
	def price(self, count_500=0, count_100=0, count_50=0):
		return count_500 * 500 + count_100 * 100 + count_50 * 50

coins = coins(int(input()),int(input()),int(input()))
target_price = int(input())
pattern_count = 0

for i in range(coins.count_500+1):
	if target_price < coins.price(i):
		#print("count:{}, 500:{}, price:{}".format(pattern_count,i,coins.price(i)))
		break
	for j in range(coins.count_100+1):
		if target_price < coins.price(i,j):
			#print("count:{}, 500:{}, 100:{}, price:{}".format(pattern_count,i,j,coins.price(i,j)))
			break
		for k in range(coins.count_50+1):
			if target_price < coins.price(i,j,k):
				#print("count:{}, 500:{}, 100:{}, 50:{}, price:{}".format(pattern_count,i,j,k,coins.price(i,j,k)))
				break
			if target_price == coins.price(i,j,k):
				pattern_count += 1
print("{}".format(pattern_count))