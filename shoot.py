def shoot(attacker, victim, aimXY):

    for shot in attacker.shotList:
        if aimXY == shot[0]:
            return False

    for fish in victim.fishes: # wiederhole für die Anzahl der Fische

        if aimXY in fish.occupied: # wenn an der stelle des schusses ein Fisch ist
            fish.hits += 1 # hitte den Fisch
            if len(fish.occupied) == fish.hits: # wenn getroffener Fisch hit anzahl größer als Fishlänge, dann setze gebe "sunk" aus
                attacker.addShot(aimXY, "sunk") # führe einen Speichervorgang vom Schuss zu shotList aus
                attacker.sunkenFish += 1
                return "sunk" # gebe "sunk zurück"

            else: # sonst gebe hit aus
                attacker.addShot(aimXY, "hit") # führe einen Speichervorgang vom Schuss zu shotList aus
                return "hit" # gebe "hit" zurück

    attacker.addShot(aimXY, "miss") # führe einen Speichervorgang vom Schuss zu shotList aus
    return "miss" # gebe "miss" zurück
        