def load_high_score(filepath="highscore.txt"):
    try:
        with open(filepath, "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(score, filepath="highscore.txt"):
    high_score = load_high_score(filepath)
    if score > high_score:
        with open(filepath, "w") as file:
            file.write(str(score))
