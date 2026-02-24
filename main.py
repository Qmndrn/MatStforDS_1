import pandas as pd
from random import randint
from faker import Faker


def get_marks(klass):
    return [randint(3, 5) for mark in range(len(klass["А"]) + len(klass["Б"]))]


def class_jurnal(frame, n, stolb):
    df = pd.DataFrame(frame)
    df["mean"] = (df["matem"] + df["rus"] + df["inform"]) / 3
    
    top = df.sort_values(by="mean", ascending=False).head(n)
    top = top.reset_index(drop=True)
    top = top.reindex(columns=['bukva', 'name', 'matem', 'rus', 'inform', 'mean'])
    
    rezult = df.pivot_table(index=[stolb], values=['matem', 'rus', 'inform'], aggfunc='count')
    
    return rezult, top


def main():
    fake = Faker("ru_RU")
    klass = {
        "А": [fake.first_name() for name in range(10)],
        "Б": [fake.first_name() for name in range(10)]
    }

    subjects = ["matem", "rus", "inform"]

    names = klass["А"] + klass["Б"]
    bukva = ["A"] * len(klass["А"]) + ["B"] * len(klass["Б"])
    parall = [9] * 5 + [10] * 5 + [9] * 5 + [10] * 5

    frame = {
        "name": names,
        "bukva": bukva,
        "parall": parall
    }

    for subject in subjects:
        frame[subject] = get_marks(klass)
    

    rezult, top = class_jurnal(frame, 3, "bukva")

    print("Средний балл по классам:")
    print(rezult)
    print("\nТоп учеников:")
    print(top)


if __name__ == '__main__':
    main()
