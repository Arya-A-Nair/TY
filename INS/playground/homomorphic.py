def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

p=13
q=17
n=p*q
phi=(p-1)*(q-1)

def lx(x):
    y=(x-1)/n
    return int(y)

g=1+n
lmbda=phi*1
mu=pow(phi,-1,n)
print(f"private key: {lmbda}")
print(f"public key- {g}")

def encrypt(m,r):
    c=(pow(g,m,n*n)*pow(r,n,n*n))%(n*n)
    return c

def decrypt(c):
    p=(lx(pow(c,lmbda,n*n))*mu)%n
    return p



# homormorphic features for addition
m1=123
r1=56

m2=37
r2=90

c1=encrypt(m1,r1)
c2=encrypt(m2,r2)
print((c1*c2)%(n*n))
print(encrypt(m1+m2,r1*r2))
