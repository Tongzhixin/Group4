from User_Profile.models import Student, User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

from .forms import CourseForm
from .models import CourseDetail


# Create your views here.
# 首页导航
def index(request):
    if request.user.is_authenticated:
        #user = User.objects.get(id=id)
        Course = CourseDetail.objects.all()
        #Course = Courseall.filter(state_match=0)
        if request.method == 'GET':
            gender_choice = request.GET.get("gender", '')
            subject_choice = request.GET.get("subject", '')
            grade_choice = request.GET.get("grade", '')
            if gender_choice == "9" or gender_choice == '':
                if subject_choice == "0" or subject_choice == '':
                    if grade_choice == "0" or grade_choice == '':
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(state_match=0)
                    else:
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(grade_course=grade_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(grade_course=grade_choice).filter(state_match=0)
                else:
                    if grade_choice == "0":
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(subject=subject_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(subject=subject_choice).filter(state_match=0)
                    else:
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
            else:
                if subject_choice == "0":
                    if grade_choice == "0":
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(state_match=0)
                        else:
                            Course_show = Course
                    else:
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(grade_course=grade_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(grade_course=grade_choice).filter(state_match=0)
                else:
                    if grade_choice == "0":
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(subject=subject_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(state_match=0)
                    else:
                        if request.GET.get("charge", '') == "1":
                            Course_show = Course.objects.filter(charge__lte=30).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "2":
                            Course_show = Course.objects.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "3":
                            Course_show = Course.objects.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "4":
                            Course_show = Course.objects.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        elif request.GET.get("charge", '') == "5":
                            Course_show = Course.objects.filter(charge__gt=100).filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)
                        else:
                            Course_show = Course.objects.filter(grade_course=grade_choice).filter(subject=subject_choice).filter(state_match=0)

            context = {'course': Course_show}
            return render(request, 'filter.html', context)
        else:
            return HttpResponse("请使用GET请求数据")
    else:
        return render(request, 'index.html')


@login_required(login_url='/user/login/')
def filter(request, id):
    return render(request, 'filter.html')


# 增加课程
@login_required(login_url='/user/login/')
def increase_course(request):
    user = User.objects.get(id=request.user.id)
    if user.is_teacher == True:
        if request.method == "POST":
            if request.user != user:
                return HttpResponse("你没有权限修改此用户信息。")

            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                new_course = course_form.save(commit=False)
                # 还要存一些表单给不了的数据
                new_course.teacher = user
                new_course.state_match = False
                new_course.save()
                return redirect("Course:increase_course")

        elif request.method == "GET":
            course_form = CourseForm()
            context = {'form': course_form}
            return render(request, 'Course/increase_course.html', context)
        else:
            return HttpResponse("请使用GET或POST请求数据")
    else:
        return HttpResponse("只有老师才能开设新课程哦")


# 课程申请匹配
def match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    applicant = User.objects.get(id=request.user.id)
    # 虽然这里有判断，但还是尽量在前端控制只有学生浏览课程详情页面时才有“申请”的按钮
    if applicant.is_student == True:
        # 多对多中间表加一个元组
        course_applying.student_applied.add(applicant)
        course_applying.save()
        return redirect('Course: detail_course')
    else:
        return HttpResponse("只有学生可以申请选课")
    return redirect('Course: detail_course')


# 同意申请
def agree_match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    selected_student = Student.objects.get(id=request.POST['choice'])
    course_applying.student_agreed = selected_student
    course_applying.state_match = True
    course_applying.save()
    return redirect('Course: manage_course')


# 课程详细内容
def detail_course(request, coursedetail_id):
    course = CourseDetail.objects.get(id=coursedetail_id)
    context = {'course': course, 'coursedetail_id': coursedetail_id}
    return render(request, 'Course/detail.html', context)


# 课程管理
def manage_course(request):
    ID = request.user.id
    user = User.objects.get(id=ID)
    # context = {}
    if user.is_teacher:

        course_match = user.teacher_profile.coursedetail_set.filter(state_match=True)
        # course_match = CourseDetail.objects.filter(teacher_id=id, state_match=True)
        # course_unmatched = CourseDetail.objects.filter(teacher__id=id, state_match=False)
        course_unmatched = user.teacher_profile.coursedetail_set.filter(state_match=False)
        course_list = {}
        for course in course_unmatched:
            if course.student_applied.all():
                course_list[course] = course.student_applied.all()
        context = {'course_match': course_match, 'course_unmatched': course_unmatched,
                   'course_list': course_list}
        return render(request, 'Course/teacher_subject_detail.html', context)
    if user.is_student:
        course_match = user.student_profile.agreed_Student.filter(state_match=True)
        course_applying = user.student_profile.applied_Student.all()
        context = {'course_match': course_match, 'course_applying': course_applying}

        return render(request, 'Course/student_subject_detail.html', context)

