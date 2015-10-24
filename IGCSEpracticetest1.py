
#-------------------------------------------------------------------------------
#!/usr/bin/env python
classresults = []
result = input
count =1
def dotask1():
    global classresults
    global result
    global count


    while (count < 20):
        print ("enter the candidate name")
        name = input ("Name:")
        if name == "":
            print ("enter a valid name")
        print ("enter candidate number")
        while True:
            result = input ("Number:")
            if str.isnumeric(result):
                break
            else:
                print ("please enter a valid number")
        print ("enter candidate score")
        score = input ("Score: ")
        classresults.append((name, result, score))
        count = count + 1
def dotask2():
    global classresults
    print (classresults)
def dotask3():
    global classresults

def dotask4():
    pass

def main():
    global results
    while True:
        print ("enter a number from 1 to 5")
        print ("1: enter results")
        print ("2:print results file")
        print ("3: calculate averages")
        print ("4: exit")
        choice = input ("Choice:")
        if choice == "1":
            dotask1()
        elif input == "2":
            dotask2()
        elif input == "3":
            dotask3()
        elif input == "4":
            dotask4()
        print("not a valid number")

if __name__ == '__main__':
    main()
