import uuid
from datetime import datetime
import csv

class NOTE:

    def __init__(self, title, body):
        self.id = str(uuid.uuid4())
        self.title = title
        self.body = body
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())


class NOTE_2:

    def __init__(self):
        self.notes = {}

    def read_notes(self, path):
        with open(path, "r") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if len(row) > 0:
                    note = NOTE(row[1], row[2])
                    note.id = row[0]
                    note.created_at = row[3]
                    note.updated_at = row[4]
                    self.notes[note.id] = note
    def PRINT(self):
        num = 0
        for note_id in self.notes:
            note = self.notes[note_id]
            num += 1
            print(
                f"\nId:{note.id}\n{note.title}\n{note.body}\nСоздано: {note.created_at}\nИзменено: {note.updated_at}\n")

    def ADD(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        note = NOTE(title, body)
        self.notes[note.id] = note
        print("Заметка успешно создана!")

    def EDIT(self):
        note_id = input("Введите id: ")
        if note_id in self.notes:
            title = input("Введите новый заголовок: ")
            body = input("Внесите изменения в тело заметки: ")
            note = self.notes[note_id]
            note.title = title
            note.body = body
            note.updated_at = str(datetime.now())
            print("Заметка успешно изменена!")
        else:
            print("Заметка не найдена!")

    def DEL(self):
        note_id = input("Введите id: ")
        if note_id in self.notes:
            del self.notes[note_id]
            print("Заметка успешно удалена!")
        else:
            print("Заметка не найдена!")

    def SAVE(self, path):
        with open(path, "w") as f:
            writer = csv.writer(f, delimiter=";")
            for note_id in self.notes:
                note = self.notes[note_id]
                writer.writerow([note.id, note.title, note.body,
                                note.created_at, note.updated_at])
                print("Данные сохранены!")

    

if __name__ == "__main__":
    
    notes = NOTE_2()
    path = "notes.csv"
    try:
        notes.read_notes(path)
    except IOError:
        file = open(path, 'w')
    finally:
        notes.read_notes(path)
        
    print("Добро пожаловать в приложение заметки!")    

    while True:
        print("1) Показать все заметки")
        print("2) Добавить новую заметку")
        print("3) Изменить заметку")
        print("4) Удалить заметку")
        print("5) Сохранить")
        print("z) Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            notes.PRINT()
        elif choice == "2":
            notes.ADD()
        elif choice == "3":
            notes.EDIT()
        elif choice == "4":
            notes.DEL()
        elif choice == "5":
            notes.SAVE(path)
        elif choice == "z":
            break
