def split_into_groups(males, females):
    match_scores = {}

    for male in males.keys():
        for female in females.keys():
            if (male, female) not in match_scores.keys():
                male_index = int(male[1]) - 1
                female_index = int(female[1]) - 1
                match_scores[(male,female)] = (males[male][female_index] + females[female][male_index])
                
    sorted_match_scores = list(sorted(match_scores.items(), key=lambda x: x[1], reverse = True))

    group = []

    for (male, female), match_score in sorted_match_scores:
        if male not in group and female not in group:
            group.extend([male, female])
    output = []
    for i in range(len(group) - 1):
        output.append((group[i], group[i+1]))

    return output[0:len(output) + 1: 2]

# males = {
#     'M1': [2,5,3,4,6,1],
#     'M2': [1,3,2,6,5,4],
#     'M3': [4,5,2,1,3,6],
#     'M4': [6,4,1,2,3,5],
#     'M5': [5,3,4,1,6,2],
#     'M6': [2,6,3,4,1,5],
# }

# females = {
#     'F1': [1,5,4,2,3,6],
#     'F2': [3,2,5,1,4,6],
#     'F3': [6,4,5,3,1,2],
#     'F4': [1,2,3,4,5,6],
#     'F5': [5,2,6,4,3,1],
#     'F6': [4,3,1,2,6,5],
# }

# split_into_groups(males, females)