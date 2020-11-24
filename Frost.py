
from Biome import Biome


class Frost(Biome):
    def __init__(self, layout):
        self.water = [125, True, (125, 146, 177)]
        self.snow = [140, True, (250, 255, 255)]
        self.forest = [175, True, (52, 85, 69)]
        self.snow_hills = [255, True, (235, 241, 241)]

        # Default order
        self.colors = [self.water, self.snow, self.forest, self.snow_hills]

        # Right(Alphabet) order for iterations
        self.colors_iterator = [self.forest, self.snow, self.water]
        super().__init__(layout, self.colors, self.colors_iterator)
