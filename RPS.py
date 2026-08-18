# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order=[{}]):
    # Reset state at the start of each new match
    if prev_play == "":
        opponent_history.clear()
        play_order[0] = {}
    else:
        opponent_history.append(prev_play)

    n = 5  # length of the pattern we memorize
    guess = "R"

    if len(opponent_history) >= n:
        # Save the last n-move sequence and count how often it appeared
        key = "".join(opponent_history[-n:])
        play_order[0][key] = play_order[0].get(key, 0) + 1

        # Look at the last n-1 moves, check which move usually follows
        recent = "".join(opponent_history[-(n - 1):])
        candidates = [recent + m for m in ["R", "P", "S"]]
        counts = {c: play_order[0].get(c, 0) for c in candidates}

        if max(counts.values()) > 0:
            guess = max(counts, key=counts.get)[-1]

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]
