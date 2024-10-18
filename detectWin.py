def detectWin(player):
    detectedHits = 0 # setze erkannte treffer zurück
    for fish in player.fishes:  # für die anzahl der fische
        detectedHits += fish.hits # füge erkannte treffer hinzu
    
    if detectedHits == 17: # wenn die anzahl der erkannten treffen größer als die gewinnsumme ist,
        return True # dann gebe True als gewonnen aus  
    else:
        return False # sonst gebe False als verloren aus