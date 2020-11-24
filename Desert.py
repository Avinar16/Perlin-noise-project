from Biome import Biome


class Desert(Biome):
    def __init__(self, layout):
        self.low_sand = [125, True, (255,253,208)]
        self.sand = [150, True, (255,223,132)]
        self.sand_hills = [190, True, (253, 234, 168)]
        self.s_sand = [255, True, (255, 226, 150)]

        # Default order
        self.colors = [self.low_sand, self.sand, self.sand_hills, self.s_sand]

        # Right(Alphabet) order for iterations
        self.colors_iterator = [self.low_sand, self.sand, self.sand_hills]
        super().__init__(layout, self.colors, self.colors_iterator)
