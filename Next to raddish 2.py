from collections import Counter

# Create Counter objects to store the counts
radish_names = Counter()
customer_name = Counter()

# Read the data from the file
with open("C:/Users/Ritika/Desktop/My data/Python/radishsurvey.txt", "r") as file:
    lines = file.readlines()

# Iterate through the lines and count the votes
for line in lines:
    name, radish_type = line.strip().split(" - ")
    name = name.replace(" ", "").upper()
    radish_type = radish_type.replace(" ", "").upper()

    radish_names[radish_type] += 1
    customer_name[name]+=1

most_popular_radish = radish_names.most_common(1)
print("The most popular radish type is", most_popular_radish)

least_popular_radish = radish_names.most_common()[-1]
print("The least popular radish type is", least_popular_radish)

repeated_names = customer_name.most_common(2)
print("The most repeated names are", repeated_names)