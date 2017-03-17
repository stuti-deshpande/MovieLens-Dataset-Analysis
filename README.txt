Name:Stuti Deshpande

Performed following tasks:
--Developed MapReduce jobs to compute the frequency of co-occurrence for every pair of movies that receive a "High" ranking (4-5 star rating) from the same user using both Pairs and Stripes approach and emitted most frequent 20 pairs.

--Computed the conditional probability(or relative frequency) P(MovieB | MovieA) and emitted movie names in pairs whose conditional probability is greater than 0.8. This approach can be used as a primitive way to recommend movieB to customers that rent movieA and liked it.

--Computed the Lift between two movies and emitted pairs whose lift is greater than 1.5. 
Lift is a measure of the effectiveness of a predictive model (or association rule) calculated as the ratio between the results obtained with and without the predictive model.

--Implemented the SON algorithm in MapReduce which uses the Apriori Algorithm to compute all itemsets (groups of movies) that frequently receive high ranking by users. Implemented this by chaining the output of Apriori Algorithm (using MapReduce) to the SON algorithm.

--All the task in this project were implemented using Python, executed using MapReduce on Hadoop using Hadoop Streaming. Used all the datasets namely MovieLens 100K, MovieLens 1M and MovieLens 10M to perform the below mentioned tasks. Created multiple shell scripts for each task to run the MapReduce jobs on various data sizes and recorded the running times. Then, created graphs for each task showing running time vs the data size.

1. The zipped file contains one folder which contains 3 folders : Code, Pseuodocode  and Output folders
2. The output folder contains the output file for Task-1 and the graphs for the Task-1
3. The folder named "Code" has 4 subfolders
    1. The folder Map-Reduce-Hadoop contains python scripts for pairs and stripes in Hadoop
    2. The folder Map-Reduce-Spark contains python scripts for pairs and stripes in Spark
    3. The folder Conditional Probability contains the python script for calculating the same in spark
    4. The folder Lift contains the python script to calculate lift
3. The folder named "Pseudocode" has 4 subfolders
    1. The folder Map-Reduce-Hadoop contains pseudocode for pairs and stripes in Hadoop
    2. The folder Map-Reduce-Spark contains pseudocode for pairs and stripes in Spark
    3. The folder Conditional Probability contains the pseudocode for the python script calculating the same in spark
    4. The folder Lift contains the pseudocode to calculate lift 

Conclusion: According to the graphs plotted for the runtimes for hadoop and spark for both pairs and stripes approach, it can be seen that stripes approach is more time-efficient than the pairs approach
