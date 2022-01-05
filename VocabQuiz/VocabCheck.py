#This file for checking vocabulary testing programme for beginner to advance purpose in this programe show hindi meaning word and user give english word for this hindi meaning.


from tkinter import *
from tkinter import messagebox
from insert import *
from tempInsert import *


root = Tk()
root.title("VocabQuiz")
root.geometry("400x250+10+10")
root.resizable(False, False)
root.configure(background='#8F5902')

entry = Entry(font=('Verdana', 18),width=23, bg='white',bd=3, fg='green')
entry.place(x=20, y=150)

#Both are Fetching random data from given database
cursor = conn.execute("SELECT id, words, meaning from VOCABULARY ORDER BY RANDOM() LIMIT 1")
cursor1 = newConn.execute("SELECT id, words, meaning from VOCABULARY RANDOM LIMIT 1")

def checkReal(row):
    '''Here function check parameter value of input value are same or not''' 

    #Asks English word for given Hindi meaning word
    word = str(entry.get())
    # print(word)

    #This condition checks whether the given word and the English word are the same or not
    if word == row[1].lower():
        # print("Your answer is correct!!")
        newData(row[0], row[1], row[2])

        index = row[0]
        delete = '''DELETE from VOCABULARY where ID = ?'''
        conn.execute(delete, (index,))
        conn.commit()
        root.destroy()
    else:
        messagebox.askretrycancel("Incorrect Word", "Try again?")
        # print("Your answer is not correct!!")

def checkTemp(row):
    '''Here function check parameter value of input value are same or not''' 

    #Asks English word for given Hindi meaning word
    word = str(entry.get())
    # print(word)

    #This condition checks whether the given word and the English word are the same or not
    if word == row[1].lower():
        # print("Your answer is correct!!")
        insertData(row[0], row[1], row[2])

        index = row[0]
        delete = '''DELETE from VOCABULARY where ID = ?'''
        newConn.execute(delete, (index,))
        newConn.commit()
        root.destroy()
    else:
        messagebox.askretrycancel("Incorrect Word", "Try again?")
        # print("Your answer is not correct!!")


def realVocabFile():
    global cursor

    #'fetchall' fuction check fetched data is empty or not
    if len(cursor.fetchall()) != 0:
        cursor = conn.execute("SELECT id, words, meaning from VOCABULARY ORDER BY RANDOM() LIMIT 1")
        for row in cursor:
            hindi = StringVar(root, row[2])
            label = Message(root, textvariable=hindi,relief=RAISED, font=('Verdana', 16, 'bold'), width=250, bg='white', fg='green')
            label.place(x=75, y=65)

            message_label = Label(text=' Put English Meaning ', font=('Verdana', 16, 'bold'),bg='green', fg='white')
            message_label.place(x=35, y=120)


            chang_button = Button(text='Ok', font=('Verdana', 16), bg='red', bd=3, fg='white', command=lambda: checkReal(row))
            chang_button.place(x=155, y=200)

    else:
        with open('/VocabQuiz/test.txt', mode='w') as file:
            file.write("tempVocabFile")
        tempVocabFile()

def tempVocabFile():
    global cursor1 
    if len(cursor1.fetchall()) != 0:
        cursor1 = newConn.execute("SELECT id, words, meaning from VOCABULARY RANDOM LIMIT 1")
        for row in cursor1:
            hindi = StringVar(root, row[2])
            label = Message(root, textvariable=hindi,relief=RAISED, font=('Verdana', 16, 'bold'), width=250, bg='white', fg='green')
            label.place(x=75, y=65)

            message_label = Label(text=' Put English Meaning ', font=('Verdana', 16, 'bold'),bg='green', fg='white')
            message_label.place(x=35, y=120)


            chang_button = Button(text='Ok', font=('Verdana', 16), bg='red', bd=3, fg='white', command=lambda: checkTemp(row))
            chang_button.place(x=155, y=200)
    else:
        with open('/VocabQuiz/test.txt', mode='w') as file:
            file.write("realVocabFile")
        realVocabFile()

if __name__ == '__main__':

    message_label1 = Label(text=' Hindi to English VocabCheck', font=('Verdana', 16, 'bold'), bg='white', fg='green')
    message_label1.place(x=20, y=20)

    with open('/VocabQuiz/test.txt', mode='r') as file:
        fun = file.read()
        if fun == 'realVocabFile':
            realVocabFile()
        else:
            tempVocabFile()

mainloop()

