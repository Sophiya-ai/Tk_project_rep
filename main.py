import tkinter as tk
from tkinter import messagebox


class ListManager:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        #self.tasks_del =[]

        self.text1 = tk.Label(root, text="Введите задачу - ", bg="AliceBlue", font=("Arial", 12))
        self.text1.grid(column=0, row=1, columnspan=2, padx=5, sticky="e")
        self.task_entry = tk.Entry(root, width=50, bg="khaki2", font=("Arial", 11))
        self.task_entry.grid(column=2, row=1, ipady=6)

        self.img_save = tk.PhotoImage(file="save.png")
        self.ed_task_b = tk.Button(root, text="Добавить задачу    ", image=self.img_save, compound="right",
                                   font=("Arial Bold", 11), command=self.add_task)
        self.ed_task_b.grid(row=1, column=3, ipadx=30, ipady=2, padx=5, pady=10, sticky="w")

        self.img_list = tk.PhotoImage(file="list.png")
        self.text2 = tk.Label(root, text="Список задач  ", image=self.img_list, compound="right", font=("Arial", 12))
        self.text2.grid(column=1, row=2, pady=5)
        self.task_list = tk.Listbox(root, height=10, width=50, bg="grey85", font=("Arial", 11))
        self.task_list.grid(column=1, row=3)
        self.task_list.bind("<<ListboxSelect>>", self.change_task_num)

        self.done_task_b = tk.Button(root, text="Задача выполнена", font=("ArialBold", 11), command=self.done_task)
        self.done_task_b.grid(column=1, row=4, pady=5)

        self.del_task_b = tk.Button(root, text="Удалить задачу", font=("Arial Bold", 11), command=self.del_task)
        self.del_task_b.grid(column=1, row=5, ipadx=10)

        self.move_task = tk.Label(root, text="\n"
                                             "Перемещение задачи в Списке задач \n "
                                             "   - встаньте на задачу в Списке выше \n "
                                             "- введите номер её новой позиции:", font=("Arial", 12))
        self.move_task.grid(column=1, row=6, sticky="sw")
        self.task_Num_move = tk.Entry(root, bg="khaki2", width=5, font=("Arial", 12))
        self.task_Num_move.grid(column=1, row=7, sticky="se", ipady=6)

        self.update_task_b = tk.Button(root, text="Обновить список задач", font=("Arial Bold", 11),
                                       command=self.change_task_num)
        self.update_task_b.grid(column=1, row=8, pady=5, sticky="se")

        self.img_done = tk.PhotoImage(file="done.png")
        self.text3 = tk.Label(root, text="Список выполненных задач  ", image=self.img_done, compound="right",
                              font=("Arial", 12))
        self.text3.grid(column=2, row=2, pady=5)
        self.task_list_done = tk.Listbox(root, height=10, width=50, bg="pale green", font=("Arial", 11))
        self.task_list_done.grid(column=2, row=3)

        self.ed_task_Num_done = tk.Label(root, text="Введите номер позиции для возврата  \n "
                                                    "задачи в Cписок задач на доработку:", font=("Arial", 12))
        self.ed_task_Num_done.grid(column=2, row=4)

        self.task_Num_entry_done = tk.Entry(root, width=5, bg="khaki2", font=("Arial", 12))
        self.task_Num_entry_done.grid(column=2, row=5, ipady=6)

        self.back_task_b_done = tk.Button(root, text="Вернуть задачу на доработку", font=("Arial Bold", 11), command=self.back_task_done)
        self.back_task_b_done.grid(column=2, row=6, sticky="n", pady=5)

        self.img_del = tk.PhotoImage(file="del.png")
        self.text4 = tk.Label(root, text="Список удаленных задач   ", image=self.img_del, compound="right",
                              font=("Arial", 12))
        self.text4.grid(column=3, row=2, pady=5)
        self.task_list_del = tk.Listbox(root, height=10, width=50, bg="salmon1", font=("Arial", 11))
        self.task_list_del.grid(column=3, row=3)
        self.task_list_del.bind("<<ListboxSelect>>", self.back_task_del)

        self.ed_task_Num = tk.Label(root, text="Введите номер позиции задачи  \n "
                                               "для ввода её в Cписок задач:", font=("Arial", 12))
        self.ed_task_Num.grid(column=3, row=4)

        self.task_Num_entry = tk.Entry(root, width=5, bg="khaki2", font=("Arial", 12))
        self.task_Num_entry.grid(column=3, row=5, ipadx=1, ipady=6)

        self.back_task_b = tk.Button(root, text="Вернуть задачу в Список задач", font=("Arial Bold", 11), command=self.back_task_del)
        self.back_task_b.grid(column=3, row=6, sticky="n", pady=5)

        self.img_file = tk.PhotoImage(file="file.png")
        self.save_b = tk.Button(root, text="Сохранить списки в файлы   ", image=self.img_file, compound="right",
                                font=("Arial Bold", 11), command=self.save)
        self.save_b.grid(column=3, row=8, sticky="n", ipadx=12, ipady=2,  pady=5)

        self.img_ofile = tk.PhotoImage(file="open_file.png")
        self.open_b = tk.Button(root, text="Открыть сохраненные списки   ", image=self.img_ofile, compound="right",
                                font=("Arial Bold", 11), command=self.open)
        self.open_b.grid(column=3, row=9, sticky="n", ipadx=2, ipady=3)

    # Обновить Список задач на интерфейсе
    def update_tasks(self):
        self.task_list.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            self.task_list.insert(tk.END, f"{i}: {task}")

    # добавить задачу в Список задач
    def add_task(self):
        self.tasks.append(self.task_entry.get())
        if self.task_entry.get():
            self.update_tasks()
            self.task_entry.delete(0, tk.END)

    #задача удалена
    def del_task(self):
        selected_del_index = self.task_list.curselection()
        if selected_del_index:
            index = selected_del_index[0]
            element = self.tasks[index]
            if " *" in element:
                new = element.replace(" *", "")
            elif " +" in element:
                new = element.replace(" +", "")
            else:
                new = element
            self.task_list_del.insert(tk.END, new)
            del self.tasks[index]
            self.update_tasks()

    # задача решена
    def done_task(self):
        selected_done_index = self.task_list.curselection()
        if selected_done_index:
            index = selected_done_index[0]
            element = self.tasks[index]
            if " *" in element:
                new = element.replace(" *", "")
            elif " +" in element:
                new = element.replace(" +", "")
            else:
                new = element
            self.task_list_done.insert(tk.END, new)
            del self.tasks[index]
            self.update_tasks()

    #изменение позиции выбранной задачи в Списке выполняемых задач
    def change_task_num(self, event=None):
        selected_for_change_index = self.task_list.curselection()
        new_index = self.task_Num_move.get()
        try:
            if selected_for_change_index and new_index and 0 <= int(new_index) <= len(self.tasks)+1:
                index = selected_for_change_index[0]
                element = self.tasks.pop(index)
                self.tasks.insert(int(new_index), element)
                self.update_tasks()
                self.task_Num_move.delete(0, tk.END)
        except (ValueError):
            messagebox.showinfo("Ошибка!", "Введите корректное число новой позиции \n"
                                           "и снова кликните по выбранной задаче!")
            self.task_Num_move.delete(0, tk.END)

    # возврат выбранной задачи из удаленных в Список выполняемых задач
    def back_task_del(self, event=None):
        sel = self.task_list_del.curselection()
        index = self.task_Num_entry.get()
        try:
            if sel and index and 0 <= int(index) <= len(self.tasks) + 1:
                index_sel = sel[0]
                element = self.task_list_del.get(index_sel)
                self.tasks.insert(int(index), element+" *")
                self.task_list_del.delete(index_sel)
                self.update_tasks()
                self.task_Num_entry.delete(0, tk.END)
        except (ValueError):
            messagebox.showinfo("Ошибка!", "Введите ЧИСЛО (не символ) позиции задачи \n"
                                           "и снова кликните по выбранной задаче!")
            self.task_Num_entry.delete(0, tk.END)


    # возврат выбранной задачи из сделанных в Список выполняемых задач на доработку
    def back_task_done(self, event=None):
        sel = self.task_list_done.curselection()
        index = self.task_Num_entry_done.get()
        try:
            if sel and index and 0 <= int(index) <= len(self.tasks) + 1:
                index_sel = sel[0]
                element = self.task_list_done.get(index_sel)
                self.tasks.insert(int(index), element+" +")
                self.task_list_done.delete(index_sel)
                self.update_tasks()
                self.task_Num_entry_done.delete(0, tk.END)
        except (ValueError):
            messagebox.showinfo("Ошибка!", "Введите корректное число позиции задачи \n"
                                           "и снова кликните по выбранной задаче!")
            self.task_Num_entry_done.delete(0, tk.END)

    def save(self):
        with open("agenda.txt", "w", encoding="utf-8") as file:
            items = self.task_list.get(0, tk.END)
            for i in items:
                ind = i.find(" ")
                i_new = i[(ind+1):]
                file.write(f"{i_new}\n")

        with open("done.txt", "w", encoding="utf-8") as file:
            items1 = self.task_list_done.get(0, tk.END)
            for i in items1:
                file.write(f"{i}\n")

        with open("del.txt", "w", encoding="utf-8") as file:
            items2 = self.task_list_del.get(0, tk.END)
            for i in items2:
                file.write(f"{i}\n")

    def open(self):
        with open("agenda.txt", "r", encoding="utf-8") as file:
            items = file.readlines()
            for i in items:
                self.task_list.insert(tk.END,f"{items.index(i)}: {i}")
                self.tasks.append(i)

        with open("done.txt", "r", encoding="utf-8") as file:
            items1 = file.readlines()
            for i in items1:
                self.task_list_done.insert(tk.END, i)

        with open("del.txt", "r", encoding="utf-8") as file:
            items2 = file.readlines()
            for i in items2:
                self.task_list_del.insert(tk.END, i)

root = tk.Tk()
root.geometry("1212x580")
root.title("Task Manager")
app = ListManager(root)

root.mainloop()
