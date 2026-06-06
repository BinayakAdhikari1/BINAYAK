import psutil
import tkinter as tk
from tkinter import ttk

def update_processes():
    process_list.delete(*process_list.get_children())

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent']
            mem = round(proc.info['memory_percent'], 2)

            # Simple AI Logic
            if cpu > 10:
                status = "High Resource"
            else:
                status = "Normal"

            process_list.insert(
                "",
                "end",
                values=(pid, name, cpu, mem, status)
            )

        except:
            pass

    root.after(3000, update_processes)


root = tk.Tk()
root.title("AI Smart Process Scheduler")
root.geometry("900x500")

title = tk.Label(
    root,
    text="AI Smart Process & Task Scheduler",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

columns = ("PID", "Process", "CPU %", "Memory %", "Classification")

process_list = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    process_list.heading(col, text=col)
    process_list.column(col, width=150)

process_list.pack(fill="both", expand=True)

update_processes()

root.mainloop()