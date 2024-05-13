from collections import defaultdict

emails_history_json = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})

# Sample data for email address "q1@qq.com"
emails_history_json["q1@qq.com"]["total_count"] = 3
emails_history_json["q1@qq.com"]["history"]["2022-01-21"] = 1
emails_history_json["q1@qq.com"]["history"]["2022-06-11"] = 2

# Sample data for other email addresses
emails_history_json["q2@qq.com"]["total_count"] = 5
emails_history_json["q2@qq.com"]["history"]["2022-02-15"] = 2
emails_history_json["q2@qq.com"]["history"]["2022-07-03"] = 3

emails_history_json["q3@qq.com"]["total_count"] = 7
emails_history_json["q3@qq.com"]["history"]["2022-03-10"] = 3
emails_history_json["q3@qq.com"]["history"]["2022-08-22"] = 4

emails_history_json["q4@qq.com"]["total_count"] = 2
emails_history_json["q4@qq.com"]["history"]["2022-04-05"] = 1
emails_history_json["q4@qq.com"]["history"]["2022-09-17"] = 1

emails_history_json["q5@qq.com"]["total_count"] = 4
emails_history_json["q5@qq.com"]["history"]["2022-05-20"] = 2
emails_history_json["q5@qq.com"]["history"]["2022-10-11"] = 2

# Print the initialized dictionary
print(emails_history_json)


import json

# Save the dictionary to a JSON file
with open("emails_history.json", "w") as file:
    json.dump(emails_history_json, file)


with open("emails_history.json", "r") as file:
    loaded_emails_history = json.load(file)

# Create a new defaultdict for email history
emails_history_json = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})

# Iterate over the loaded_emails_history dictionary and populate emails_history_json
for email, data in loaded_emails_history.items():
    emails_history_json[email]["total_count"] = data["total_count"]
    for date, count in data["history"].items():
        emails_history_json[email]["history"][date] = count