# from igramscraper.instagram import Instagram
from context import Instagram
import time
instagram = Instagram()

# authentication supported
instagram.with_credentials('username', 'password')
instagram.login()
print("logging to instagram .... wait")
time.sleep(1)

thisMedias=instagram.get_medias_by_tag("icecream",25,'')

for media in thisMedias:
	print(media)
