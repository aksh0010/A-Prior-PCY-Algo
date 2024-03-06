def Apriori_Algorithm(data, support_threshold):
    """
    Generate frequent item sets using the Apriori algorithm.

    Parameters:
    - data: A list of lists, where each inner list represents a transaction.
    - support_threshold: An integer representing the minimum support count for an item set to be considered frequent.

    Returns:
    - frequent_pairs: A dictionary where keys are item pairs and values are their support counts.
    """
    # Calculate the frequency of each item
    
    
    #Below is our pass 1 as we know we need to count the frequent items  first before moving on to next steps
    frequency = {}
    for basket in data:
        for item in basket:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

    # Keep only the items that have a frequency greater than the support threshold
    frequent_items = {item for item, freq in frequency.items() if freq >= support_threshold}
   
    # Now we are moving to 2nd pass and thus we will generrate  all possible pair combinations from frequent_items set 
    # for possible pairs and then we will  check if they meet the condition meaning if they are in frequent _items or not
    
    # Find frequent pairs
    all__possible_pairs = {}
    for basket in data:
        # Get only the items that are in our frequent_items set
        #For each basket we are taking items, that are frequent
        items = [item for item in basket if item in frequent_items]

        #Now if items are frequent, then we start making pairs with other items and add them to the frequent_pair dictionary

        for i in range(len(items)): # For each item
            for j in range(i+1, len(items)): # For each next item
                pair = (items[i], items[j])  # Create the pair
                # If this pair exist in our all__possible_pairs dict then update the count
                if pair in all__possible_pairs:
                    all__possible_pairs[pair] += 1
                else: #If this pair doesn't exist yet in our all__possible_pairs dict then add it with a value of 1 
                    all__possible_pairs[pair] = 1

    

    # Keep only the pairs that have a frequency greater than the support threshold
    frequent_pairs = {pair: freq for pair, freq in all__possible_pairs.items() if freq >= support_threshold}

    # # Print the frequent item pairs
    # print("\nApriori : Your Frequent item pairs are ready\n")
    # print(frequent_pairs)
    # print("\n____________________________\n")

    return frequent_pairs
