# -*- coding: windows-1251 -*-
import tkinter as tk
import sqlite3
from prettytable import from_db_cursor

# Создание соединения с базой данных
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
             (
             name TEXT,
             phone TEXT,
             email TEXT,
             age INTEGER)''')

# Функция для добавления контакта в базу данных
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    cursor.execute("INSERT INTO contacts VALUES (?, ?, ?, ? )", ( name, phone, email, age))
    conn.commit()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Функция для поиска контакта по имени
def search_by_name():
    name = name_search_entry.get()
    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    result = cursor.fetchall()
    if result:
        name = from_db_cursor(cursor)
        result_label.config(text=name)
    else:
        result_label.config(text="Контакт не найден.")

# Функция для поиска контакта по номеру телефона
def search_by_phone():
    phone = phone_search_entry.get()
    cursor.execute("SELECT * FROM contacts WHERE phone=?", (phone,))
    result = cursor.fetchall()
    if result:
        table = from_db_cursor(cursor)
        result_label.config(text=table)
    else:
        result_label.config(text="Контакт не найден.")

# Функция для поиска контакта по адресу электронной почты
def search_by_email():
    email = email_search_entry.get()
    cursor.execute("SELECT * FROM contacts WHERE email=?", (email,))
    result = cursor.fetchall()
    if result:
        table = from_db_cursor(cursor)
        result_label.config(text=table)
    else:
        result_label.config(text="Контакт не найден.")

# Функция для поиска контакта по возрасту
def search_by_age():
    age = age_search_entry.get()
    cursor.execute("SELECT * FROM contacts WHERE age=?", (age,))
    result = cursor.fetchall()
    if result:
        table = from_db_cursor(cursor)
        result_label.config(text=table)
    else:
        result_label.config(text="Контакт не найден.")

# Создание графического интерфейса
root = tk.Tk()
root.title("Контактная книга")

name_label = tk.Label(root, text="Имя:")
name_entry = tk.Entry(root)
phone_label = tk.Label(root, text="Телефон:")
phone_entry = tk.Entry(root)
email_label = tk.Label(root, text="Электронная почта:")
email_entry = tk.Entry(root)
age_label = tk.Label(root, text="Возраст:")
age_entry = tk.Entry(root)

add_button = tk.Button(root, text="Добавить", command=add_contact)

name_search_label = tk.Label(root, text="Поиск по имени:")
name_search_entry = tk.Entry(root)
search_by_name_button = tk.Button(root, text="Найти")
phone_search_label = tk.Label(root, text="Поиск по телефону:")
phone_search_entry = tk.Entry(root)
search_by_phone_button = tk.Button(root, text="Найти", command=search_by_phone)

email_search_label = tk.Label(root, text="Поиск по почте:")
email_search_entry = tk.Entry(root)
search_by_email_button = tk.Button(root, text="Найти", command=search_by_email)

age_search_label = tk.Label(root, text="Поиск по возрасту:")
age_search_entry = tk.Entry(root)
search_by_age_button = tk.Button(root, text="Найти", command=search_by_age)

result_label = tk.Label(root, text="Результаты поиска:")

# Определение макета
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
phone_label.grid(row=1, column=0)
phone_entry.grid(row=1, column=1)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
age_label.grid(row=3, column=0)
age_entry.grid(row=3, column=1)

add_button.grid(row=4, column=1)

name_search_label.grid(row=5, column=0)
name_search_entry.grid(row=5, column=1)
search_by_name_button.grid(row=5, column=2)

phone_search_label.grid(row=6, column=0)
phone_search_entry.grid(row=6, column=1)
search_by_phone_button.grid(row=6, column=2)

email_search_label.grid(row=7, column=0)
email_search_entry.grid(row=7, column=1)
search_by_email_button.grid(row=7, column=2)

age_search_label.grid(row=8, column=0)
age_search_entry.grid(row=8, column=1)
search_by_age_button.grid(row=8, column=2)

result_label.grid(row=9, column=0, columnspan=3)

# Запуск главного цикла

root.mainloop()
# Закрытие соединения с базой данных
conn.close()

if __name__ == '__app__':
    root.mainloop()

