from django.views.generic import View, CreateView
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'age', 'no_subjects', 'status', 'course_type')

class CourseList(View):
    def get(self, request):
        courses = list(Course.objects.all().values())
        data = dict()
        data['courses'] = courses
        return JsonResponse(data)

class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = dict()
        data['course'] = model_to_dict(course)
        return JsonResponse(data)

#@method_decorator(csrf_exempt(), name='dispatch')
class CourseCreate(CreateView):
    def post(self, request):
        data = dict()
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            data['course'] = model_to_dict(course)
        else:
            data['error'] = "form not valid!"
        return JsonResponse(data)

class CourseUpdate(View):
    def post(self, request, pk):
        data = dict()
        course = Course.objects.get(pk=pk)
        form = CourseForm(instance= course, data= request.POST)
        if form.is_valid():
            course = form.save()
            data['course'] = model_to_dict(course)
        else:
            data['error'] = "form not valid!"
        return JsonResponse(data)

class CourseDelete(View):
    def get(self, request, pk):
        data = dict()
        course = Course.objects.get(pk=pk)
        if course:
            course.delete()
            data['message'] = "course deleted!"
        else:
            data['message'] = "error"
        return JsonResponse(data)
