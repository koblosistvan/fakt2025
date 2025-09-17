helyezes = int(input("Hányadik lettél a versenyen? "))

if helyezes == 1:
    print("Aranyérem")

elif helyezes == 2:
    print("Ezüstérem")

elif helyezes == 3:
    print("Bronzérem")

elif helyezes < 1:
    print("Ne szórakozz velem")

else:
    print("Nem dobogós")