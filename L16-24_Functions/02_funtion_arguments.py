def add(a,b,plus=0): #a,b are positioned arguments , agar plus = 0 nhi likhoge too ( plus ke equals me kuch likhna padega nhi too error ayega) these are called default arguments., positioned arguments ke baad he likhe jynge default arguments like at the very end.     
    return a+b*plus

c = add(3,5,2) # 2 likhne se plus is value overwritten ki jaa skti hain.
print(c)

c1 = add(b=5, a=3) # keyword arguments