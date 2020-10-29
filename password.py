import random
comb = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-'
tech21 = 16
p = ''.join(random.sample(comb, tech21))
print(p)