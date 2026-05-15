import json

# ---- Simple Questions ----
with open('Data/Questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# ---- Strengthes & Weaknesses  ----
with open('Data/sw.json', 'r', encoding='utf-8') as file:
    sw = json.load(file)

# ---- Jobs for each tip ----
with open('Data/Jobs.json', 'r', encoding='utf-8') as file:
    Jobs = json.load(file)

# ---- Growth tips ----
with open('Data/Growth_tips.json', 'r', encoding='utf-8') as file:
    Growth_tips = json.load(file)

# ---- Famous people ----
with open('Data/Famous_people.json', 'r', encoding='utf-8') as file:
    Famous_people = json.load(file)
