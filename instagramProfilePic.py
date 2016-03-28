import urllib

def get_page(username):
	url = "https://instagram.com/" + username 
	try:
		return urllib.urlopen(url).read()
	except:
		return ""
		
def download_pic (url, name):
	urllib.urlretrieve(url, name)
		
def get_profile_pic (username):
	page = get_page(username)
	if page == "":
		print "# FAILED TO DOWNLOAD #".center(100)
		return

	place = page.find(":image")

	begin_link = place + len(":image") + 11
	
	end_quote = page[begin_link:].find('"')
	end_quote = begin_link + end_quote
	
	profile_link = page[begin_link:end_quote]
	
	download_pic (profile_link, username + ".jpg")
	print "|| SUCCESSFUL DOWNLOAD ||".center(100)
	print

# Main Program

print ".: PICTURE DOWNLOAD INSTAGRAM :.".center(100)
print

while True:
	username = raw_input(">> Insira o nome do usuario (X para finalizar): ").lower()
	if username == "x":
		break
		
	get_profile_pic(username)



