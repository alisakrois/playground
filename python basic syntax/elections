
"""
Statement
As you know, the president of USA is elected not by direct vote, but through a two-step voting.
First elections are held in each state and determine the winner of elections in that state.
Thereafter, the state election is going: in this election,
every state has a certain the number of votes — the number of electors from that state. In practice,
all the electors from the state of voted in accordance with the results of the vote within a state.
The first line contains the number of records.After that, each entry contains the name of the candidate
and the number of votes they got in one of the states. Count the total results of the elections:
sum the number of votes for each candidate. Print candidates in the alphabetical order.
"""


d = {}
for i in range(int(input())):
    surname, vote = input().split()
    d[surname] = d.get(surname, 0) + int(vote)

for surname in sorted(d):
    print(surname, d[surname])