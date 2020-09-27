from random import seed
from random import randint

#answer = 1234

def check_location(ans, user) :
    res = 0
    for i in range(len(ans)) :
        if (ans[i] == user[i]):
            res+=1

    return res

def check_samenumber(ans, user) :
    res = 0
    for i in range(len(user)) :
        for j in range(len(ans)) :
            if (user[i] == ans[j] and i != j) :
                res+=1
    return res

def compose_array(num):
    ans = []
    #print(num)

    tmp = num
    while tmp > 0:
        a = tmp % 10
        ans.append(a)
        tmp = int(tmp / 10)
    return ans

def generate_answer():
#    seed(1)
    ansList=[]
    while len(ansList) < 4:
        ans = randint(1,9)
        ansList.append(ans)
        x = 0
        while x < len(ansList)-1 :
            if (ansList[x] == ansList[len(ansList)-1]):
                del ansList[len(ansList)-1]
            else:
                x+=1


    return ansList


def main():
    ans = generate_answer()
#    print(ans)
    #ans = compose_array(answer)
    #print(ans)

    a = 0
    while (a < 4):
        testnum = int(input("Please type a number:"))
        #print(testnum)
 
        user = compose_array(testnum)
        #print(user)

        if (testnum > 10000 or testnum < 1000) :
            print("Number should be 4 digit.")
        a = check_location(ans, user)
        b = check_samenumber(ans, user)
        print(str(a) + " A " + str(b) + " B")

    return

if __name__ == "__main__":
    main()
