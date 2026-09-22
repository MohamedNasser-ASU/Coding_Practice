import re
url = input("url: ").strip()

if username := re.search( r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(username.group(1))
