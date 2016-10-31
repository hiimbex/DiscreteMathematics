# def gcd(a,b):
#     """
#         Find the greatest common divisor
#     """
#     if not isinstance(a,int) or not isinstance(b,int):
#         return None
#
#     a,b=abs(a),abs(b)
#     a,b=max(a,b),min(a,b)
#
#     while b!=0:
#         a,b=b,a%b
#
#     return a

def gcd(m,n):
	m,n=abs(m),abs(n)
	m,n=max(m,n),min(m,n)
	mm,nn=m,n #Keep original values
	M=[1,0]
	N=[0,1]
	while n != 0:
		q,r=m//n,m%n
		M[0],N[0]=N[0],M[0]-N[0]*q
		M[1],N[1]=N[1],M[1]-N[1]*q
		m,n=n,r
	print("{:d}*{:d}+{:d}*{:d}={:d}".format(M[0],mm,M[1],nn,m))
	return "this is the inverse: ", M[1]

def main():
    userInputA = input("Input a number (then hit enter): ")
    userInputB = input("Input a second number (then hit enter): ")
    return gcd(userInputA, userInputB)

print main()