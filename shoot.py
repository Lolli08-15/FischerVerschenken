def shoot(player, aimX, aimY):

    aimXY = aimX*10+aimY #füge X udn Y in eine Var zusammen

    for fish in player.fishes:

        if aimXY in fish.occupied: # wenn an der stelle des schusses ein Fisch ist
            fish.hits += 1 # hitte den Fisch
            
            if fish.length == fish.hits: # wenn getroffener Fisch hit anzahl größer als Fishlänge, dann setze gebe "sunk" aus
                return "sunk" # gebe "sunk zurück"

            else: # sonst gebe hit aus
                return "hit" # gebe "hit" zurück

    return "miss" # gebe "miss" zurück
        