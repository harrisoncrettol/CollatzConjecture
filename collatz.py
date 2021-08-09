from matplotlib import pyplot as plt
plt.figure(figsize=[8, 8])

# 3n + 1  -> graph the paths n has to take to reach 1

num = 5
stack = []


for i in range(2, num+1):
    n = i
    while n != 1:
        stack.append(n)
        if n % 2 != 0:
            n = n * 3 + 1
        else:
            n /= 2
    
    stack.append(n)
    x = list(range(len(stack)))
    print(stack, i)
    #plt.figure(figsize=([5, 5]))  # graphs plots one by one
    #plt.title("N = " + str(i)) 
    plt.plot(x, stack)
    stack = []

plt.title("Number = " + str(num))
plt.show()
