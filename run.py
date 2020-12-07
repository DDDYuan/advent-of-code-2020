from tasks import day1
from tasks import day2
from tasks import day3
from tasks import day4
from tasks import day5
from tasks import day6
from tasks import day7

tasks = [day1, day2, day3, day4, day5, day6, day7]


for day in range(len(tasks)):
    print(f'Result of day{day + 1} is')
    print(f'Part 1:')
    tasks[day].part_one()
    print(f'Part 2:')
    tasks[day].part_two()
    print()
