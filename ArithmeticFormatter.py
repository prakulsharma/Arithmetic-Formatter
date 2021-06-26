#!/usr/bin/env python
# coding: utf-8

# In[1]:


def arithmetic_arranger(problems,result=False):
    numOfProb = len(problems)
    str = ""
    problemList = []
    finalstr = ""  
    firststr = ""
    secstr = ""
    thirdstr = ""
    forstr = ""
    calList = []
    
    # Condition 1: Number of problems
    if numOfProb > 5 :
        return "Error: Too many problems."
    for i in range(numOfProb):
        if len(problems[i].split(" ")) != 3:
            # Condition 2: Wrong format
            return "Error: Wrong format"     
        problemList.append(problems[i].split(" "))
        if problemList[i][1] != '+' and problemList[i][1] != '-':
            # Condition 3: Wrong operator
            return "Error: Operator must be '+' or '-'."
        if len(problemList[i][0]) > 4 or len(problemList[i][2]) > 4:
            # Condition 4: Max number of digits
            return "Error: Numbers cannot be more than four digits."
        if problemList[i][0].isnumeric() == False or problemList[i][2].isnumeric() == False:
            # Condition 5: Only digits
            return "Error: Numbers must only contain digits."
         
    for i in range(numOfProb):
        if i == (numOfProb-1):
            operand1 = problemList[i][0]
            operator = problemList[i][1]
            operand2 = problemList[i][2]
            olen1 = len(operand1)
            olen2 = len(operand2)
            res = 0

            if operator == "+":
                res = int(operand1) + int(operand2)
            else:
                res = int(operand1) - int(operand2)

            resStr = "{}".format(res) 

            if olen1 > olen2:
                firststr = firststr + operand1.rjust(olen1+2)
                secstr = secstr + operator + operand2.rjust(olen1+1)
                thirdstr = thirdstr + "-"*(olen1+2)
                forstr = forstr + resStr.rjust(olen1+2)
            else:
                firststr = firststr + operand1.rjust(olen2+2)
                secstr = secstr + operator + " " + operand2.rjust(olen2)
                thirdstr = thirdstr + "-"*(olen2+2)
                forstr = forstr + resStr.rjust(olen2+2)
        else:
            operand1 = problemList[i][0]
            operator = problemList[i][1]
            operand2 = problemList[i][2]
            olen1 = len(operand1)
            olen2 = len(operand2)
            res = 0

            if operator == "+":
                res = int(operand1) + int(operand2)
            else:
                res = int(operand1) - int(operand2)

            resStr = "{}".format(res) 

            if olen1 > olen2:
                firststr = firststr + operand1.rjust(olen1+2) + "    "
                secstr = secstr + operator + operand2.rjust(olen1+1) + "    "
                thirdstr = thirdstr + "-"*(olen1+2) + "    "
                forstr = forstr + resStr.rjust(olen1+2) + "    "
            else:
                firststr = firststr + operand1.rjust(olen2+2) + "    "
                secstr = secstr + operator + " " + operand2.rjust(olen2) + "    "
                thirdstr = thirdstr + "-"*(olen2+2) + "    "
                forstr = forstr + resStr.rjust(olen2+2) + "    "

    if result == False:
        finalstr = firststr + "\n" + secstr + "\n" + thirdstr
        return finalstr
    else:
        finalstr = firststr + "\n" + secstr + "\n" + thirdstr + "\n" + forstr
        return finalstr


# In[2]:


print(arithmetic_arranger(["234 + 656", "1 - 8001", "7463 + 9878", "9999 + 1", "544 - 22"]))


# In[3]:


print(arithmetic_arranger(["234 + 656", "1 - 8001", "7463 + 9878", "9999 + 1", "544 - 22"], True))

