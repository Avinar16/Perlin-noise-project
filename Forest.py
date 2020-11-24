
from Biome import Biome


class Forest(Biome):
    def __init__(self, layout):
        self.water = [110, True, (65, 105, 225, 255)]
        self.sand = [113, True, (238, 214, 175, 255)]
        self.forest = [130, True, (34, 139, 34, 255)]
        self.deep_forest = [150, True, (34, 120, 34, 255)]
        self.mountains = [180, True, (121, 121, 121, 255)]
        self.high_mountains = [300, self.mountains[1], (210, 210, 210, 255)]

        # Default order
        self.colors = [self.water, self.sand, self.forest, self.deep_forest,
                       self.mountains, self.high_mountains]

        # Right(Alphabet) order for iterations
        self.colors_iterator = [self.deep_forest, self.forest, self.mountains, self.sand, self.water]
        super().__init__(layout, self.colors, self.colors_iterator)