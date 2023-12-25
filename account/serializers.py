from rest_framework import serializers
from account.models import Student, Judge


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = ('first_name', 'middle_name', 'surname', 'email', 'phone')