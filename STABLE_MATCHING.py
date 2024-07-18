def stable_matching(men,women):
    engaged = {}
    free_mans = list(men.keys())

    while free_mans:
        man = free_mans.pop(0)
        pref_man = men[man]
        for woman in pref_man:
            if woman not in engaged:
                engaged[woman] = man
                break

            else:
                current_match = engaged[woman]
                pref_woman = women[woman]
                if pref_woman.index(man) < pref_woman.index(current_match):
                    engaged[woman] = man
                    free_mans.append(current_match)
                    break
                else:
                    continue
    return engaged

def main():
    men = {}
    no_mens = int(input("Enter no of mens : "))
    for _ in range(no_mens):
        man = input("Enter name of the man : ")
        man_pref = input(f"Enter pref of man {man} (ss) : ").split()
        men[man] = man_pref

    women = {}
    no_women = int(input("Enter no of womens : "))
    for _ in range(no_women):
        woman = input("Enter name of the woman : ")
        woman_pref = input(f"Enter pref of the woman {woman} (ss) : ").split()
        women[woman] = woman_pref

    matches = stable_matching(men,women)

    for woman,man in matches.items():
        print(f"{man} - > {woman}")

if __name__ == "__main__":
    main()