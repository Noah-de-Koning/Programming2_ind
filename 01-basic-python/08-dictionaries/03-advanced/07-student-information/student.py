# Write your code here
def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students

def average_age(data):
    sum_ages = 0
    count = 0
    for student in data.values():
        sum_ages += student['age']
        count += 1
    return sum_ages/count

def courses(data):
    result_set = set()
    for student in data.values():
        result_set.update(student['courses'])
    return result_set

def most_common_courses(data):
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    max_count = max(course_counts.values())
    return {
        course 
        for course in course_counts.keys()
        if course_counts[course] == max_count
    }