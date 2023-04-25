## Data Analytics with Hadoop Programming Assignment

### Problem Statement

Count the number of times a word appears in the document. Develop a MapReduce framework based on Python threads. The data will be read from a file, stored in-memory and will run on a single computer.

<img src = "https://github.com/vedanthv/map-reduce-python/blob/master/map-reduce.jpg">

### Why Shuffle?

For example the results from a map need to be shuffled before being sent to reduce processes: if the two instances of the word ‘Apple’ were sent to distinct reduce processes, the count would not be correct.

### Requirements

- [x] Import text file
- [x] Data Cleaning
- [x] Split Data in Parts   
- [x] Implement the Map Function
- [ ] Implement the Shuffle Function
- [x] Implement the Reduce Function
- [ ] Document the project
- [x] Add requirements.txt file

### How to Run?

- Change the path for the input text in ```implementation.py```. Feel free to use your data as well.

- Run ```pipreqs requirements.txt``` to install the packages.

- Run ```python implementation.py``` to run the code and generate the output csv file.

### Output Screenshots

1. Map Function Intermidiate Output

<img src = "https://github.com/vedanthv/map-reduce-python/blob/master/intermidiate-map.PNG">

2. Reduce Function Intermidiate Output

<img src = "https://github.com/vedanthv/map-reduce-python/blob/master/reducer_out.PNG">

3. Final csv file with word count

<img src = "https://github.com/vedanthv/map-reduce-python/blob/master/final-output.jpg">

### Contributor

**Vedanth V Baliga**

**USN : ENG20DS0044**
