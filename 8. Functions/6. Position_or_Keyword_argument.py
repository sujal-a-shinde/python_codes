def calculate_marks(maths=0, eng=0, hindi=0, comp=0, history=0):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"the total marks is {total_marks}")


calculate_marks(11, 22, comp=22, history=11, hindi=199)
