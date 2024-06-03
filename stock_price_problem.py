# Given an array prices[] of length N, representing the prices of the stocks on different days
# the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.
# Note: Stock must be bought before being sold.

# Input: prices[] = {7, 1, 5, 3, 6, 4}
# Output: 5
# Explanation:
# The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
# Therefore, maximum possible profit = 6 – 1 = 5. 

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.


x=[7,8,9,11,20]

def stock(x):
    contain_least=x[0]
    for i in range(0,len(x)):
        if x[i]<contain_least:
            contain_least=x[i]
        else:
            pass
    print(f"The stock was the cheapest on day {x.index(contain_least)+1}")
    contain_max=x[x.index(contain_least)]
    for j in range(x.index(contain_least),len(x)):
        if x[j]>contain_max:
            contain_max=x[j]
        else:
            pass
    if contain_max==contain_least:
        print("The Stock Prices are in a decreasing order, hence the problem cannot be solved with this array")
    else:
        print(f"The stock was the costliest on day {x.index(contain_max)+1}\n")
        print(f"Maximum Possible Profit on basis of the costs = {(contain_max)-(contain_least)}")

stock(x)
        
    
    




