

## 1: (Task 2.12.2) Policy Compare
def policy_compare(sen_a: str, sen_b: str, voting_dict: dict) -> int:

    return sum([voting_dict[sen_a][x] * voting_dict[sen_b][x] for x in range(len(voting_dict[sen_a]))])
    


## 2: (Task 2.12.3) Most Similar
def most_similar(sen: str, voting_dict: dict) -> str:

    similarity = policy_compare(sen, sen, voting_dict) * -1

    for name in voting_dict:
        if policy_compare(sen, name, voting_dict) >= similarity and name != sen:
            similarity = policy_compare(sen, name, voting_dict)
            similar = name

    return similar





## 3: (Task 2.12.4) Least Similar
def least_similar(sen: str, voting_dict: dict) -> str:

    similarity = policy_compare(sen, sen, voting_dict)

    for name in voting_dict:
        if policy_compare(sen, name, voting_dict) <= similarity and name != sen:
            similarity = policy_compare(sen, name, voting_dict)
            similar = name

    return similar


## 4: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen: str, sen_set: set, voting_dict: dict) -> float:
    
    total = [policy_compare(sen, name, voting_dict) for name in sen_set]

    return sum( total ) / len( total )


## 5: (Task 2.12.8) Average Record
def find_average_record(sen_set: set, voting_dict: dict) -> list[float]:

    average = [0]*max([len(x) for x in voting_dict.values()])

    for name in sen_set:
        for component in range(len(voting_dict[name])):
            average[component] += voting_dict[name][component]

    for component in range(len(average)):
        average[component] /= len(sen_set)

    return average


## 6: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict: dict) -> tuple:
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    lowest = policy_compare(list(voting_dict.keys())[0], list(voting_dict.keys())[1], voting_dict)
    rivals = (list(voting_dict.keys())[0], list(voting_dict.keys())[1])
    for name_1 in voting_dict.keys():
        for name_2 in voting_dict.keys():
            if name_1 != name_2:
                similarity = policy_compare(name_1, name_2, voting_dict)
                if similarity <= lowest:
                    lowest = similarity
                    rivals = (name_1, name_2)

    return rivals


# print(policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]}))
# 253

# vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
# print(most_similar('c', vd))
# D

# vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
# print(least_similar('a', vd))
# C

# vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
# sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
# print(find_average_similarity('Klein', sens, vd))
# # -0.5
# print(sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'})
# # True
# print(vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]})
# # True

# voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
# senators = {'Fox-Epstein','Ravella'}
# find_average_record(senators, voting_dict)
# # [-0.5, -0.5, 0.0]

# voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
# br = bitter_rivals(voting_dict)
# print(br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein'))
# #True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
