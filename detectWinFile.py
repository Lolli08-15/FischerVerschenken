def detectWin(player):
    detectedHits = 0 # setze erkannte treffer zurück
    occupied = 0
    for fish in player.fishes:  # für die anzahl der fische
        detectedHits += fish.hits # füge erkannte treffer hinzu
        occupied += len(fish.occupied)
    
    if detectedHits >= occupied: # wenn die anzahl der erkannten treffen größer als die anzahl aller verbrauchten plätze ist ist,
        return True # dann gebe True als gewonnen aus  
    else:
        return False # sonst gebe False als verloren aus
