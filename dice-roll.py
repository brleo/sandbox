import secrets

number_of_sides = 6
number_of_plays = 10000

roll_results = []
face_occurrences = []

print("[Rolling dices {} times...]".format(str(number_of_plays)))

for counter in range(0, number_of_plays):
    result = secrets.choice(range(1, number_of_sides + 1))
    roll_results.append(result)
    
    print("Play number {}".format(str(counter + 1)) + " = {}".format(str(result)))

print("[Generating statistics for each result...]")
    
for counter in range(1, number_of_sides + 1):
    face_occurrences.append(roll_results.count(counter))

for counter in range(1, number_of_sides + 1):
    percentual = (face_occurrences[counter - 1] / number_of_plays) * 100
    
    print("Total plays of side {}".format(str(counter))
        + ": ".format(str(face_occurrences[counter - 1]))
        + "{} ".format(face_occurrences[counter - 1])
        + "({}) ".format(str(round(percentual, 2))
        + "%"))