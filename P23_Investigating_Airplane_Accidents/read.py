file = open("AviationData.txt", "r")

read_file = file.read()

aviation_data = read_file.split("\n")

# print(aviation_data[0:2])

aviation_list = []

for line in aviation_data:
    text = line.split("|")
    word_list = []
    for word in text:
        word_list.append(word.strip())
    aviation_list.append(word_list)
    
# print(aviation_list[:2])
    
lax_code = []

# Search for the value of LAX94LA336 through iterations of rows by columns
for i in range(len(aviation_list)):
    for j in range(len(aviation_list[i])):
        if aviation_list[i][j] == 'LAX94LA336':
            lax_code.append(aviation_list[i])
            
print(lax_code)

# Downside is the time complexity of O(n^2)

# Write a function for linear search
def linear_search(a_str):
    '''
    a_str is a string
    '''
    lax_code = []
    for line in aviation_list:
        for word in line:
            if word == a_str:
                lax_code.append(line)
    return lax_code

l_search = linear_search("LAX94LA336")
print(l_search)

# Write a function for search with complexity of O(n)
def search_by_line(a_str):
    lax_code = []
    for line in aviation_list:
        if a_str in line:
            lax_code.append(line)
    return lax_code

o_n_search = search_by_line("LAX94LA336")
print(o_n_search)

# Split the words in each line by '|' and add them into dic with keys

# Extract the keys from the first line
keywords = aviation_data[0].split("|")
keys = []
for keyword in keywords:
    keys.append(keyword.strip())

# Extract the values
cleaned_lines = []
for i in range(1, len(aviation_data)):
    line = aviation_data[i]
    words = line.split("|")
    words_list = []
    for word in words:
        words_list.append(word.strip())
    cleaned_lines.append(words_list)

for line in cleaned_lines:
    if len(line) != 32:
        print(line)
        print(cleaned_lines.index(line))

cleaned_lines.pop(77281)

aviation_dict_list = []

# Add in the values with corresponding keys
for line in cleaned_lines:
    dict_line = {}
    for i in range(len(keys)):
        dict_line[keys[i]] = line[i]
    aviation_dict_list.append(dict_line)
    
# Test
print(aviation_dict_list[0])

# Search through dict
lax_dict = []
for line in aviation_dict_list:
    if line["Accident Number"] == "LAX94LA336":
        lax_dict.append(line)
        
print(lax_dict)

# Find the numbers of accidents in each state in US

accidents_record_by_state = []

for line in aviation_dict_list:
    accidents_record_by_state.append(line["Location"][-2:])
    
from collections import Counter
accidents_by_state = Counter(accidents_record_by_state)

print(accidents_by_state.most_common(10))

# Count the total number of fatalities and injuries in different months
total_injuries_by_month = {}
for line in aviation_dict_list:
    month = line["Event Date"][:2]
    total_injuries = 0
    # Check the blank cells
    try:
        fatalities  = int(line["Total Fatal Injuries"])
    except:
        fatalities = 0
    try:
        injuries = int(line["Total Serious Injuries"])
    except:
        injuries = 0
    total_injuries = fatalities + injuries
    if month in total_injuries_by_month:
        total_injuries_by_month[month] += total_injuries
    else:
        total_injuries_by_month[month] = total_injuries
        
print(total_injuries_by_month)