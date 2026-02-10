import re
text = "Hello team , our new product launch is planened for 25/03/2026 at 10.30AM .please contact marketing.team@startupAI.com or support@startupAI.com for more details.Follow us on social media using #startupAI #productlaunch . The early_bird price is $2999(limited offer!!) nad valid for 100 users only"
hastags = re.findall(r"#\+",text)
mentions=re.findall(r"@\w+",text)
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b",text)
url=re.findall(r"https?://^s+",text)
dates=re.findall(r"\b\d{1,2}^d{1,2}^d{4}\b",text)
token=re.findall(r"\b\w+\b",text)
print("Hashtags",hastags)
print("Mentions",mentions)
print("Email",emails)
print("url",url)
print("dates",dates)
print("token",token)
