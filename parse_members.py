import os
import re

raw_data = """
김지민	10기	학회원
이지민	10기	학회원
정연석	10기	학회원
최진우	10기	학회원
주승현	10기	학회원
김진영	10기	학회원
양준혁	10기	학회원
이호준	10기	학회원
박영선	10기	학술팀장
정세빈	10기	임원진,학술팀장
김태연	10기	임원진,홍보팀장
김진호	10기	임원진,회장
손창기	9기	학회원
김지호	9기	학회원
조진형	9기	학회원
김현아	9기	학회원
김예연	9기	학회원
김민준	9기	학회원
최인열	9기	학회원
고대현	9기	학회원
유희라	9기	학회원
김기수	8기	학회원
정서영	8기	학회원
이영석	8기	학회원
송겸희	8기	학회원
윤효정	7기	학회원
유대명	7기	임원진,학술팀장
김한성	6기	학회원
박세연	7기	임원진,회장
지민경	5기	임원진
이가은	3기	학회원
문희주	1기	학회원
강수연	6기	학회원
김예원	1기	학회원
이한울	2기	임원진
김정은	1기	기획팀장,임원진
정지휴	6기	임원진,회장
신다혜	3기	학회원
현정섭	2기	학회원
서연우	6기	학회원
이지연	7기	학회원
이동찬	2기	학회원
박현진	3기	학회원
안주영	1기	학회원
송주혜	6기	HR팀장,임원진
김찬영	7기	임원진,총무팀장
이상윤	6기	학회원
정지영	6기	학회원
나건주	4기	임원진
이정운	1기	운영지원팀장,임원진
신인호	7기	기획팀장,임원진,회장
김성진	1기	학회원
김예찬	1기	임원진,회장
최민	6기	학회원
윤창원	1기	기획팀장
김보배	4기	임원진
김가영	5기	임원진
박성은	4기	임원진
용예린	6기	학회원
백경호	1기	학회원
성민석	1기	임원진,자료연구팀장
조현경	3기	임원진
손규진	3기	임원진
김종현	3기	학회원
이우주	6기	학회원
장건	8기	운영지원팀장,임원진
이승한	3기	임원진
이해인	6기	학회원
이승환	7기	학회원
김강민	6기	학회원
이은규	9기	학회원
홍동우	7기	학회원
김규리	7기	학회원
박지원	5기	임원진
이문기	6기	HR팀장,임원진
홍지중	2기	임원진
전승원	6기	기획운영팀장
전민진	1기	학회원
이석준	7기	임원진
김정현	3기	학회원
김다은	7기	학회원
정욱준	2기	학회원
정민기	1기	학회원
이연진	2기	임원진
편정욱	1기	학회원
안희재	1기	학회원
이재성	1기	임원진,회장
최강현	8기	학회원
"""

cohorts = {}

# Parse data
for line in raw_data.strip().split('\n'):
    parts = re.split(r'\s+|\t+', line.strip())
    if len(parts) >= 2:
        name = parts[0]
        cohort_str = parts[1]
        role = "".join(parts[2:]) if len(parts) > 2 else ""
        
        # Extract number from "10기"
        cohort_num = re.sub(r'[^0-9]', '', cohort_str)
        
        if not cohort_num:
            continue
            
        if cohort_num not in cohorts:
            cohorts[cohort_num] = []
            
        cohorts[cohort_num].append({
            "name": name,
            "affiliation": role,
            "photo": "/images/person.jpg"
        })

# Write to files
base_path = r"c:\Users\FELAB\Desktop\Python_venv\finda_homepage\content\members"

# Ensure directory exists (it should)
os.makedirs(base_path, exist_ok=True)

# Process cohorts 1 to 10 (or max found)
# User data covers 1 to 10.
# We generated 1..11 before. We should update 1..10 and maybe leave 11 empty or delete it if not needed?
# I'll just update the ones present in data, and ensure files exist.

for i in range(1, 12): # Cover 1 to 11
    s_i = str(i)
    members = cohorts.get(s_i, [])
    
    # Generate YAML array for members
    members_yaml = ""
    if members:
        members_yaml = "members:\n"
        for m in members:
            members_yaml += f"  - name: \"{m['name']}\"\n"
            members_yaml += f"    affiliation: \"{m['affiliation']}\"\n"
            members_yaml += f"    photo: \"{m['photo']}\"\n"
    else:
        # Keep empty placeholder if no data for this cohort (like 11)
        members_yaml = "members: []\n"

    content = f"""---
title: "{s_i}기"
weight: {s_i}
{members_yaml}---
"""
    
    file_path = os.path.join(base_path, f"{s_i}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Members updated successfully.")
