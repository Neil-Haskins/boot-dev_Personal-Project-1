# Personal Project 1 for boot.dev

Preferably something both interesting and useful:

Consider:

- Automating
- Something with data is good for backend

Should probably use Python and Tkinter, so as to match what's been done in the previous courses.

## Something to choose cities based on climate

**Description**

- Get climate data for a set of cities
- Allow user to input what sort of weather they want, e.g.
    - min/max/average high and/or low temps
    - min/max/average rainfall
    - wind speeds
    - whatever else
    - Choose a time of the year, or all year to consider data for
- Get a list of cities which fit the criteria, or a few that are closest.
- Bonus:
    - add weighting for most important characteristics

**Evaluation**

- Is interesting
- Not genuinely useful, but pseudo-useful
- Does use data
- Probably need to compile data manually (likely from Wikipedia)

### Plan

1. Set up parsing from a CSV, and print info to command line.
2. Set up GUI


### Examples:
- I want a list of all cities where the coldest it gets from June to August is 10 degrees.
- I want a list of all cities where the hottest it gets from June to August is 35 degrees.
- I want a list of all cities where between June and August the hottest it gets is AT LEAST 35 degrees.

- For a given city, I want the three months with the highest minimum temperature.

