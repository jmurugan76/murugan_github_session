# ✅ All imports at the top
from datetime import datetime, date, timedelta

# ==============================
# FILE HANDLING SECTION
# ==============================

# Step 1: Create and Write to a File
with open("sample.txt", "w") as file:
    file.write("Hello Murugan!\n")
    file.write("Welcome to Python kasyab File Handling.\n")

print("File created and data written successfully.\n")

# Step 2: Append Data to the File
with open("sample.txt", "a") as file:
    file.write("This line is appended later.\n")

print("Data appended successfully.\n")

# Step 3: Read the File
with open("sample.txt", "r") as file:
    content = file.read()

print("Reading file content:\n")
print(content)


# ==============================
# DATE OPERATIONS SECTION
# ==============================

# 1️⃣ Get Current Date and Time
current_datetime = datetime.now()
print("Current Date & Time:", current_datetime)

# 2️⃣ Get Only Current Date
today = date.today()
print("Today's Date:", today)

# 3️⃣ Format Date
formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date:", formatted_date)

# 4️⃣ Add 10 Days
future_date = today + timedelta(days=10)
print("Date after 10 days:", future_date)

# 5️⃣ Subtract 5 Days
past_date = today - timedelta(days=5)
print("Date before 5 days:", past_date)

# 6️⃣ Difference Between Two Dates
date1 = date(2025, 1, 1)
date2 = date(2025, 2, 24)
difference = date2 - date1
print("Difference between two dates:", difference.days, "days")

# 7️⃣ Age Calculation
birth_date = date(1990, 5, 15)
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print("Calculated Age:", age)