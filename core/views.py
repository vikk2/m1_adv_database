from django.shortcuts import render
from .db import students_col, courses_col
from bson import ObjectId


def create_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        students_col.insert_one({
            "name": name,
            "email": email
        })

    return render(request, "student_form.html")


def create_course(request):
    if request.method == "POST":
        title = request.POST.get("title")
        student_ids = request.POST.getlist("students")

        students = list(
            students_col.find({
                "_id": {"$in": [ObjectId(sid) for sid in student_ids]}
            })
        )

        embedded_students = [
            {"_id": s["_id"], "name": s["name"]}
            for s in students
        ]

        courses_col.insert_one({
            "title": title,
            "students": embedded_students
        })

    all_students = [
    {
        "id": str(s["_id"]),   # rename _id → id
        "name": s["name"]
    }
    for s in students_col.find()
]

    return render(request, "course_form.html", {
        "students": all_students
    })


def course_report(request, id):
    from bson import ObjectId

    course = courses_col.find_one({"_id": ObjectId(id)})

    # transform course data
    course_data = {
        "id": str(course["_id"]),
        "title": course["title"]
    }

    # transform students
    students = [
        {
            "id": str(s["_id"]),
            "name": s["name"]
        }
        for s in course.get("students", [])
    ]

    return render(request, "report.html", {
        "course": course_data,
        "students": students
    })

def course_list(request):
    courses = [
        {
            "id": str(c["_id"]),
            "title": c["title"]
        }
        for c in courses_col.find()
    ]

    return render(request, "course_list.html", {
        "courses": courses
    })