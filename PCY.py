import hashlib

#Creating hascode of the  string using sha256 algorithm. and then performing modulo
#As we know for hashfunction, we need the total number of possible buckets we need thus we need num_buckets

def hash_function(item, num_buckets):
    
    basket_from_hashing =int(hashlib.md5(str(item).encode()).hexdigest(), 16) % num_buckets
    return basket_from_hashing

def Multistage_Algorithm(data, support_threshold, num_buckets):
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
    #In the first pass, the algorithm counts the frequency of each item using a hash function.
    #It initializes an array frequency to keep track of the count of items hashed into each bucket.
    
    #Basically we are counting the frequncy of each bucket based on our hashfunction
    frequency = [0]*num_buckets
    for basket in data:
        for item in basket:
        
            basket_from_hashing = hash_function(item, num_buckets)

            frequency[basket_from_hashing] += 1

    # Second pass
    # In the second pass, the algorithm identifies frequent items based on the support threshold.
    # It goes through each basket again,
    # checks the count of the item in the frequency array, and determines if it's frequent.
    
    #Basically after we had our frequnecy of each basket, we  will go through that list
    # and fetch items from the frequent baskets
    frequent_items = {}
    for basket in data:
        for item in basket:
            # meaning if the bucket is frequent , then we add the item in our frequent items dict
            if frequency[hash_function(item, num_buckets)] >= support_threshold:
                if item in frequent_items:
                    frequent_items[item] += 1
                else:
                    frequent_items[item] = 1

    # Third pass
    # removing infrequent items based on the support threshold.
    
    #here we are removing false positivies by  checking how many times an item appears in the dataset
    #because we know in PCY, sometimes  due to collision some items may appear more than their actual value
    #so we need to check with the number of time they appeared in the list
    #and remove those which doesn't meet the criteria that is threshold
    #Basically  we remove all the items which are not frequent from  our frequent_items dictionary
    frequent_items = {item: freq for item, freq in frequent_items.items() if freq >= support_threshold}
    print("\nMULTISTAGE : Your Frequent item pairs are ready\n")
    print(frequent_items)
    print("\n____________________________\n")
    return frequent_items

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
            #first hashfunction call
            first_basket_from_hashing = hash_function(item, num_buckets)
            frequency1[first_basket_from_hashing] += 1
            
            #second hashfunction call 
            second_basket_from_hashing= hash_function(hash_function(item, num_buckets), num_buckets)
            frequency2[second_basket_from_hashing] += 1

    # Second pass
    
    #same as Multistage but below is different  because now we don't combine both array into one
    #we keep two separate array and use simple AND operation to fetch both frequent buckets then only adding items
    frequent_items = {}
    for basket in data:
        for item in basket:
            
            # meaning if both buckets are frequent , then only we fetch  the item and store it in our frequent items dict
            if frequency1[hash_function(item, num_buckets)] >= support_threshold and frequency2[hash_function(hash_function(item, num_buckets), num_buckets)] >= support_threshold:
                if item in frequent_items:
                    frequent_items[item] += 1
                else:
                    frequent_items[item] = 1

    # Filter out infrequent items
    #Same as Multistage 3rd pass
    frequent_items = {item: freq for item, freq in frequent_items.items() if freq >= support_threshold}
    print("\nMULTIHASH : Your Frequent item pairs are ready\n")
    print(frequent_items)
    print("\n____________________________\n")
    
    return frequent_items
