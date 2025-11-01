import re
def classify_with_regex(log_message):
    regex_patterns={
        r"User User\d* logged (in|out).":"User Action",
        r"Backup (started|ended) at .*":"System Notification",
        r"Backup completed successfully.":"System Notification",
        r"System updated to version .*":"System Notification",
        r"File data_.*":"System Notification",
        r"Disk cleanup completed successfully.":"System Notification",
        r"System reboot initiated by user User\d*\.":"System Notification",
        r"nova\.(osapi|metadata).*":"HTTP Status",
        r"nova\.compute.*":"Resource Usage",
        r"Account with ID \d* created by User\d*.":"User Action",
        r"Account with ID \d* created by User\d*.":"User Action",
        r"\breplication\b":"Error"
    }
    for pattern, label in regex_patterns.items():
        if re.findall(pattern,log_message,re.IGNORECASE):
            return label
    return None

if __name__ =="__main__":
    print(classify_with_regex("nova.osapi_compute.wsgi.server [req-ee8bc8ba-9265-4280-9215"))
    print(classify_with_regex("Account with ID 5351 created by User634."))
    print(classify_with_regex("File data_3847.csv uploaded successfully by user User175."))
    print(classify_with_regex("nova.compute.wsgi.server [req-ee8bc8ba-9265-4280-9215"))
    print(classify_with_regex("Hey How are you"))

# msg="User User345 logged in."

# match=re.search("User User\d* logged (in|out).",msg,re.IGNORECASE)


# print(match)