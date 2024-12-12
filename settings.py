width = 1600
height = 900

ai_processing_time = 30 * 0.5 # 1.5 Seconds

hitmarker_time = 8 # in frames

fish_lengths0 = [2, 3, 3, 4, 5] #Normen !!! Bleibt
#Hindernisse: 0
fish_lengths1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7] #Volles Rohr
#Hindernisse: 0-5
fish_lengths2 = [1, 1, 6, 6, 7, 7] #Not Straight
#Hindernisse: 3-8
fish_lengths3 = [1, 1, 2, 2] #Double Trouble
#Hindernisse: 8-18
fish_lengths4 = [1, 2, 3, 4, 5, 6, 7] #Einzigartig
#Hindernisse: 4-10
fish_lengths5 = [7, 7, 7, 7, 7] #Krumme Sache
#Hindernisse: 7
fish_lengths6 = [3, 4, 4, 5, 5, 7] #Bananas Choice
#Hindernisse: 2-12

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
    if ai == 7: name = "Dirty Dan"
    return name