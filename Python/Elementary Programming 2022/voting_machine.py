tax_renewal = {
    "yay": 0,
    "nay": 0,
    "idk": 0,
    "error": 0
}
pooh_for_president = {
    "yay": 12,
    "nay": 0,
    "idk": 5,
    "error": 4
}


def vote(d):
    """add a vote"""
    print()
    print("Give your vote, the options are:")
    print("yay, nay, idk")
    vote = input("Your vote: ").lower()
    if vote == "yay":
        d["yay"] += 1
    elif vote == "nay":
        d["nay"] += 1
    elif vote == "idk":
        d["idk"] += 1
    else:
        d["error"] += 1
    print()


def show_results(d):
    max_length_key = 0
    for key in d:
        if len(key) > max_length_key:
            max_length_key = len(key)

    for key in d:
        spaces = " " * (max_length_key - len(key))
        progres_bar = "#" * d[key]
        print(f"{key.capitalize()}{spaces}: {progres_bar}")


for i in range(5):
    print("Should we implement the tax renewal?")
    vote(tax_renewal)
show_results(tax_renewal)
print()
print("*"*30)
print()


for i in range(5):
    print("Vote Winnie the Pooh for president?")
    vote(pooh_for_president)
show_results(pooh_for_president)
