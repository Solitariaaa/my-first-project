def find_prime(n):
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n+ 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def min_additional_cards(cardTypes):
    max_value = max(cardTypes)
    primes = find_prime(max_value)
    min_additional = float('inf')
    
    for prime in primes:
        additional = 0
        for num in cardTypes:
            remainder = num % prime
            if remainder != 0:
                additional += (prime - remainder)
        min_additional = min(min_additional, additional)
    
    return min_additional

# Test cases
test_cases = [
    [4, 7, 5, 11, 15],
    [10, 20, 30, 40, 50],
    [5, 5, 5, 5, 10],
    [17, 23, 29, 31, 37],
    [2, 3, 4, 5, 6, 7, 8, 9, 10]
]

# Running test cases
results = {tuple(tc): min_additional_cards(tc) for tc in test_cases}
print(results)


def getMaxGoodSubarrayLength(limit, financialMetrics):
    n = len(financialMetrics)
    
    left = [-1] * n
    right = [n] * n
    
    # 使用单调栈找到每个元素的左边界
    stack = []
    for i in range(n):
        while stack and financialMetrics[stack[-1]] >= financialMetrics[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    
    # 使用单调栈找到每个元素的右边界
    stack = []
    for i in range(n):
        while stack and financialMetrics[stack[-1]] >= financialMetrics[i]:
            right[stack[-1]] = i
            stack.pop()
        stack.append(i)
    
    max_length = -1
    for i in range(n):
        length = right[i] - left[i] - 1
        if financialMetrics[i] * length > limit:
            max_length = max(max_length, length)
    
    return max_length

# 示例
n = 5
limit = 6
financialMetrics = [1, 3, 4, 3, 1]
print(getMaxGoodSubarrayLength(limit, financialMetrics))  # 输出: 3

