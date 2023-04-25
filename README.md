## Data Analytics with Hadoop Programming Assignment

**Problem Statement**
Count the number of times a word appears in the document. Develop a MapReduce framework based on Python threads. The data will be read from a file, stored in-memory and will run on a single computer.

**Why Shuffle?**
For example the results from a map need to be shuffled before being sent to reduce processes: if the two instances of the word ‘Apple’ were sent to distinct reduce processes, the count would not be correct.

**Task Checklist and Requirements**

- [ ] Implement the Map Function
- [ ] Implement the Reduce Function
- [ ] Implement the Shuffle Function
- [ ] Document the code
- [ ] Add requirements.txt file

