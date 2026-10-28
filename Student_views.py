import mysql.connector
from mysql import connector
import datetime


class Student_Management:
    def __init__(self):
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Afreen@2004",
            database = "student_db"
        )
        print("Connected Successfully...!")
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from student where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return  record
        except Exception as e:
            return None
    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into student(Name,Department,Phone,Place,College,Joined_date) values(%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Student added Successfully...!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from student"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id = None):
        try:
            record = self.get_object(id = id)
            if record == None:
                print("Record not found...!")
            else:
                print(record)
        except Exception as e:
            print(e)
    def delete(self,id= None):
        try:
            record = self.get_object(id = id)
            values = (id,)
            if record != None:
                query = "Delete from student where id = %s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Student deleted successfully...!")
            else:
                print("Student not found...!")
        except Exception as e:
            print(e)
    def put(self,id = None,**kwargs):
        try:
            record = self.get_object(id = id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs:
                    placeholder += k + "=%s,"
                placeholder = placeholder.rstrip(",")
                query = f"update student set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Student details updated successfully...!")
            else:
                print("Student not found...!")
        except Exception as e:
            print(e)


student_instance = Student_Management()                        #create an object
# student_instance.post(name= "Amritha",Department= "ECE",Phone = "9895647648",Place= "Palakkad",College = "MEA",Joined_date = datetime.datetime.today())
student_instance.get()
print("_ _ _ _ Details of one student _ _ _ _")
student_instance.retrieve(id=2)
print("_ _ _ _ Delete operation _ _ _ _")
student_instance.delete(id = 5)
print("_ _ _ _ Updation _ _ _ _");
student_instance.put(4,department = "ECE")