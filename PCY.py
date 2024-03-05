import hashlib

def hash_function(item, num_buckets):
    return int(hashlib.md5(str(item).encode()).hexdigest(), 16) % num_buckets

def Multistage(data, support_threshold, num_buckets):
    # First pass
    frequency = [0]*num_buckets
    for basket in data:
        for item in basket:
            frequency[hash_function(item, num_buckets)] += 1

    # Second pass
    frequent_items = {}
    for basket in data:
        for item in basket:
            if frequency[hash_function(item, num_buckets)] >= support_threshold:
                if item in frequent_items:
                    frequent_items[item] += 1
                else:
                    frequent_items[item] = 1

    # Third pass
    frequent_items = {item: freq for item, freq in frequent_items.items() if freq >= support_threshold}

    return frequent_items

def Multihash(data, support_threshold, num_buckets):
    # First pass
    frequency1 = [0]*num_buckets
    frequency2 = [0]*num_buckets
    for basket in data:
        for item in basket:
            frequency1[hash_function(item, num_buckets)] += 1
            frequency2[hash_function(hash_function(item, num_buckets), num_buckets)] += 1

    # Second pass
    frequent_items = {}
    for basket in data:
        for item in basket:
            if frequency1[hash_function(item, num_buckets)] >= support_threshold and frequency2[hash_function(hash_function(item, num_buckets), num_buckets)] >= support_threshold:
                if item in frequent_items:
                    frequent_items[item] += 1
                else:
                    frequent_items[item] = 1

    # Filter out infrequent items
    frequent_items = {item: freq for item, freq in frequent_items.items() if freq >= support_threshold}

    return frequent_items
