import calendar
import math

from PIL import Image

from classes import Calendar, StartPoint, Margins

# Make Python's calendar module start weeks on Sunday
calendar.setfirstweekday(calendar.SUNDAY)

def rgb2hex(color: tuple) -> str:
    """
    Converts a list or tuple of color to an RGB string

    Args:
        color (list|tuple): the list or tuple of integers (e.g. (127, 127, 127))

    Returns:
        str:  the rgb string
    """
    return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in color)}"


def zero_pad_number(num: int) -> str:
    """
    Prepend a zero to numbers less than 10
    """
    return str(num).zfill(2)


def parse_calendar(filename: str, start_year: int, start_month: int, num_months: int, num_columns: int) -> dict:
    """
    Parse a calendar image to determine what days are open

    return:
        { "YYYY-MM-DD": bool }
    """
    to_return = {}

    # Record the structure of a calendar to help navigate it
    cal = Calendar(
        cell_height=40,
        cell_width=40,
        margins=Margins(top=0, right=17, bottom=84, left=0),
        border_inner=1,
        border_outer=2,
    )

    with open(filename, "rb") as fp:
        img = Image.open(fp)
        px = img.load()

    year = start_year
    month = start_month
    start = StartPoint(x=6, y=146)

    row = 0
    for count in range(num_months):
        # A simple way to keep track of which column we're in
        col = count % num_columns
        # Move down rows as we progress through the calendars
        if count > 0 and count % num_columns == 0:
            row += 1
        # Calculate the current month
        curr_month = month + count
        if curr_month > 12:
            curr_month -= 12
        # Advance a year if we're in January
        if curr_month == calendar.January:
            year += 1
        # Get an array of week arrays for the current month
        curr_month_cal = calendar.monthcalendar(year, curr_month)
        cal.num_weeks = len(curr_month_cal)
        # Shift over a distance equal to the number of calendars to the left of the current column
        start_x = start.x + (cal.width * col)
        start_y = start.y + (cal.height * row)
        x = start_x
        y = start_y
        # Iterate through each week
        for week in curr_month_cal:
            for day in week:
                if day > 0:
                    # Zero-pad numbers less than 10
                    _month = zero_pad_number(curr_month)
                    _day = zero_pad_number(day)
                    key = f"{year}-{_month}-{_day}"
                    (r, g, b, a) = px[x, y]
                    is_available = rgb2hex((r, g, b)) == "#B7D291"
                    to_return[key] = is_available
                    # DEBUG - See where we've been
                    # px[x, y] = (0, 0, 0)
                # Move over
                x += cal.cell_width + cal.border_inner
            # Move back to the first column
            x = start_x
            # Move down a row
            y += cal.week_height
    # DEBUG - Save a disposable copy of the image with modified pixel data
    # img.save("./blah.png")
    return to_return
