import Easy_Database_User.urls
from User.models import *
from ServiceUtils.rpc import RPCServiceModel


class AccountService(RPCServiceModel):
    name = "Account"
    __dependence__ = Account


class UserService(RPCServiceModel):
    name = "User"
    __dependence__ = User


class FacultyService(RPCServiceModel):
    name = "Faculty"
    __dependence__ = Faculty


class TeacherService(RPCServiceModel):
    name = "Teacher"
    __dependence__ = Teacher


class StudentGradeService(RPCServiceModel):
    name = "Student_Grade"
    __dependence__ = Student_Grade


class MajorService(RPCServiceModel):
    name = "Major"
    __dependence__ = Major


class CampusService(RPCServiceModel):
    name = "Campus"
    __dependence__ = Campus


class StudentClassService(RPCServiceModel):
    name = "Student_Class"
    __dependence__ = Student_Class


class StudentCategoryService(RPCServiceModel):
    name = "Student_Category"
    __dependence__ = Student_Category


class StudentService(RPCServiceModel):
    name = "Student"
    __dependence__ = Student


class UndergraduateService(RPCServiceModel):
    name = "Undergraduate"
    __dependence__ = Undergraduate


class GraduateService(RPCServiceModel):
    name = "Graduate"
    __dependence__ = Graduate


if __name__ == '__main__':
    import os

    os.system("nameko run views")
