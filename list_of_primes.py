#function to find prime numbers
def isPrime(num):

    for i in range(2, num):
        if (num%i) == 0:
            return False
    return True

#create a list to hold primes
def getPrimes(num_max):

    list_of_primes = []

    for i in range(2, num_max):
        if isPrime(i):
            list_of_primes.append(i)
    return list_of_primes

number = int(input("Search for primes up to: "))
list_of_primes = getPrimes(number)

print(list_of_primes)