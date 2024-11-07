import random

# Klasse für den Schiffe-Versenken-Gegner
class Gegner:
    def __init__(self):
        self.grid_size = 10
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]  # 10x10 Spielfeld
        self.last_shot = None  # Letzter Schuss
        self.possible_targets = []  # Liste für mögliche nächste Ziele bei einem Treffer
    
    def get_next_shot(self, last_result):
        """
        Diese Funktion bestimmt den nächsten Schuss basierend auf dem letzten Ergebnis.
        Input:
        last_result: 0 = Daneben, 1 = Treffer, 2 = Versenkt
        Output:
        Nächste Schusskoordinaten als Liste [x, y]
        """
        # Falls der letzte Schuss ein Treffer war (1), füge angrenzende Felder zu möglichen Zielen hinzu
        if last_result == 1 and self.last_shot is not None:
            x, y = self.last_shot
            self.add_possible_targets(x, y)
        
        # Falls das Schiff versenkt wurde (2), leere die Liste der möglichen Ziele
        if last_result == 2:
            self.possible_targets.clear()

        # Bestimme den nächsten Schuss
        if self.possible_targets:
            next_shot = self.possible_targets.pop(0)  # Schieße auf das nächste mögliche Ziel
        else:
            next_shot = self.random_shot()  # Zufälliger Schuss, wenn kein Ziel vorhanden

        self.last_shot = next_shot
        return next_shot

    def add_possible_targets(self, x, y):
        """
        Fügt angrenzende Felder als mögliche Ziele hinzu (oben, unten, links, rechts)
        """
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Oben, unten, links, rechts
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size and self.grid[new_x][new_y] == 0:
                self.possible_targets.append([new_x, new_y])

    def random_shot(self):
        """
        Gibt eine zufällige Koordinate für den nächsten Schuss zurück, die noch nicht getroffen wurde.
        """
        tries = 0
        while True:
            tries += 1
            if tries > 100:
                return [0, 0]
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if self.grid[x][y] == 0:  # Schieße nur auf ungetroffene Felder
                self.grid[x][y] = 1  # Markiere das Feld als getroffen
                return [x, y]
    
    def reset(self):
        """
        Setzt alle gespeicherten Daten zurück, um für eine neue Runde vorbereitet zu sein.
        """
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]  # Setze das Spielfeld zurück
        self.last_shot = None  # Setze den letzten Schuss zurück
        self.possible_targets.clear()  # Leere die Liste der möglichen Ziele


# Erstelle eine Gegnerinstanz
gegner = Gegner()

# Funktion, die den Gegner aufruft und den nächsten Schuss bestimmt
def shootAI(response):
    """
    Ruft die Gegner-Logik auf und gibt die nächste Schusskoordinate basierend auf der letzten Antwort zurück.
    :param response: 0 = Daneben, 1 = Treffer, 2 = Versenkt
    :return: Nächste Schusskoordinate als [x, y]
    """
    return tuple(gegner.get_next_shot(response))

# Funktion, um den Gegner für eine neue Runde zurückzusetzen
def resetAI():
    """
    Setzt den Gegner zurück, um eine neue Runde zu beginnen.
    """
    gegner.reset()

