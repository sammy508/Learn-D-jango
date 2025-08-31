from django.contrib import admin
from .models.course_model import CourseModel
from .models.student_models import StudentModel
from .models.Teacher_table import TeacherModel
from .models.user_models import UserModel



# Register your models here.

admin.site.register(CourseModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(UserModel)