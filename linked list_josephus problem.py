#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Student:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None

    def remove(self, prefix, suffix):
        self.prev.next = self.next
        self.next.prev = self.prev
        print(prefix + str(self.id) + suffix)


class Circle:
    def __init__(self, num_students):
        #Create all students and make doubly linked list
        self.num_students = num_students
        self.head = None

        prev_student = None
        for i in range(self.num_students):
            curr_student = Student(id=i)

            if i == 0:
                self.head = curr_student
            elif i == self.num_students-1:
                curr_student.prev = prev_student
                prev_student.next = curr_student
                curr_student.next = self.head
                self.head.prev = curr_student
            else:
                curr_student.prev = prev_student
                prev_student.next = curr_student
            prev_student = curr_student
        self.curr_student = self.head        

    def advance(self, num_steps):
        for i in range(num_steps-1):
            self.curr_student = self.curr_student.next
        self.curr_student = self.curr_student.next
        self.curr_student.prev.remove(prefix='Student ', suffix=' is removed')

    def remove_all(self, num_steps):
        while self.curr_student != self.curr_student.next:
            self.advance(num_steps)
        print('Congratulations, student ' + str(self.curr_student.id) + '!')

n = int(input('Enter number n of students, at least 2: '))
k = int(input('Enter a number of students to skip, between 1 and n: '))
c = Circle(num_students=n)
c.remove_all(num_steps=k)


# In[ ]:




