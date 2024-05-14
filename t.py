from collections import defaultdict

emails_history_json = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})

emails_history_json2 = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})

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




# Save the dictionary to a JSON file
with open("emails_history.json", "w") as file:
    json.dump(emails_history_json, file)



import json

with open("emails_history.json", "r") as file:
    loaded_emails_history = json.load(file)

# Create a new defaultdict for email history
emails_history_json = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})

# Iterate over the loaded_emails_history dictionary and populate emails_history_json
for email, data in loaded_emails_history.items():
    emails_history_json[email]["total_count"] = data["total_count"]
    for date, count in data["history"].items():
        emails_history_json[email]["history"][date] = count

emails_test_lt = ["q1@qq.com", "q2@qq.com", "q_1@qq.com", "q_2@qq.com"]

def email_filter(email_list, emails_history_json):
    filtered_emails = []
    for email in email_list:
        if emails_history_json[email]['total_count'] < 1:
            filtered_emails.append(email)
    return filtered_emails

email_filter(emails_test_lt, emails_history_json)


def email_history_log(email, emails_history_json, today=None):
    from datetime import datetime
    if today is None:
        today = datetime.now().strftime("%Y-%m-%d")
    emails_history_json[email]["total_count"] += 1
    emails_history_json[email]["history"][today] += 1
    print(f"Info logged: {emails_history_json[email]}")


def get_email_history(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return history_dict
    else: 
        return None

def set_email_history(path):
    """Set email_history for the 1st time."""
    contents = json.dumps(defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)}))
    path.write_text(contents)
    print("Email history set.")


# Save the dictionary to a JSON file
with open("emails_history.json", "w") as file:
    json.dump(emails_history_json, file)

