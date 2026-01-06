web_dev = ["Rahul", "Asha", "Neha"]
data_science = ["Kiran", "Meena", "Rohit"]
ui_ux = ["Anjali", "Pooja", "Vikram"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("Arjun")

data_science.insert(1, "Sneha")

ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

first_two_web = web_dev[:2]
print("First two Web Development participants:", first_two_web)

name_lengths = [len(name) for name in data_science_copy]
print("Length of each name in Data Science list:", name_lengths)

asha_present = "Asha" in web_dev or "Asha" in data_science or "Asha" in ui_ux
print("Is Asha in any workshop?", asha_present)

first_participants = (web_dev[0], data_science_copy[0], ui_ux[0])
print("First participant from each workshop:", first_participants)
