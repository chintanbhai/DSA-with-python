if __name__ == '__main__':
    # Initialize an empty list to store names and scores
    List = []
    
    # Read the input data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        List.append([name, score])
    
    # Extract scores from the nested list
    scores = [score for name, score in List]

    print("Scores : ", scores)
    
    unique_scores = sorted(set(scores))
    
    second_lowest_score = unique_scores[1]
    
    second_lowest_names = [name for name, score in List if score == second_lowest_score]
    
    second_lowest_names.sort()
    
    for name in second_lowest_names:
        print(name)
