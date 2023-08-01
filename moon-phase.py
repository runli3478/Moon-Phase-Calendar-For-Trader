import datetime
import ephem
import calendar

def get_phase_on_day(year: int, month: int, day: int):
    date = ephem.Date(datetime.date(year, month, day))
    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)
    lunation = (date - pnm) / (nnm - pnm)
    return lunation

def get_moons_in_year(year: int):
    moons = []
    date = ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year == year:
        date = ephem.next_full_moon(date)
        moons.append((date, '🌕 Full Moon'))

    date = ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year == year:
        date = ephem.next_new_moon(date)
        moons.append((date, '🌑 New Moon'))

    moons.sort(key=lambda x: x[0])
    return moons

def print_moon_calendar(year: int):
    moon_phases = {
        'new': '🌑',
        'waxing_crescent': '🌒',
        'first_quarter': '🌓',
        'waxing_gibbous': '🌔',
        'full': '🌕',
        'waning_gibbous': '🌖',
        'last_quarter': '🌗',
        'waning_crescent': '🌘'
    }

    print(f"========= Crypto Moon Calendar - {year} =========")
    cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    for month in range(1, 13):
        month_days = cal.monthdayscalendar(year, month)
        print(f"\n=== {calendar.month_name[month]} ===")
        print("  Sun  Mon  Tue  Wed  Thu  Fri  Sat")
        for week in month_days:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "     "
                else:
                    phase = get_phase_on_day(year, month, day)
                    if phase < 0.125:
                        week_str += moon_phases['new'] + " "
                    elif phase < 0.25:
                        week_str += moon_phases['waxing_crescent'] + " "
                    elif phase < 0.375:
                        week_str += moon_phases['first_quarter'] + " "
                    elif phase < 0.625:
                        week_str += moon_phases['waxing_gibbous'] + " "
                    elif phase < 0.75:
                        week_str += moon_phases['full'] + " "
                    elif phase < 0.875:
                        week_str += moon_phases['waning_gibbous'] + " "
                    elif phase < 1.0:
                        week_str += moon_phases['last_quarter'] + " "
                    else:
                        week_str += moon_phases['waning_crescent'] + " "
                    week_str += f"{day:2d}".ljust(2)
            print(week_str)

if __name__ == "__main__":
    year_to_display = 2023 # You may change the value of year_to_display to show other year!
    print_moon_calendar(year_to_display) 
