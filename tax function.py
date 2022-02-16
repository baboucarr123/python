def tax(Salary):
    T=Salary*0.2
    return T
    
salary=int(input("enteryour salary"))
netsalary=salary-tax(salary)
print("tax",tax(salary))
print("net",netsalary)

