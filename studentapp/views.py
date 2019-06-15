from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .api.serializers import studentSerializer
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from .forms import StudentForm


def homepage(request):
    return render(request, 'index.html')


class Get_students_List(APIView):

    def get(self, request):
        students = Students.objects.all()
        serialized = studentSerializer(students, many=True)
        return Response(serialized.data)


class Delete_students_List(APIView):
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = studentSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        if self.request.is_ajax():
            snippet = self.get_object(pk)
            snippet.delete()
            data = {'message': "Successfully submitted form data."}
            return JsonResponse(data)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class StudentCreate(APIView):
#     renderer_classes = [StudentForm]

#     def get(self, request, format=None):
#         snippets = Students.objects.all()
#         serializer = studentSerializer(snippets, many=True)
#         return Response({'serializer': serializer})

#     def post(self, request, format=None):
#         serializer = studentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
