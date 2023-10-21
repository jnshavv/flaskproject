import pymysql as p


def getconnection():

    return p.connect(host="localhost", user="root", password="", database="project", port=3306)


def insertrec(t):
    db = getconnection()
    cr = db.cursor()
    sql = "insert into register values(%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql, t)
    db.commit()
    db.close()


def insertrec1(t):
    db = getconnection()
    cr = db.cursor()
    sql = "insert into sendrequest1 values(%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql, t)
    db.commit()
    db.close()



def insertrec2(t):
    db = getconnection()
    cr = db.cursor()
    sql = "insert into donationcamp values(%s,%s,%s,%s,%s)"
    cr.execute(sql, t)
    db.commit()
    db.close()    



def displayrec():
    db = getconnection()
    cr = db.cursor()
    sql = "select name,gender,age,bloodgroup,email,contact from register"
    cr.execute(sql)
    data = cr.fetchall()
# print(data)
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data

# 
def displayrec1():
    db = getconnection()
    cr = db.cursor()
    sql = "select * from sendrequest1"
    cr.execute(sql)
    data = cr.fetchall()
# print(data)
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data




    


def display():
    db = getconnection()
    cr = db.cursor()
    sql = "select * from register"
    cr.execute(sql)
    data = cr.fetchall()
# print(data)
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data
    

def displaydon(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select * from donationcamp  where email=%s"
    cr.execute(sql,email)
    data = cr.fetchall()
# print(data)
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data




   
def displayrec2(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select * from register where email=%s"
    cr.execute(sql,email)
    data = cr.fetchall()
# print(data),email
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data




def selectrec(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select email,password from register where email=%s"
    cr.execute(sql, email)
    data = cr.fetchall()
    # print(data)
    db.commit()
    db.close()
    return data

def selectrec1(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select * from register where email=%s"
    cr.execute(sql, email)
    data = cr.fetchall()
    # print(data)
    db.commit()
    db.close()
    return data[0]


def selectreccamp(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select * from register where email=%s"
    cr.execute(sql, email)
    data = cr.fetchall()
    # print(data)
    db.commit()
    db.close()
    return data[0]



def updaterec(t):
    db = getconnection()
    cr = db.cursor()
    sql = "update register set name=%s,gender=%s,age=%s,bloodgroup=%s,email=%s,password=%s,contact=%s where email=%s"
    cr.execute(sql, t)
    db.commit()
    db.close()


def deleterec(email):
    db = getconnection()
    cr = db.cursor()
    sql = "delete from register where email=%s"
    cr.execute(sql, email)
    db.commit()
    db.close()    


# insertrec(t)


'''b = getconnection()
    cr = db.cursor()
    sql = "select * from registration"
    cr.execute(sql)
    data = cr.fetchall()
# print(datdef displayrec():
    da)
    # for tup in data:
    # print(tup)
    db.commit()
    db.close()
    return data

# displayrec()


def deleterec(id):
    db = getconnection()
    cr = db.cursor()
    sql = "delete from registration where id=%s"
    cr.execute(sql, id)
    db.commit()
    db.close()

# deleterec(102)


def selectrec(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select email,password from registration where email=%s"
    cr.execute(sql, email)
    data = cr.fetchall()
    # print(data)
    db.commit()
    db.close()
    return data

# selectrec(103)


def updaterec(t):
    db = getconnection()
    cr = db.cursor()
    sql = "update registration set id=%s,name=%s,email=%s,password=%s,contact=%s where email=%s"
    cr.execute(sql, t)
    db.commit()
    db.close()


# updaterec(t)
def sel(email):
    db = getconnection()
    cr = db.cursor()
    sql = "select * from registration where email=%s"
    cr.execute(sql, email)
    data = cr.fetchall()
    # print(data)


    
    db.commit()
    db.close()
    return data[0]
'''