# Slido-Automated-VoteBot
This python script allows you to manipulate the audience data from Sl.ido surveys

Since Slido blocks interference from automated bots by creating a new ID for every vote casted and a new XPATH 'ID' every time the page was refreshed, this tool works around that by scraping the XPath of the desired choice every refresh.

Versions:
selenium==3.141.0
six==1.14.0
urllib3==1.25.9
