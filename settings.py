width = 1600
height = 900

ai_mode = False

ai_processing_time = 30 * 1.5 # 1.5 Seconds
if ai_mode:
    ai_processing_time = 2 # 2 Frames

fish_lengths0 = [2, 3, 3, 4, 5] #Standart Array
fish_lengths1 = [3, 4, 4, 3, 5] #Fast Round
fish_lengths2 = [2, 2, 3, 3, 3, 4, 4] #slow Round
fish_lengths3 = [2, 2] #only 2er
fish_lengths4 = [3, 3, 3] #only 3er
fish_lengths5 = [4, 4, 4, 4] #only 4er
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