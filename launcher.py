# Import the apriori function from the Apriori module
from Apriori import apriori
import random

# Open the file in read mode ('r')
with open('retail.txt', 'r') as file:
    # Read the contents of the file and split each line into a list of items
    data = [line.strip().split() for line in file]

# Define percentages and threshold percentages
percentages = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
threshold_percentages = [0.01, 0.05, 0.1, 0.5]  # Define your threshold percentages here

results = {}  # Initialize a dictionary to store results

# Loop through each percentage
for data_percentage in percentages:
    # Calculate the number of transactions based on the percentage of data
    num_transactions = int(len(data) * data_percentage)
    
    # Randomly select a subset of data for this percentage
    subset_data = random.sample(data, num_transactions)
    
    # Check if the subset_data is empty if so we dont need to process it
    if len(subset_data) == 0:
        print(f"Data set is empty for data_percentage {data_percentage}")
    else:
        # Loop through each threshold percentage
        for threshold_percentage in threshold_percentages:
            # Calculate the support threshold based on the length of the subset data and threshold percentage
            support_threshold = len(subset_data) * threshold_percentage
            
            # Print information about the current data percentage and threshold percentage for logging
            print("data_percentage: " + str(data_percentage))
            print("threshold_percentage: " + str(support_threshold))
            print("\nData:\n" + str(subset_data))
            
            # Calling the apriori function to find frequent item sets
            freq_pairs = apriori(data=subset_data, support_threshold=support_threshold)
            
            # Store the results in a nested dictionary which stores  the frequency pairs along 
            # with data_percentage and  threshold_percentage
            # for plotting
            if data_percentage not in results:
                results[data_percentage] = {}
            results[data_percentage][threshold_percentage] = freq_pairs

    # Print a separator after processing one percentage for logging
    print("#########################################One percentage done")


print(results)