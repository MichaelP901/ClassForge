from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.

@login_required(login_url='Login:login_view')
def grades(request): # loads the Grade page with all the users classes
    user_class_attributes = ClassAttributes.objects.filter(user=request.user)
    return render(request, "Grades/grades.html", {
        "class_attributes": user_class_attributes,
    })

@login_required(login_url='Login:login_view')
def classAdd(request): # adds user generated class
    if request.method == "POST":
        #retrieve all the input data
        class_name = request.POST.get("class-name")
        class_id = request.POST.get("class-Id")
        class_requirement = request.POST.get("class-requirement")

        #Gets the users classes
        user_class_attributes = ClassAttributes.objects.filter(user=request.user)

        if ClassAttributes.objects.filter(class_name=class_name).exists() == True:
            messages.error(request, "Class already added")
            return redirect("Grades:grades")
        else:
            if len(user_class_attributes) > 7:
                messages.error(request, "Class size maxed")
                return redirect("Grades:grades")
            else:
                attributes = ClassAttributes.objects.create(
                    user= request.user,
                    class_name=class_name, 
                    course_number=class_id, 
                    requirement=class_requirement,
                    class_grade = None,
                    )
                attributes.save()
                
                messages.success(request, "Class added successfully")
                return redirect("Grades:grades")
    else:
        messages.success(request, "Invalid request method")
        return redirect("Grades:grades")
    
@login_required(login_url='Login:login_view')
def classDelete(request):
    
    if request.method == "POST":
        attribute = ClassAttributes.objects.filter(user=request.user)

        for i, class_attr in enumerate(attribute):
            if request.POST.get(f"class-name-{i}"): # checks if a checkbox is on
                class_attr.delete()
        
    messages.success(request, "Class deleted sucessfully")
    return redirect('Grades:grades')

@login_required(login_url='Login:login_view')
def getAssignments(request, course_number):
    if request.method == "GET":
        user_class_attributes = ClassAttributes.objects.filter(user=request.user)
        user_assignments = Assignment.objects.filter(
            class_attributes__in=user_class_attributes, 
            class_attributes__course_number=course_number
            )
        

        return render(request, "Grades/grades.html", {
            "class_attributes": user_class_attributes,
            "assignments": user_assignments,
            "course": course_number,
        })

@login_required(login_url='Login:login_view')
def assignmentAdd(request):
    if request.method == "POST":
        assignment_name = request.POST.get("assignment-name")
        assignment_descrption = request.POST.get("assignment-description")
        assignment_due_date = request.POST.get("assignment-due-date")
        input_course_number = request.POST.get("course-number")
        

        if Assignment.objects.filter(name=assignment_name).exists():
            messages.error(request, "Assignment already added")
            return redirect("Grades:grades")
        else:

            if input_course_number == None or input_course_number == "":
                messages.error(request, "Something went wrong")
                return redirect("Grades:grades")

            user_class_attributes = ClassAttributes.objects.get(
                user=request.user, 
                course_number=input_course_number
                )
            
            user_assignments = Assignment.objects.filter(
                class_attributes__user=request.user,
                class_attributes__course_number=user_class_attributes.course_number
                )
            
            assignment = Assignment.objects.create(
                class_attributes = user_class_attributes,
                name=assignment_name,
                description=assignment_descrption, 
                due_date=assignment_due_date,
                assignment_grade = None
                )
            
            assignment.save()
            
            user_class_attributes = ClassAttributes.objects.filter(
                user=request.user,
                )

            return render(request, "Grades/grades.html", {
                "class_attributes": user_class_attributes,
                "assignments": user_assignments,
            })
                
    else:
        messages.success(request, "Invalid request method")
        return redirect("Grades:grades")

@login_required(login_url='Login:login_view')
def assignmentDelete(request):
    if request.method == "POST":
        input_course_number = request.POST.get("course-number")
        
        user_assignment = Assignment.objects.filter(
            class_attributes__user = request.user,
            class_attributes__course_number = input_course_number,
        )

        for i, class_attr in enumerate(user_assignment):
            print(f"\n\n\n\nassignment-name-{i}\n\n\n")
            if request.POST.get(f"assignment-name-{i}"):
                # print(request.POST.get(f"assignment-name-{i}"))

                assignmentDelete = user_assignment = Assignment.objects.filter(
                    class_attributes__user = request.user,
                    class_attributes__course_number = input_course_number,
                    name = request.POST.get(f"assignment-name-{i}"),
                )
                assignmentDelete.delete()
                messages.success(request, "Assignment deleted sucessfully")
    return redirect('Grades:grades')
        


