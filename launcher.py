from Apriori import apriori
import random

# Open the file in read mode ('r')
with open('retail.txt', 'r') as file:
    # Read the contents of the file
    data = [line.strip().split() for line in file]

# Define percentages and threshold percentages
percentages = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
threshold_percentages = [0.01, 0.05, 0.1, 0.5]  # Define your threshold percentages here

results = {}

for data_percentage in percentages:
    num_transactions = int(len(data) * data_percentage)
    subset_data = random.sample(data, num_transactions)
    if len(subset_data) == 0:
        print(f'''Data set is empty for data_percentage {data_percentage}''')
    else:
    # Perform your operations on subset_data
        
        for threshold_percentage in threshold_percentages:
            support_threshold = len(subset_data) * threshold_percentage
            
            print("data_percentage: " + str(data_percentage))
            print("threshold_percentage: " + str(support_threshold))
            print("\nData:\n" + str(subset_data))
            
            freq_pairs = apriori(data=subset_data, support_threshold=support_threshold)
            
            # Store the results in a nested dictionary
            if data_percentage not in results:
                results[data_percentage] = {}
            results[data_percentage][threshold_percentage] = freq_pairs

    print("#########################################One percentage done")