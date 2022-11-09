def sort_teams(teams):
    size = len(teams)
    i = 0
    while i != size - 1:
        if teams[i][1]["points"] < teams[i + 1][1]["points"]:
            temp = teams[i]
            teams[i] = teams[i + 1]
            teams[i + 1] = temp
            i = 0
        elif teams[i][1]["points"] == teams[i + 1][1]["points"]:
            if teams[i][2]["gd"] < teams[i + 1][2]["gd"]:
                temp = teams[i]
                teams[i] = teams[i + 1]
                teams[i + 1] = temp
                i = 0
            else:
                i += 1
        else:
            i += 1
    return teams

if __name__ == "__main__":
    inp = input("Enter Input : ").split("/")
    teams = []
    for e in inp:
        team = e.split(",")
        result = []
        result.append(team[0])
        result.append({"points": int(team[1]) * 3 + int(team[3]) * 1})
        result.append({"gd": int(team[4]) - int(team[5])})
        teams.append(result)

    print("== results ==")
    teams = sort_teams(teams)
    for e in teams:
        print(e)
