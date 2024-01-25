text="""2001,Historic Kolkata Test, Bhajji takes a Hattrick V Steve Waugh's Invincible Aus Team.  
@harbhajan_singh
 became the 1st Indian to take a Test """
words=text.split(" ")
for w in words:
    if w.startswith('@'):
        print(w)