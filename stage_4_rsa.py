import random
import math

"""======================================================"""
#ENCRYPTION

def binary(n):
    #returns string
    
    return bin(n)[2:]


def S_and_M_mod(a,power,mod):
    #square and multiply algorithm
    #a^power mod(smth)
    bin_power = binary(power)
    answer,unit = a%mod,a%mod

    for i in bin_power[1:]:
        answer= (answer*answer)%mod

        if i == "1":
            answer = (answer*unit)%mod

    return answer


def miillerTest(d, n):
     
    a = 2 + random.randint(1, n - 4);
 
    x = S_and_M_mod(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 

    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    return False;




def isPrime( n, k):
     
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;


#Pollard Rho's Algorithm for prime factorise

def PollardRho(n):
    if isPrime(n,6):
        return n

    else:
        if (n == 1):
            return n
     
        if (n % 2 == 0):
            return 2
     
        x = (random.randint(0, 2) % (n - 2))
        y = x
        c = (random.randint(0, 1) % (n - 1))
        d = 1
     
        while (d == 1):
            x = (S_and_M_mod(x, 2, n) + c + n)%n
            y = (S_and_M_mod(y, 2, n) + c + n)%n
            y = (S_and_M_mod(y, 2, n) + c + n)%n
     
            d = math.gcd(abs(x - y), n)
            if (d == n):
                return PollardRho(n)
         
        return PollardRho(d)


def prime_fact(n):
    
    res = {}
    k = PollardRho(n)
    
    while n!=1:
        
        res[k] = res.get(k,0)+1
        n//=k
        k = PollardRho(n)

    return res
    


def phi(n):
    
    ans = 1
    prime_factorisation = prime_fact(n)

    for i in prime_factorisation:
        a = i-1
        b = (i**(prime_factorisation[i]-1))
        ans *= (a*b)

    return ans


"""
RULES
m: original message 
n: mod
m < n so that m (mod n) gives back m
gcd(m,n) = 1

e: public key
gcd(e,phi(n)) = 1

SUGGESTIONS
n = product of large primes
e = large prime
"""


#the following hint from previous stage gives e which is a prime
hint = "DROP 20!"
e = 1
for i in hint:
  e *= ord(i)
e+=1
#e = 89313067008001 (this is prime)



#the following code gives m
m = ''
for i in "bR0ncODe":
  m+= str(ord(i))
#m = 988248110997968101
m = int(m)
print(m)




  
n = 9576890767*3628273133*2860486313
#n = 99394964034952494350006468443



phi_n = (9576890767-1)*(3628273133-1)*(2860486313-1)
#phi_n = 99394963962431728301618554944



#the following code gives ciphertext
ciphertext = S_and_M_mod(m,e,n)
#ciphertext = 88381628651586574911841376827
print(ciphertext)

"""======================================================"""
#DECRYPTION

#STEPS FOR DECIPHERING

#1. get phi(phi(n)) 
phi_phi_n = phi(phi(n))
#phi_phi_n = 27297576748519940487905280000


#2. get d mod(phi(n))
#d = e ^ [ phi(phi(n))-1 ]
x = S_and_M_mod(e,phi_phi_n-1,phi_n)
#x = 72564138096003579802585609153


#3. get back message (m) by taking ciphertext^d mod(n)
text = S_and_M_mod(ciphertext,x,n)
# m = 988248110997968101


#4. Use ASCII to convert to letters
def num_to_text(n):
    x = str(n)
    y= []
    i = 0
    text = ''
    
    while i < len(x):
        y.append(i)
        if x[i] == "1":
            i+= 3
        else:
            i+= 2
            
    y.append(len(x))
    
    for i in range(len(y)-1):
        text += chr(int(x[y[i]:y[i+1]]))
    
    return text

#text = "bR0ncODe"



      
      
  
  

  









