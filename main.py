import random

class Tables:
    def __init__(self):
        self.students = []
        self.variants = []
        self.testing_table = []
        self.marks = []

    def add_student(self, student_id, student_full_name):
        self.students.append({'student_id': student_id, 'student_full_name': student_full_name})

    def add_variant(self, variant_id):
        self.variants.append({'variant_id': variant_id})

    def generate_testing_table(self):
        if not self.students or not self.variants:
            print("Please add students and variants before generating the testing table.")
            return

        random.shuffle(self.students)
        random.shuffle(self.variants)

        self.testing_table = [{'student_id': student['student_id'], 'variant_id': variant['variant_id']} for student, variant in zip(self.students, self.variants)]

    def add_mark(self, student_id, mark):
        self.marks.append({'student_id': student_id, 'mark': mark})

    def display_testing_table(self):
        for record in self.testing_table:
            student_id = record['student_id']
            variant_id = record['variant_id']
            student_full_name = next((student['student_full_name'] for student in self.students if student['student_id'] == student_id), 'Unknown')
            mark = next((mark['mark'] for mark in self.marks if mark['student_id'] == student_id), 'N/A')
            print(f"Student Name: {student_full_name}, Variant: {variant_id}, Mark: {mark}")

    def get_student_by_name(self, student_full_name):
        student = next((s for s in self.students if s['student_full_name'] == student_full_name), None)
        if student:
            return student
        else:
            print(f"Student with name '{student_full_name}' not found.")
            return None

def main():
    tables = Tables()

    while True:
        print('Menu:')
        print('1 - Add student to the database')
        print('2 - Add variant to the database')
        print('3 - Generate testing table')
        print('4 - Add mark to a student')
        print('5 - Display testing table')
        print('6 - Get student info by name')
        print('0 - Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            student_id = len(tables.students) + 1
            student_full_name = input('Enter student full name: ')
            tables.add_student(student_id, student_full_name)
        elif choice == '2':
            variant_id = len(tables.variants) + 1
            tables.add_variant(variant_id)
        elif choice == '3':
            tables.generate_testing_table()
            print('Testing table has been generated.')
        elif choice == '4':
            student_id = int(input('Enter student ID: '))
            mark = input('Enter mark: ')
            tables.add_mark(student_id, mark)
        elif choice == '5':
            tables.display_testing_table()
        elif choice == '6':
            student_full_name = input('Enter student full name: ')
            student = tables.get_student_by_name(student_full_name)
            if student:
                print(f"Student ID: {student['student_id']}")
        elif choice == '0':
            break
        else:
            print('Invalid choice. Please select a valid option.')

if __name__ == '__main__':
    main()

            print('Такой команды не существует')

if __name__ == '__main__':
    main()
  
