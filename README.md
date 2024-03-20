## Project 1- Comp 4250 Big Data

1.	Introduction :
The report presents the findings and experiments conducted as part of Project I in COMP-4250, focusing on mining frequent itemsets using the A-Priori and PCY algorithms(Multistage & MultiHash). The primary objective of this project was to analyze the efficiency and performance of these algorithms in discovering frequent pairs of elements within a retail dataset.

2.	Computer Specifications for this Experiment: 
Operating System: MS Windows 11 Home Version 23H2
CPU : Intel i7-9750H CPU @ 2.60 GHz
RAM:  16gb @ 2667 MHz

3.	Methodology
Algorithms: The implemented algorithms include the A-Priori, Multistage, and Multihash versions of the PCY algorithm.
Programming Language: Python 
Version Control: GitHub: aksh0010/A-Prior-PCY-Algo (github.com)
Experimental Setup :
-	I have created 2 modules ; 1 for Apriori (Apriori.py) and 1 for PCY’s(PCY.py) Extension ( Multistage & Multihash)
-	I have created a Launcher.py where I do the necessary imports from each module I created and then plot the graphs one by one on the exit of each graph.
-	Code runs on each chunk of data and for each chunk of data, it runs on all support threshold values.
    -	The support thresholds selected for evaluation were 1%, 5%, and 10%, representing different levels of stringency in identifying frequent items.
    -	Dataset Percentages: 1%, 5%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, and 100%.
    -	Results are then stored and Plotted using MatplotLib
    -	For Multistage and Multihash Algorithms, I have created a hash function using Hashlib’s sha256 to create a unique hashcode for unique items.
How to Run the code: Simply run the Launcher.py wait for a few minutes and let mining complete. Once the mining is complete you will see the first graph of the Support threshold 1%. Upon closing this graph, another will appear for 5%. When closing this graph, finally will see the last graph for the 10 % Support threshold.


4.	Algorithm Comparison: 
-	The performance comparison among the A-Priori, Multihash, and Multistage algorithms provided valuable insights into their efficiency and scalability for frequent itemset mining tasks. Surprisingly, the A-Priori algorithm emerged as the fastest across various support thresholds, followed by the Multihash algorithm, while the Multistage algorithm exhibited slower execution times.

-	The observed trend challenges conventional expectations, as the traditionally naive A-Priori algorithm outperformed the more optimized PCY variants in this specific context. This phenomenon underscores the importance of considering algorithmic characteristics and dataset properties in algorithm selection for frequent itemset mining tasks.

-	One plausible explanation for the observed trend is the varying computational time associated with the support threshold. As the support threshold increases, implying a stricter criterion for item set frequency, the workload per transaction diminishes, leading to faster execution times across all algorithms. However, the relative efficiency gains are more pronounced in the case of A-Priori due to its simpler traversal and candidate generation process.

-	Moreover, the PCY variants, particularly the Multistage algorithm, incur additional computational overhead in hash table management and multiple passes over the dataset, which becomes more apparent as the support threshold grows. This overhead contributes to comparatively slower execution times for PCY algorithms, especially in scenarios where the support threshold is relatively high.

-	Interestingly, as the support threshold escalates, the algorithms demonstrate improved efficiency, contrary to conventional expectations. This phenomenon can be attributed to various factors, including reduced candidate generation space, optimized hash table utilization, and streamlined transaction processing. Moreover, higher support thresholds necessitate a more stringent filtering process, resulting in fewer candidate item sets and expedited computation.

-	These observations highlight the intricate interplay between algorithm design, support threshold constraints, and computational resources in the context of frequent itemset mining. While A-Priori's efficiency in this scenario is notable, further investigation is warranted to explore the scalability and adaptability of different algorithms across diverse datasets and application domains.

-	The project successfully implemented and evaluated the A-Priori and PCY algorithms for mining frequent item sets. The findings underscore the importance of algorithm selection and optimization in big data analytics tasks. The Multistage and Multihash variants of the PCY algorithm offer promising avenues for efficient frequent itemset mining in large-scale datasets.

5.	Visuals 
Line charts were generated for time performance vs dataset sizes for each Algorithm on a fixed support threshold. The results indicated notable differences in execution times based on dataset sizes and thresholds. However, as mentioned earlier, in this case, I got Apriori running the fastest which is unlikely. 
Python’s Matplotlib was used to create the graphs of all 3 Algorithms.

   ![image](https://github.com/aksh0010/A-Prior-PCY-Algo/assets/68304244/e6d03dba-024b-4b00-9d39-6b95a4f23f18)

                                              Threshold 1 %
   ![image](https://github.com/aksh0010/A-Prior-PCY-Algo/assets/68304244/bc4011d9-e3c3-4936-acf1-cc99a244e060)

 
                                               Threshold 5 %

  ![image](https://github.com/aksh0010/A-Prior-PCY-Algo/assets/68304244/6bf69ebf-3ddd-4725-9fde-ab0345dc6cd7)

                                                Threshold 10 %

6.	Conclusion 
- In conclusion, frequent itemset mining algorithms such as Apriori and PCY’s extension, change their behavior when the data type and data size are varied. Fine-tuning the Multihash and Multistage variants of the PCY algorithm is equally crucial for enhancing their efficiency and scalability in frequent itemset mining tasks. While the A-Priori algorithm may exhibit superior performance in certain scenarios, optimizing the PCY extensions can unlock their full potential in handling larger datasets and stricter support threshold constraints. In the case of the PCY’s Extension algorithm, careful selection and fine-tuning of hash functions are pivotal for achieving optimal bucket distribution and reducing hash collision along with minimizing computations during hash table construction and itemset counting phases.

