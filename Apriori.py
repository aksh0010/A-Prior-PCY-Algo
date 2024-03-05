def apriori(data, support_threshold):
    # Calculate the frequency of each item
    frequency = {}
    for basket in data:
        for item in basket:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

    # Keep only the items that have a frequency greater than the support threshold
    frequent_items = {item for item, freq in frequency.items() if freq >= support_threshold}

    # Find frequent pairs
    frequent_pairs = {}
    for basket in data:
        # Get only the items that are in our frequent_items set
        items = [item for item in basket if item in frequent_items]

        # For each pair of items, increment the count in our frequent_pairs dictionary
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                pair = (items[i], items[j])
                if pair in frequent_pairs:
                    frequent_pairs[pair] += 1
                else:
                    frequent_pairs[pair] = 1
    # print(frequent_items)
    # Keep only the pairs that have a frequency greater than the support threshold
    frequent_pairs = {pair: freq for pair, freq in frequent_pairs.items() if freq >= support_threshold}
    print("\nYour Frequent item_pairs are ready\n")
    print(frequent_pairs)
    print("\n____________________________\n")
    return frequent_pairs