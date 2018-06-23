from collections import namedtuple

StartPoint = namedtuple("StartPoint", "x y")
Margins = namedtuple("Margins", "top right bottom left")

class Calendar:
    def __init__(self, cell_height, cell_width, margins, border_inner, border_outer):
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.margins = margins
        self.border_inner = border_inner
        self.border_outer = border_outer
        self.num_weeks = 0

    @property
    def width(self):
        """
        Calculate the width of a calendar by mimicking the pixel dimensions of a row in a calendar
        """
        return (
            self.border_outer
            +
            # Multiply by number of days in a week
            (self.cell_width * 7)
            +
            # Multiply by number of borders between days in a week
            (self.border_inner * 6)
            + self.border_outer
            + self.margins.right
        )

    @property
    def height(self):
        """
        Calculate the height of a calendar by mimicking the pixel dimensions of the rows in a calendar
        """
        return (
            self.border_outer
            # All calendars display six rows, even if they contain a fewer number of weeks
            + (self.cell_height * 6)
            + (self.border_inner * (self.num_weeks - 1))
            + self.border_outer
            + self.margins.bottom
        )

    @property
    def week_height(self):
        return self.cell_height + self.border_inner
