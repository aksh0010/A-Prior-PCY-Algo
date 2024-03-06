# Import the apriori function from the Apriori module
from Apriori import Apriori_Algorithm
from PCY import Multihash_Algorithm,Multistage_Algorithm
import random
import time
import matplotlib.pyplot as plt

try:
    # Open the file in read mode ('r')
    with open('retail.txt', 'r') as file:
        # Read the contents of the file and split each line into a list of items
        data = [[int(item) for item in line.strip().split()] for line in file]
except FileNotFoundError:
    print("File not found. Please check the file path.")
except ValueError:
    print("Invalid data format. Make sure all items in the file are integers.")
except UnicodeDecodeError:
    print("Unable to decode the file. Please check the file encoding.")

print(type(data))
# Define percentages and threshold percentages starts from 1 % , 5% and goes to 100%
percentages = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
threshold_percentages = [0.01,0.05, 0.1]  # Define your threshold percentages here starts from 1 % , 5% and 10%

Apriori_results = {}  # Initialize a dictionary to store results for each algorithms
Multistage_results={}
Multihash_results={}
Apriori_times = {}
Multistage_times = {}
Multihash_times = {}
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
            print(f'''Data size:{len(subset_data)}''')
            # Print information about the current data percentage and threshold percentage for logging
            print(f'''data_percentage:{data_percentage}''')
            print(f'''support_threshold:{support_threshold}''')
            # print("\nData:\n" + str(subset_data))
            
            Multihash_start_time = time.time()
            freq_pair_Multihash= Multihash_Algorithm(data=subset_data,support_threshold=support_threshold,num_buckets=600)
            Multihash_final_time = time.time()-Multihash_start_time
            Multihash_times[(data_percentage, threshold_percentage)] = Multihash_final_time
          
      
          
            # Calling the apriori function to find frequent item sets
            Apriori_start_time= time.time()
            freq_pairs_Apriori = Apriori_Algorithm(data=subset_data, support_threshold=support_threshold)
            Apriori_final_time = time.time()-Apriori_start_time
            Apriori_times[(data_percentage, threshold_percentage)] = Apriori_final_time
            
      
            Multistage_start_time= time.time()
            freq_pair_Multistage = Multistage_Algorithm(data=subset_data,support_threshold=support_threshold,num_buckets=600)
            Multistage_final_time = time.time()-Multistage_start_time
            Multistage_times[(data_percentage, threshold_percentage)] = Multistage_final_time
            
           
      
            # Store the results in a nested dictionary which stores  the frequency pairs along 
            # with data_percentage and  threshold_percentage
            # for plotting
            if data_percentage not in Apriori_results:
                Apriori_results[data_percentage] = {}
            Apriori_results[data_percentage][threshold_percentage] = freq_pairs_Apriori
            
            if data_percentage not in Multistage_results:
                Multistage_results[data_percentage] = {}
            Multistage_results[data_percentage][threshold_percentage] = freq_pair_Multistage
            
            if data_percentage not in Multihash_results:
                Multihash_results[data_percentage] = {}
            Multihash_results[data_percentage][threshold_percentage] = freq_pair_Multistage
    # Print a separator after processing one percentage for logging
    print("######################################### One dataset completed #########################################")

# print("Apriori Results\n")
# print(Apriori_results)
# print("Multistage Results\n")
# print(Multistage_results)
# print("MultiHash Results\n")
# print(Multihash_results)


print("Apriori Results\n")
print(Apriori_times)
print("Multistage Results\n")
print(Multistage_times)
print("MultiHash Results\n")
print(Multihash_times)



def plot_time_vs_dataset_fixed_threshold_combined(algorithm_times_apriori, algorithm_times_multistage, algorithm_times_multihash, threshold_percentage):
    """
    Plot the graph of time versus dataset size for all algorithms with a fixed threshold percentage.

    Parameters:
    - algorithm_times_apriori: A dictionary of times for Apriori algorithm.
    - algorithm_times_multistage: A dictionary of times for MultiStage algorithm.
    - algorithm_times_multihash: A dictionary of times for MultiHash algorithm.
    - threshold_percentage: A float representing the fixed threshold percentage.

    Returns:
    - None (displays the plot).
    """
    # Extract data percentages and times from the dictionaries for the fixed threshold
    data_percentages = sorted(set(key[0] for key in algorithm_times_apriori.keys()))
    times_apriori = [algorithm_times_apriori[(data_percentage, threshold_percentage)]
                     for data_percentage in data_percentages]
    times_multistage = [algorithm_times_multistage[(data_percentage, threshold_percentage)]
                        for data_percentage in data_percentages]
    times_multihash = [algorithm_times_multihash[(data_percentage, threshold_percentage)]
                       for data_percentage in data_percentages]

    # Plotting the graph
    plt.plot(data_percentages, times_apriori, marker='o', label='Apriori Algorithm')
    plt.plot(data_percentages, times_multistage, marker='o', label='MultiStage Algorithm')
    plt.plot(data_percentages, times_multihash, marker='o', label='MultiHash Algorithm')

    plt.xlabel('Data Percentage')
    plt.ylabel('Time (seconds)')
    plt.title(f'Time vs. Dataset Size for Algorithms (Threshold: {threshold_percentage})')
    plt.grid(True)
    plt.legend()
    plt.show()

# Plotting time versus dataset for all algorithms with a fixed threshold
plot_time_vs_dataset_fixed_threshold_combined(Apriori_times, Multistage_times, Multihash_times, 0.01)

# Plotting time versus dataset for all algorithms with a fixed threshold
plot_time_vs_dataset_fixed_threshold_combined(Apriori_times, Multistage_times, Multihash_times, 0.05)

# Plotting time versus dataset for all algorithms with a fixed threshold
plot_time_vs_dataset_fixed_threshold_combined(Apriori_times, Multistage_times, Multihash_times, 0.1)