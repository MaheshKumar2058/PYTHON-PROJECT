email=input("Enter your Email:-")   #g@g.in
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():  # Corrected here
                        k=1
                    elif i.isalpha():
                        if i.isupper():  # Corrected here
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")  
    else:
        print("wrong email 2")
else:
    print("wrong email 1")