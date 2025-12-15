from .student import Student
from .course import Course
from .mark_manager import MarkManager  


# 3 cái này chỉ giúp cho hàm main gọn hơn bằng cách gọi: from domains import Student, Course, MarkManager
# chứ thật ra file này để trống cũng được =>
# => khi đó hàm main phải gọi : from domains.student import Student