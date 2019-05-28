# Exercise 3
from pathlib import Path
# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

from pathlib import Path
data_dir = Path("C:/Users/Jasmin/Desktop/Sommersemester 2019/Python/exercise-3-jasminkofler/data/cars.txt")
print(data_dir)
dir_exists = data_dir.exists()
print("Directory exists: {}".format(dir_exists))

# 2. Read the text file [2P]

with open(data_dir, "r") as file:
    lines = file.readlines()    
print(lines)

# 3. Count the occurences of each item in the text file [2P]

len(lines)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

dir_exists2 = output_dir.exists()
print("Directory exists: {}".format(dir_exists2))
output_dir.mkdir(parents = True, exist_ok = True)
print("Directory exists after creation: {}".format(output_dir.exists()))

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

