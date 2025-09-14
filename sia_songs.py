import random

def suggest_sia_song():
    songs = [
        "Chandelier",
        "Elastic Heart",
        "Cheap Thrills",
        "Alive",
        "Unstoppable",
        "Never Give Up",
        "The Greatest",
        "Big Girls Cry",
        "Together",
        "Move Your Body",
        "Snowman",
        "Courage to Change"
    ]

    return random.choice(songs)

if __name__ == "__main__":
    print("🎶 You should play next:", suggest_sia_song())
