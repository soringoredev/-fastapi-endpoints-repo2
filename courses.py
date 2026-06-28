from fastapi import FastAPI

app = FastAPI()

COURSES = [
    {'title': 'Python Fundamentals', 'trainer': 'Alex', 'level': 'beginner'},
    {'title': 'Java Backend', 'trainer': 'Maria', 'level': 'intermediate'},
    {'title': 'QA Automation', 'trainer': 'Victor', 'level': 'beginner'},
    {'title': 'Web Basics', 'trainer': 'Elena', 'level': 'beginner'},
    {'title': 'Databases', 'trainer': 'Andrei', 'level': 'intermediate'},
    {'title': 'System Design', 'trainer': 'Irina', 'level': 'advanced'}
]

@app.get('/courses')
async def read_all_courses():
    return COURSES