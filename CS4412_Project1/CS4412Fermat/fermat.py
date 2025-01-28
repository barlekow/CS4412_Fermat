import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


#def mod_exp(x, y, N):
    # Based on the pseudoocde in Figure 1.4
 #   if y == 0:
  #      return 1

   # z = mod_exp(x, y//2, N)
    #if (y % 2 == 0):
     #   return z**2 % N

    #return (x*z**2) % N

def mod_exp(x, y, N):
    result = 1
    base = x % N
    while y > 0:
        if (y % 2 == 1):  # If y is odd, multiply the base with the result
            result = (result * base) % N
        base = (base * base) % N  # Square the base
        y = y // 2
    return result


def fprobability(k):
    # p_failure is the probablity of a 'non-prime' number
    # returning 'yes' (ie. bypassing the test)
    # based on the discussion
    p_failure = 1 / (2**k)
    return 1.0 - p_failure


def mprobability(k):
    # You will need to implement this function and change the return value.

    # Probablity that a random number will not fail miller_rabin test
    # test will result "composite"
    p_composite_miller_rabin = 3/4

    # p_failure is the probablity of a non-prime random number considered 'prime'
    # in all k tests
    p_failure = (1-p_composite_miller_rabin)**k
    return 1 - p_failure


def fermat(N, k):

    for _ in range(k):
        a = random.randint(1, N-1)
        r = (a ** (N-1)) % N
        if r != 1:
            return 'composite'
    return 'prime'

def fermat_probability(k):
    return 1 - (1 / (2 ** k))

def miller_rabin(N, k):

    # if N=1 it's not prime
    if N == 1:
        return 'composite'

    # repeat at most k times
    for _ in range(k):

        # generate random number
        a = random.randint(1, N-1)

        y = N-1
        # if (N-1) is odd do one test
        if (y % 2 == 1):  # odd
            c = mod_exp(a, y, N)
            if (c == 1) or (c == (N-1)):
                # you passed the test
                continue
            else:
                # the modulo result is not 1
                return 'composite'

        # if N-1 is even
        while (y % 2 == 0):
            c = mod_exp(a, y, N)

            # passed the test
            if c == N-1:
                break

            # failed, the number is composed
            if c != 1:
                return 'composite'

            # square root in the next iteration
            y = y // 2

    return 'prime'

"""
# CUSTOM TEST SECTION
if __name__ == '__main__':
    N = 51
    k = 3
    print(f"fermat({N}, {k}): {fermat(N, k)}")

    x, y, N = 5, 3, 13
    x, y, N = 4, 40, 13
    x, y, N = 3, 96, 97
    print(f"mod_exp({x}, {y}, {N}): {mod_exp(x, y, N)}")

    pn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    N, k = 561, 100
    print(f"miller_rabin({N}, {k}): {miller_rabin(N, k)}")

    for N in range(2, 20):
        print(f"miller_rabin({N}, {k}): {miller_rabin(N, k)}")

    print(">> Fprobablitly:")
    for k in range(2, 10):
        print(f"fprobability({k}): {fprobability(k)}")

    print(">> Mprobablitly:")

    for k in range(2, 10):
        print(f"mprobability({k}): {mprobability(k)}")

"""