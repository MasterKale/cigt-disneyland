import calendar
import math
from collections import namedtuple

from PIL import Image

calendar.setfirstweekday(calendar.SUNDAY)

def rgb2hex(color: tuple) -> str:
    """Converts a list or tuple of color to an RGB string

    Args:
        color (list|tuple): the list or tuple of integers (e.g. (127, 127, 127))

    Returns:
        str:  the rgb string
    """
    return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in color)}"

StartPoint = namedtuple('StartPoint', 'x y')
Margins = namedtuple('Margins', 'top right bottom left')
# Calendar = namedtuple('Calendar', '')
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
      self.border_outer +
      # Multiply by number of days in a week
      (self.cell_width * 7) +
      # Multiply by number of borders between days in a week
      (self.border_inner * 6) +
      self.border_outer +
      self.margins.right
    )

  @property
  def height(self):
    """
    Calculate the height of a calendar by mimicking the pixel dimensions of the rows in a calendar
    """
    return (
      self.border_outer +
      (self.cell_height * self.num_weeks) +
      (self.border_inner * (self.num_weeks - 1)) +
      self.border_outer +
      self.margins.bottom
    )

  @property
  def week_height(self):
    return self.cell_height + self.border_inner

"""
Cells: 40x40px
Inner Border: 1px
Outer Border: 2px
Height between calendars (excluding outer borders): 84px
Date: 10x10px (max)
"""
cal = Calendar(
  cell_height=40,
  cell_width=40,
  margins=Margins(top=0, right=17, bottom=84, left=0),
  border_inner=1,
  border_outer=2,
)

with open('./DLR-DL-Select-Desktop-13.png', 'rb') as fp:
  img = Image.open(fp)
  px = img.load()

"""
START SETTINGS
"""
# Settings to manually adjust/pass in as args
# num_months = 13
num_months = 3
start_year = 2018
start_month = 6
num_columns = 3
"""
END SETTINGS
"""

year = start_year
month = start_month
num_rows = math.ceil(num_months / num_columns)
start = StartPoint(x=3, y=146)

row = 0
for count in range(num_months):
  print(f'count: {count}')
  # A simple way to keep track of which column we're in
  col = count % num_columns
  print(f'col: {col}')
  print(f'row: {row}')
  # Calculate the current month
  curr_month = month + count
  if curr_month > 12:
    curr_month -= 12
  if curr_month == 1:
    year += 1
  # Get an array of week arrays for the current month
  curr_month_cal = calendar.monthcalendar(year, curr_month)
  cal.num_weeks = len(curr_month_cal)
  # Shift over a distance equal to the number of calendars to the left of the current column
  start_x = start.x + (cal.width * col)
  start_y = start.y + (cal.height * row)
  x = start_x
  y = start_y
  print(f'at {x},{y}')
  # Iterate through each week
  for week in curr_month_cal:
    for day in week:
      if day > 0:
        (r,g,b,a) = px[x,y]
        print(f'{year}-{curr_month}-{day}: {rgb2hex((r,g,b)) == "#B7D291"}')
      # Move over
      x += cal.cell_width + cal.border_inner
    # Move back to the first column
    x = start_x
    # Move down a row
    y += cal.week_height
  """
  TODO: Figure out how to move down to the next calendar in col 0
  """
  print(f'at {x},{y}')
