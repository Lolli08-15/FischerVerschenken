width = 1600
height = 900

ai_processing_time = 30 * 1.5 # 1.5 Seconds

fish_lengths0 = [1, 2, 3, 3, 4, 5, 6] #Standart Array
fish_lengths1 = [3, 3, 4, 4, 4, 4, 5, 5, 5, 5] #Fast Round
fish_lengths2 = [1, 1, 2, 2, 3, 3] #slow Round
fish_lengths3 = [1, 6, 7] #only 2er
fish_lengths4 = [3, 3, 3] #only 3er
fish_lengths5 = [4, 4, 6, 6] #only 4er
fish_lengths6 = [5, 5, 5, 5, 5] #only 5er


def get_fish_preset(preset):
    if preset == 0:
        return fish_lengths0.copy()
    if preset == 1:
        return fish_lengths1.copy()
    if preset == 2:
        return fish_lengths2.copy()
    if preset == 3:
        return fish_lengths3.copy()
    if preset == 4:
        return fish_lengths4.copy()
    if preset == 5:
        return fish_lengths5.copy()
    else:
        return fish_lengths6.copy()

def get_ai_name(ai):
    name = "Spieler"
    if ai == 0: name = "Dummheit Persönlich"
    if ai == 1: name = "Chad GPT"
    if ai == 2: name = "Medium"
    if ai == 3: name = "High AIQ"
    if ai == 4: name = "Hart wie Hartmut"
    if ai == 5: name = "Unmöglich"
    if ai == 6: name = "Mr. Chunky"
    return name