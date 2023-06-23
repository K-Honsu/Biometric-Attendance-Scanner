from django.db.models import TextChoices


class Gender(TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class Grade(TextChoices):
    GRADE1 = 'grade1'
    GRADE2 = 'grade2'
    GRADE3 = 'grade3'
    GRADE4 = 'grade4'
    # GRADE5 = 'grade5'
    # GRADE6 = 'grade6'


class Subject(TextChoices):
    MATHEMATICS = 'mathematics'
    ENGLISH = 'english'
    COMPUTER_SCIENCE = 'computer science'
    BUSINESS_STUDIES = 'business studies'
    PHYSICS = 'physics'
    CHEMISTRY = 'chemistry'
    BIOLOGY = 'biology'
    ARTS = 'arts'
    COMMERCIAL = 'commercial'


class Attendance(TextChoices):
    ABSENT = 'absent'
    PRESENT = 'present'
