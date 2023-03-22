import tkinter as t
import pyodbc


class SQLlogin:
    def __init__(self):
        self.main_window = t.Tk()

        self.main_window.geometry("350x125")
        self.main_window.title("SQL Server Login")
        
        self.top_frame = t.Frame(self.main_window)
        self.middle_frame = t.Frame(self.main_window)
        self.bottom_frame = t.Frame(self.main_window)

        self.top_frame.pack(side= "top")
        self.middle_frame.pack(side= "top")
        self.bottom_frame.pack(side= "top")

        self.login = t.Label(self.top_frame, text="Login:             ")
        self.login_entry = t.Entry(self.top_frame, width=25)

        self.password = t.Label(self.middle_frame, text="Password:      ")
        self.password_entry = t.Entry(self.middle_frame, width=25, show="*")



        self.login.pack(side="left")
        self.login_entry.pack(side="right")

        self.password.pack(side="left")
        self.password_entry.pack(side="right")


        self.login_button = t.Button(self.bottom_frame, text="Login", command=self.access_database)

        self.login_button.pack(side="left")


        t.mainloop()

    def access_database(self):
        user_login = self.login_entry.get()
        user_password = self.password_entry.get()

        self.main_window.destroy()

        

        cn_str = (
    
    'Driver={SQL Server Native Client 11.0};'      #data source driver, go to administrative

    'Server=MIS-SQLJB;'             #server name

    'Database=School;'              #database name

    'UID='+user_login+';'                #username

    'PWD='+user_password+';'             #password

    )
        
        #connect to server

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute ('select * from School.dbo.Course')

        data = cursor.fetchall()
        
        for course in data:
            print("CourseID:     ", course[0])
            print("Course Name:  ", course[1])
            print("Credit Hours: ", course[2])
            print("DepartmentID: ", course[3])
            print()

myinstance = SQLlogin()