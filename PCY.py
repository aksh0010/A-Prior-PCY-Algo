import hashlib

#Creating hascode of the  string using sha256 algorithm. and then performing modulo
#As we know for hashfunction, we need the total number of possible buckets we need thus we need num_buckets

def hash_function(item, num_buckets,seed=1):
  
   # Convert the item to a string for hashing
    item_str = str(item) + str(seed)
    # Use SHA-256 hashing algorithm
    hashed_item = hashlib.sha256(item_str.encode()).hexdigest()
    # Perform modulo with the number of buckets
    hash_value = int(hashed_item, 16) % num_buckets
    return hash_value

def Multistage_Algorithm(data, support_threshold, num_buckets):
    # First pass
      # Initialize the bucket counts
    bucket_counts = [0] * num_buckets

    # Iterate through the transactions and update bucket counts for pairs of items
    for basket in data:
        # Generate pairs of items
        pairs = [(item1, item2) for item1 in basket for item2 in basket if item1 < item2]

        # Hash each pair and update the corresponding bucket count
        for pair in pairs:
            hash_value = hash_function(pair, num_buckets)
            bucket_counts[hash_value] += 1
    
    # Second pass
    frequent_pairs = {}
     # Iterate through the transactions and count pairs that hash to frequent buckets
    for basket in data:
        # Generate pairs of items
        pairs = [(item1, item2) for item1 in basket for item2 in basket if item1 < item2]

        # Count pairs that hash to frequent buckets
        for pair in pairs:
            hash_value = hash_function(pair, num_buckets)
            if bucket_counts[hash_value] >= support_threshold:
                if pair in frequent_pairs:
                    frequent_pairs[pair] += 1
                else:
                    frequent_pairs[pair] = 1


    # Third pass
    # Filter out pairs that do not meet the support threshold
    frequent_pairs = {pair: count for pair, count in frequent_pairs.items() if count >= support_threshold}

    return frequent_pairs

def Multihash_Algorithm(data, support_threshold, num_buckets):
    """
    Generate frequent item sets using the MultiStage algorithm.

    Parameters:
    - data: A list of lists, where each inner list represents a transaction.
    - support_threshold: An integer representing the minimum support count for an item set to be considered frequent.
    -num_buckets :  The number of buckets to divide the items into when building candidate itemsets.
    
    Returns:
    - frequent_pairs: A dictionary where keys are item pairs and values are their support counts.
    """
    # First pass
    
    #same like the multistage , we are creating frequency array but we need 2 arrays as we have 2
    #different type of hashing functions here
    frequency1 = [0]*num_buckets
    frequency2 = [0]*num_buckets
    for basket in data:
        for item in basket:
            hash_value1 = hash_function(item, num_buckets, 1)
            hash_value2 = hash_function(item, num_buckets, 2)
            frequency1[hash_value1] += 1
            frequency2[hash_value2] += 1

    # Second pass
    
    #same as Multistage but below is different  because now we don't combine both array into one
    #we keep two separate array and use simple AND operation to fetch both frequent buckets then only adding items
    # Second pass: Count frequent items
    frequent_items = {}

    for basket in data:
        for item in basket:
            hash_value1 = hash_function(item, num_buckets, 1)
            hash_value2 = hash_function(item, num_buckets, 2)
            if frequency1[hash_value1] >= support_threshold and frequency2[hash_value2] >= support_threshold:
                if item in frequent_items:
                    frequent_items[item] += 1
                else:
                    frequent_items[item] = 1
    #Same as Multistage 3rd pass
    # Filter out infrequent items
    frequent_items = {item: freq for item, freq in frequent_items.items() if freq >= support_threshold}
    
    return frequent_items
    # Filter out infrequent items
    
   
    # print("\nMULTIHASH : Your Frequent item pairs are ready\n")
    # print(frequent_items)
    # print("\n____________________________\n")
    
