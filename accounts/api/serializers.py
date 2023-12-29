from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from accounts.models import Student, Judge


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = (
            "first_name",
            "middle_name",
            "surname",
            "email",
            "phone",
            "birth_date",
            "gender",
            "state",
            "school",
        )



class StudentRegisterSerializer(serializers.ModelSerializer):
    middle_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    surname = serializers.CharField(max_length=100, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=20, required=True)

    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['password1', 'password2', 'email', 'first_name', 'middle_name', 'surname', 'phone']
        
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password1': 'Password fields did not match..!'})
        if User.objects.filter(username=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return attrs            

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password1'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['surname']
        )

        student = Student.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            surname=validated_data['surname'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            )
        return student



class JudgeRegisterSerializer(serializers.ModelSerializer):
    middle_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    surname = serializers.CharField(max_length=100, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=20, required=True)

    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['password1', 'password2', 'email', 'first_name', 'middle_name', 'surname', 'phone']
        
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password1': 'Password fields did not match..!'})
        if User.objects.filter(username=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return attrs            

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password1'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['surname']
        )

        judge = Judge.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            surname=validated_data['surname'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            )
        return judge


