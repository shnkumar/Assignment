## Learning something
def userfunction(userlist):
    i = len(userlist)
    savestr  = userlist[0]
    j=0
    for j in range(i-1):

        if savestr == ')' or savestr == '}' or savestr == ']':
            print("wrong paranthesis sequence")
            z=[]
            return z
            break
        else:
            if userlist[j+1]== '(' or userlist[j+1]== '{' or userlist[j+1]=='[':

                savestr = userlist[j+1]
                print(" still open", savestr)
                continue
            else:
                if (userlist[j+1] == ')' and savestr == '(') or (userlist[j+1] == '}' and savestr == '{')  or (userlist[j+1] == ']' and savestr == '['):
                    print("paranthesis closed correctly",savestr,userlist[j+1])

                    newStr = list(userlist)
                    print(newStr)
                    newStr.pop(j)
                    newStr.pop(j)
                    print(newStr)
                    return(newStr)
                    break


                else:
                    print("wrongly closed!!")
                    z = []
                    return z
                    break

if __name__ == '__main__':
    mystring = '(){}[()](()'
    newStr = list(mystring)
    print(newStr)

    while len(newStr) >= 1 :
        x=userfunction(newStr)
        newStr = x
        print("in main:",newStr,len(newStr))

        if len(newStr)== 1:
          print("wrongly closed!")
          break

        print(x)










