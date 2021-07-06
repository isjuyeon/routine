def isPowerOfFour(n):
    if n in [1, 4]:#1,4라는건 절대 1,2,3,4라는 말이 아니다.
        return True
    elif n <= 0:
        return False
    else:
        if n % 4 == 0:
            return isPowerOfFour(n // 4)
        else:
            return False
print(isPowerOfFour(48))