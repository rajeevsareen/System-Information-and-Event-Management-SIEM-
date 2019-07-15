import MySQLdb
db = MySQLdb.connect("localhost","root","root","siem")
cursor = db.cursor()
f = open("pathto\\dism.txt")
lines = f.readlines()
length = len(lines)
i = 0
for i in range(0,length):
    i = lines[i].strip()
    i = i.split()
    if(i[2] == 'Info' or i[2] == 'Warning'):
        
        time = i[1]
        time = time[:-1]
        desc = i[4:]
        desc = ' '.join(desc)
        desc = desc.replace("'","")
        desc = desc.replace('"',"")
        sql = "Insert into info values('" + i[0] + "','" + time + "','" + i[2] + "','" + i[3] + "','" + desc + "')"
        cursor.execute(sql)
    else:
        desc = i[2:]
        desc = ' '.join(desc)
        desc = desc.replace("'","")
        desc = desc.replace('"',"")
        sql = "Insert into error values('" + i[0] + "','" + i[1] + "','" + desc + "')"
        cursor.execute(sql)
        
db.commit()

print("LOG FILE HAS BEEN SCANNED AND RESLUTS ARE STORED IN DATABASE")
