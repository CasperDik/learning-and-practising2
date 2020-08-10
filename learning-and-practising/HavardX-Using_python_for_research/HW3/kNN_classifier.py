import numpy as np
import random
import scipy.stats as ss

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)

    return random.choice(winners)

def majority_vote_scipy(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,2,3,1,2,3,3,3,3,1,2]
winner = majority_vote_scipy(votes)
print(winner)
