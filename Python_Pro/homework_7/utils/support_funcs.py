from __future__ import annotations


def get_convert_student_data(students: list) -> list[dict]:
    ret = []
    for student in students:
        student = student.replace('\n', '').replace(',', '').split()
        if student:
            ret.append({'id': int(student[0]),
                        'height': float(student[1]),
                        'weight': float(student[2])})
    return ret


def load_file(path_file: str) -> list[dict]:
    with open(path_file, 'r') as f:
        students = f.readlines()[1:]
        return get_convert_student_data(students)


def get_average(table: list, header: str) -> int | float:
    quantity_rows = len(table)
    return sum(row[header] for row in table) / quantity_rows
