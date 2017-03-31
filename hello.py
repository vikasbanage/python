print("\**** Python Hellow world *****\n")
print ("Hello, Python!")
print ("One","Two")


days = ['Synday','Monday','Saturday',
        'Friday']
print (days)

#Complex numbers
d =3+1j*3
print(d)

#paragraph
eassy = """my\
name\
is
vikas"""
print(eassy)

#String and Raw String
nstring = "C:\employee\name"
rstring = r"C:\employee\name"
print(nstring)
print(rstring)

#String Operation
print("\n**** Sting Operation *****\n")
myname = 'VikasBanage'
print(myname)
print(myname[3:5])
print(myname+',Python leader')
print(myname[-2])
print(myname.split('a'))
print(len(myname))
print(myname.find('t'))
print(myname.replace('Banage','Acharya'))
print(myname.startswith('v'))
print(myname.isalpha())
print("Vi" in myname)


#List Operation
print("\n**** List Operation *****")
engineerID = ['bange499', 'aktha497','jain494','thapl499','kulka490']
engineerName = ['Vikas','Ather','Vivek','Martand','Tejashri']
print(engineerID)
print(len(engineerID))
print(engineerID+engineerName)
engineerID[2] = 'sable203'
print(engineerID)
tempID = ['ab001','ab002','ab003',engineerID]
print(tempID)
tempName = ['abc','xyz']

engineerID.append('pahad001')
print(engineerID)
engineerID.insert(2,'shiva500')
print(engineerID)
print(engineerID.count('bange499'))
newlist = zip(engineerID,engineerName)
print(newlist)
if 'ab001' in tempID:
    print("Present")
else:
    print("Not present")
#Set Operation
servers = {'W7028','W7029','W7141','W7028','W7023','W7632'}
print(servers)
ispresent = print('W7028' in servers)

#Squares
sqrs = [x**2 for x in range(10)]
print(sqrs)


#Dictionary
d = {}
d['name'] = 'vikas'
d['job'] = 'support'
d['age'] = 27
print(d)
print(d.keys())
print(d.values())
del(d['age'])
print(d)

#Taking input from user
print("What is your name")
name = input("")

print("Hello %s" %(name))

