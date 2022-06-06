n= 3
print(n)
bits = f'{n:032b}'
print(bits)

m = ''.join(["1" if i=='0' else '0' for i in bits])
print(m)

mint = int(m,32)
print(mint)

