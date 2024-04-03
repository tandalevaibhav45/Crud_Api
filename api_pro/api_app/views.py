from django.shortcuts import render
from .admin import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .serializers import StudentSerializers
import io
# Create your views here.


"""Run the myapp.py file on cmd  using python myapp.py """
@csrf_exempt
def student_api(request):
    if request.method == 'GET':   #use for to retrive the records from the database
        pk = request.GET.get('id')
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
                serializer = StudentSerializers(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type="application/json")
            except Student.DoesNotExist:
                return HttpResponse("Student not found", status=404)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializers(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
    
    if request.method == 'POST':   #use for insert the rocord in data
        try:
            json_data = json.loads(request.body)

            serializer = StudentSerializers(data=json_data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse("Data created")
            return HttpResponse("daa not created")
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
    
    if request.method == 'PUT':     #use for to updated the records
        print(request.body)
        json_data = json.loads(request.body)
        id = json_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu, data=json_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Data updated")
        
    if request.method == 'DELETE':     #use for to updated the records
        print(request.body)
        json_data = json.loads(request.body)
        id = json_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return HttpResponse("Data deleted")

