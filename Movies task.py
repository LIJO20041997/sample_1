# Write a program that helps a tourist choose tv shows .The program should know about a series of shows that
# a tourist might be interested in. It asks them a series of questions about what kind of show they prefer and gives
# two suggestions for each possibility ( from atleast COMEDY, MUSICAL, HORROR )

p1=input("would you like to see a comedy movie (yes/no): ")
if p1==("yes"):
    yes=input("would you like to see roomanjam or jo&jo: ")
    if yes==("roomanjam"):
        print("play roomanjam")
    elif yes==("jo&jo"):
        print("play jo&jo")
elif p1==("no"):
    no=input("would you like to see a thriller movie(yes/no): ")
    if no==("yes"):
        yes=input("would you lke to see Memories or kooman: ")
        if yes==("memories"):
            print("play memories")
        elif yes==("kooman"):
            print("play kooman")
    elif no==("no"):
        no=input("would you like to see a horror movie(yes/no): ")
        if no==("yes"):
            yes=input("would you like to see preetham or conjuring: ")
            if yes==("preetham"):
                print("play prertham")
            elif yes==("conjuring"):
                print("play conjuring")
        elif no==("no"):
            no=input ("would you like to listen to a music: ")
            if no==("yes"):
                print("play music")
            elif no==("no"):
                no=input("would you like to go to a park: ")



