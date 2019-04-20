from django.db import models


class Account(models.Model):
    id = models.CharField(verbose_name='账号ID', primary_key=True, max_length=15)
    name = models.CharField(verbose_name='姓名', max_length=10)
    password = models.CharField(verbose_name='密码', max_length=30)
    available = models.BooleanField(verbose_name='用户状态', null=True, blank=True)

    def __str__(self):
        return str(self.id) + '-' + str(self.name)

    class Meta:
        verbose_name = '账号'
        verbose_name_plural = '账号列表'


class User_Manager(models.Manager):
    pass


class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name_used_before = models.CharField(verbose_name='曾用名', max_length=10, null=True, blank=True)
    sex = models.IntegerField(verbose_name='性别', choices=((0, '男'), (1, '女')))
    birthday = models.DateField(verbose_name='出生日期', null=True, blank=True)
    from User.nation_choices import nation_choices
    nation = models.CharField(verbose_name='民族', max_length=8, null=True, blank=True, choices=nation_choices)
    from User.political_choices import political_choices
    political = models.IntegerField(verbose_name='政治面貌', choices=political_choices, null=True, blank=True)
    religious_belief = models.CharField(verbose_name='宗教信仰', max_length=10, null=True, blank=True)
    native_place = models.CharField(verbose_name='籍贯', max_length=5, null=True, blank=True)
    id_number = models.CharField(verbose_name='身份证号', max_length=20, null=True, blank=True)
    mobile_phone = models.CharField(verbose_name='手机', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='电子邮箱', null=True, blank=True)
    qq = models.CharField(verbose_name='QQ', max_length=20, null=True, blank=True)
    from User.country_and_region_choices import country_and_region_choices
    country_and_region = models.CharField(verbose_name='国家或地区', max_length=3, choices=country_and_region_choices, default='CN')
    creator = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='用户创建者', null=True, blank=True)
    personal_page = models.CharField(verbose_name='个人主页', max_length=50, null=True, blank=True)
    marriage = models.BooleanField(verbose_name='婚否', null=True, blank=True)
    objects = User_Manager()

    def __str__(self):
        return str(self.account)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'


class Faculty(models.Model):
    name = models.CharField(verbose_name='系/所/中心', primary_key=True, max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '系'
        verbose_name_plural = '系列表'


class Teacher_Manager(models.Manager):
    pass


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, verbose_name='系', on_delete=models.CASCADE)
    masters_supervisor = models.BooleanField(verbose_name='硕士生导师', null=True, blank=True)
    doctoral_supervisor = models.BooleanField(verbose_name='博士生导师', null=True, blank=True)
    home_phone = models.CharField(verbose_name='家庭电话', max_length=20, null=True, blank=True)
    office_phone = models.CharField(verbose_name='办公电话', max_length=20, null=True, blank=True)
    personal_profile = models.TextField(verbose_name='个人简介', null=True, blank=True, max_length=1000)
    objects = Teacher_Manager()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师列表'


class Student_Grade(models.Model):
    name = models.CharField(verbose_name='年级名称', max_length=10, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '年级'
        verbose_name_plural = '年级列表'


class Major(models.Model):
    colledge_code = models.CharField(verbose_name='校编专业代码', max_length=20, primary_key=True)
    national_code = models.CharField(verbose_name='国编专业代码', max_length=20)
    name = models.CharField(verbose_name='专业名称', max_length=10)
    faculty = models.ForeignKey(Faculty, verbose_name='系', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业列表'


class Campus(models.Model):
    name = models.CharField(verbose_name='校区名称', max_length=10, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '校区'
        verbose_name_plural = '校区列表'


class Student_Class(models.Model):
    grade = models.ForeignKey(Student_Grade, verbose_name='年级', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, verbose_name='专业', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='班级名称', max_length=10)
    instructor = models.ForeignKey(Teacher, verbose_name='辅导员', on_delete=models.CASCADE, related_name='instructor_teacher')
    headmaster = models.ForeignKey(Teacher, verbose_name='班导师', on_delete=models.CASCADE, related_name='headmaster_teacher')
    campus = models.ForeignKey(Campus, verbose_name='校区', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grade) + '-' + str(self.major) + '-' + str(self.name)

    class Meta:
        unique_together = ('grade', 'major', 'name')
        verbose_name = '班级'
        verbose_name_plural = '班级列表'


class Student_Manager(models.Manager):
    pass


class Student_Category(models.Model):
    name = models.CharField(verbose_name='学生类别', max_length=30, primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '学生类别'
        verbose_name_plural = '学生类别列表'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Student_Class, verbose_name='班级', on_delete=models.CASCADE)
    student_category = models.ForeignKey(Student_Category, verbose_name='学生类别', on_delete=models.CASCADE)
    objects = Student_Manager()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生列表'


class Undergraduate_Manager(models.Manager):
    pass


class Undergraduate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    objects = Undergraduate_Manager()

    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name = '本科生'
        verbose_name_plural = '本科生列表'


class Graduate_Manager(models.Manager):
    pass


class Graduate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Teacher, verbose_name='导师', on_delete=models.CASCADE)
    objects = Graduate_Manager()

    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name = '研究生'
        verbose_name_plural = '研究生列表'
