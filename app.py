SUPABASE_URL = "https://lecrzllvgroghwmsrzll.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxlY3J6bGx2Z3JvZ2h3bXNyemxsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2MzU4MzQsImV4cCI6MjA5MTIxMTgzNH0.U6CU5KiqMTUF_H7mWLCgXjBSMAiA54m7tJ28r9OlrT0"

from supabase import create_client
import streamlit as st

db = create_client(SUPABASE_URL,SUPABASE_KEY)
st.title('P1 - Student Records')

#INSERT run once, then comment out

student = [

    {"name":"Ali Hassan", "email":"ali@uni.edu","age":20, "gpa":3.8},

    {"name":"Siti Aishah", "email":"siti@uni.edu", "age":21, "gpa":3.2},

    {"name": "Raj Kumar", "email":"rajäuni.edu", "age":15, "gpa":2.91},

    {"name": "Lin wel","email": "lin@uni.edu", "age":22, "gpa":3.5},
]

db.table('student').insert(student).execute()

ids = {r['name']:r['id'] for r in db.table('student').select('id,name').execute().data}

enrollments = [

    {"student_id":ids["Ali Hassan"], "course": "RDBMS", "grade":"A"},
    {"student_id":ids["Ali Hassan"], "course":"Networks", "grade" : "B"},
    {"student_id":ids["Siti Aishah"], "course": "RDBMS", "grade": "B"}, 
    {"student_id":ids["Raj Kumar"], "course": "RDBMS","grade":"C"},
    {"student_id":ids["Lin wel"], "course": "Networks", "grade":"A"}, 
]

db.table('enrollments').insert(enrollments).execute()

#SELECT all

st.subheader('All Students')

st.dataframe (db.table('student').select('*').execute().data)

#WHERE high GPA

st. subheader('GPA >= 3.5')

st.dataframe(db.table('student').select('name,gpa').gte('gpa',3.5).execute().data)


#JOIN via FK

st.subheader('RDBMS Enrollments (JOIN)')

st.dataframe (db.table('enrollments').select('grade, student (name)').eq('course', 'RDBMS').execute().data)

#UPDATE

db.table('student').update({'gpa':3.9}).eq('name', 'Ali Hassan').execute() 
st.write('Ali updated:', db.table('student').select('name,gpa').eq("name", 'Ali Hassan').execute().data)