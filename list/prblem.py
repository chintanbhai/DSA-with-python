if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # arr1 = map(int, arr)
    # print("Array : ",type(arr1) , [arr1 for arr1 in arr1]) 
    
    unique_scores = set(arr)
    print(unique_scores)
    
    sorted_scores = sorted(unique_scores, reverse=True)
    print(sorted_scores)
    
    runner_up_score = sorted_scores[1]
    
    print(runner_up_score)

#what is the use of map function in python? with example
#Map function is used to apply a function to all the items in an input_list.
#Syntax: map(function_to_apply, list_of_inputs)
#Example:
#def multiply(x):
#    return x * x
#
#numbers = (1, 2, 3, 4)
#result = map(multiply, numbers)
#print(list(result))
