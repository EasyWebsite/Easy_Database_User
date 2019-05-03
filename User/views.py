from User.models import *
from ServiceUtils.ServiceModel import HttpServiceModel


class AccountService(HttpServiceModel):
    __dependence__ = Account


class UserService(HttpServiceModel):
    __dependence__ = User


class FacultyService(HttpServiceModel):
    __dependence__ = Faculty


class TeacherService(HttpServiceModel):
    __dependence__ = Teacher


class StudentGradeService(HttpServiceModel):
    __dependence__ = Student_Grade


class MajorService(HttpServiceModel):
    __dependence__ = Major


class CampusService(HttpServiceModel):
    __dependence__ = Campus


class StudentClassService(HttpServiceModel):
    __dependence__ = Student_Class


class StudentCategoryService(HttpServiceModel):
    __dependence__ = Student_Category


class StudentService(HttpServiceModel):
    __dependence__ = Student


class UndergraduateService(HttpServiceModel):
    __dependence__ = Undergraduate


class GraduateService(HttpServiceModel):
    __dependence__ = Postgraduate
