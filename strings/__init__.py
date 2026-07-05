# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


import os
from typing import List

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()

for lang in languages:
    languages[lang]["start_2"] = """<blockquote>💕━━━୨♡୧━━━💕

🌷 𝐻𝑒𝑦 {0}
𝐖𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 {1} 🦢🤍
𝐸𝑛𝑗𝑜𝑦 𝑃𝑟𝑒𝑚𝑖𝑢𝑚 𝑀𝑢𝑠𝑖𝑐 🎶

💞 ⌞𝐴𝑙𝑤𝑎𝑦𝑠 𝑉𝑖𝑏𝑒 • 𝐴𝑙𝑤𝑎𝑦𝑠 𝑇𝑜𝑔𝑒𝑡ℎ𝑒𝑟⌝ 💞

🎧 𝐴𝑑𝑠 𝐹𝑟𝑒𝑒 𝑀𝑢𝑠𝑖𝑐
🎼 24×7 𝑆𝑚𝑜𝑜𝑡ℎ 𝑆𝑡𝑟𝑒𝑎𝑚
💎 𝐻𝑖𝑔ℎ 𝑄𝑢𝑎𝑙𝑖𝑡𝑦

🫶 𝐔𝑠𝑒𝑟 ⇢ @{6}
🩷 𝐁𝑜𝑡 ⇢ {1}

🌸 𝑇𝑎𝑝 𝐻𝑒𝑙𝑝 𝑡𝑜 𝑉𝑖𝑒𝑤 𝐴𝑙𝑙 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠

💕━━━୨♡୧━━━💕

🎵 𝐸𝑛𝑗𝑜𝑦 𝐸𝑣𝑒𝑟𝑦 𝐵𝑒𝑎𝑡 🤍</blockquote>"""


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/VillainMusic
# 📢 Telegram Channel : https://t.me/VillainBots
# ===========================================


# ❤️ Love From VillainBots 
