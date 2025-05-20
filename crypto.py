import math
import random



def isPrime(n):
	"""
	Function takes a number n and returns True if prime or False if not.
	"""
	if n == 0 or n == 1:
		return False
	sroot = math.floor(n ** .5)
	result = True
	for i in range(2,sroot+1):	#python ranges mean you have to add 1 to include sroot
		if n % i == 0:
			result = False	#result is true iff n % i == 0 for all iterations
	return result


def legendre(a,p):
	return (a**((p-1)/2))%p


def millerRabinTest(n,k = 2): #return true if n is probably prime, false if witness found (n is composite)
	s = 0
	y = None
	v = n-1
	if n%2 == 0:
		return False
	else:
		for i in range(k):
			a = random.randint(2,n-2)
			pwr = factor2(v)
			odd= int(v/(2**pwr))
			print(a,pwr,odd)
			x = (a**odd)%n
			for j in range(pwr):
				y = (x**2)%n
				if y == 1 and x != 1 and x != (n-1):
					return False
				x = y
			if y != 1:
				return False
		return True


def factor2(n):#factors powers of two out, returns highest power of 2 factor
	r = 0		#fix this
	while n % 2 == 1:
		n = n % 2
		r += 1
	return r

def factorialMod(a,n): #factorial mod n
	return (a*math.factorial(a-1))%n

def L(n):
	return math.e**(math.sqrt(math.log(n)*math.log(math.log(n))))

def pollard(n,a = 2):
	g = 1
	i = 1
	while g == 1:
		#val = a**math.factorial(i)
		val = a**factorialMod(i,n) #more efficient calculation
		g = math.gcd(val-1,n)
		i += 1
		print(i, a**factorialMod(i,n)) #debug
	if g == n:
		return 0
	else:
		return g, int(n/g)

def  main():
	#userinput = int(input("giv number to factor: "))
	#print(pollard(userinput))
	#print(str(millerRabinTest(377)))
	print(pollard(199*23))
	return 0


#if __name__ == "__main__":
#	main()
