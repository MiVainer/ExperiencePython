Numbers = {}
Numbers["Миша"] = "8-923-733-32-87"
Numbers["Семён"] = "8-919-232-31-22"
Numbers["Катя"] = "8-922-132-31-11"
Numbers["Маша"] = "8-999-111-22-33"
for value in sorted(Numbers.values()):
    for key in Numbers.keys():
        if Numbers[key] == value:
            print(key, Numbers[key])