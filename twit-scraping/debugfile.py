from csv_process import read_to_variable, write_to_csv

"""
debug doc
"""
NAME = "elonmusk"
YEAR = 2019
DATE = "03-14-2023"
RANGE = 3
FILENAME = f"{NAME}_within_{RANGE}_days_of-{DATE}"
tweets = read_to_variable(NAME, YEAR)

nums = []

for tweet in tweets[1:]:
    nums.append([int(float(tweet[2])), 1, 1])

write_to_csv(nums, "test")
