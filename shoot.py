def shoot(player, aimXY):
 
    if aimXY in player.shotList: # wenn dieser latz bereicht beschossen wurde
        return False # gebe False zurück

    for fish in player.fishes: # wiederhole für die Anzahl der Fische

        if aimXY in fish.occupied: # wenn an der stelle des schusses ein Fisch ist
            fish.hits += 1 # hitte den Fisch
            if fish.length == fish.hits: # wenn getroffener Fisch hit anzahl größer als Fishlänge, dann setze gebe "sunk" aus
                player.addShot(aimXY, "sunk") # führe einen Speichervorgang vom Schuss zu shotList aus
                return "sunk" # gebe "sunk zurück"

            else: # sonst gebe hit aus
                player.addShot(aimXY, "hit") # führe einen Speichervorgang vom Schuss zu shotList aus
                return "hit" # gebe "hit" zurück

    player.addShot(aimXY, "miss") # führe einen Speichervorgang vom Schuss zu shotList aus
    return "miss" # gebe "miss" zurück
        