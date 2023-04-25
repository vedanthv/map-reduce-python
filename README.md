## Data Analytics with Hadoop Programming Assignment

**Problem Statement**

Count the number of times a word appears in the document. Develop a MapReduce framework based on Python threads. The data will be read from a file, stored in-memory and will run on a single computer.

<img src = "https://vipanchikatthula.github.io/post/mapper-reducer-implementation/featured.jpg">

**Why Shuffle?**

For example the results from a map need to be shuffled before being sent to reduce processes: if the two instances of the word ‘Apple’ were sent to distinct reduce processes, the count would not be correct.

**Task Checklist and Requirements**

- [x] Import text file
- [x] Data Cleaning
- [x] Split Data in Parts   
- [ ] Implement the Map Function
- [ ] Implement the Shuffle Function
- [ ] Implement the Reduce Function
- [ ] Document the project
- [ ] Add requirements.txt file

**How to Run?**

**Output Screenshots**

**Contributors**

Vedanth V Baliga
USN : ENG20DS0044