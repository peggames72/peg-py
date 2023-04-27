import hy as hy
def playai(typ):
    if typ == "aicode":
        hy.hyhome("aicode")
def hyhome(ty):
    if ty == "aicode":
        print("welcome!")
def hyai(ai):
    if ai == "playweb":
        web = input("enter the link to see the ping\n")
        if web == "google":
            print("bug")
            hy.hytext("goodbye")
    if ai == "print":
        prinl = input("your text:\n")
        print(prinl)
        
        
def hytext(text):
    if text == "goodbye":
           print("goodbye!")