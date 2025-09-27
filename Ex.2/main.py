symbol_quantity = 60*1000*2
i = 1
N = 2**i
while N < 33:
    i = i+1
    N = 2**i
text_quantity = i*symbol_quantity
print(text_quantity)
