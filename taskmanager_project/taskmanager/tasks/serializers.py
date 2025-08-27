# serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Task, TaskCategory, TaskUpdate, EducationalResource

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                 'role', 'phone_number', 'license_number', 'certification',
                 'experience_years')
        read_only_fields = ('id',)

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 
                 'last_name', 'role', 'phone_number', 'license_number', 
                 'certification', 'experience_years')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assigned_to', write_only=True, required=False
    )
    category = TaskCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TaskCategory.objects.all(), source='category', write_only=True, required=False
    )
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'created_by')

class TaskUpdateSerializer(serializers.ModelSerializer):
    updated_by = UserSerializer(read_only=True)
    
    class Meta:
        model = TaskUpdate
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_by')

class EducationalResourceSerializer(serializers.ModelSerializer):
    added_by = UserSerializer(read_only=True)
    
    class Meta:
        model = EducationalResource
        fields = '__all__'
        read_only_fields = ('id', 'added_at', 'added_by')