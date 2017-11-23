#! usr/bin/python3

# Auther:Mr_Yellow
# Data 2017_11_23



		
# class Myclass :
# 	"""a simple example"""
# 	i = 12345
# 	def f(self):
# 		return 'heihei'

# #实例化
# x = Myclass()

# 访问类的属性和方法
# print (x)
# print (x.i)
# print (x.f())




# class complex:
# 	def __init__(self,a,b):
# 		self.a = a
# 		self.b = b
# x = complex(3,4)
# print(x.a,x.b)
# print(dir(complex))
# print(complex.__eq__)




# class say_age(object):
# 	"""docstring for say_age"""
# 	def __init__(self, name,age):
# 		self.name = name
# 		self.age = age
# 	def speak(self):
# 		print("%s say:I am %d years old."%(self.name,self.age) )
# p = say_age('gj',20)
# p.speak()



# class People(object):
# 	"""docstring for People"""
# 	name = ''
# 	age = 0
# 	__weight = 0
# 	def __init__(self, name , age, weight):
# 		self.name = name
# 		self.age = age
# 		self.__weight = weight
# 	def speak(self):
# 		print("%s say: I am %d years old。" %(self.name,self.age))	
# #单继承
# class Student(People):
# 		"""docstring for Student"""
# 		grade = ''
# 		def __init__(self, name,age,weight ,grade):
# 			super(Student, self).__init__(name,age,weight)
# 			self.grade = grade
# 		#重写父类的方法
# 		def speak(self):
# 			print ("%s say :I am %d years old and am in grade %s"%(self.name,self.age,self.grade))
				
# s = Student('lou',24,60,3)
# s.speak()

# class Speaker(object):
# 	"""docstring for Speaker"""
# 	topic = ''
# 	name = ''
# 	def __init__(self, name ,topic):
# 		self.name = name
# 		self.topic = topic
# 	def speak(self):
# 		print("I am %s ,I am a speaker,this is \"%s\""%(self.name, self.topic))
# #多重继承
# class Sample(Speaker,Student):
# 	"""docstring for Sample"""
# 	weight = 0
# 	def __init__(self, name ,age ,weight ,grade ,topic):
# 		Student.__init__(self, name,age,weight,grade)
# 		Speaker.__init__(self, name ,topic)

# lou = Sample('lou', 22,60,3,'I am a zhizhang')
# lou.speak()
		



#方法重写，在子类里面覆盖父类的方法即可
# class Parent:
# 	def myMethod (self):
# 		print ("调用父类方法")
# class Child(Parent):	
# 	def myMethod(self):
# 		print("调用子类方法")	

# zilei = Child()
# zilei.myMethod()




#类的私有属性
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
 
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print (self.__secretCount,self.publicCount)

# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# #print(counter.__secretCount)#不能通过属性访问，但是可以加类名访问
# print(counter._JustCounter__secretCount)




#类的专有方法，即magic method


#运算符重载
class Vector:
    def __init__(self,a,b):
	self.a = a
	self.b = b
    def __str__(self):
	return ("Vector (%d,%d)"%(self.a,self.b))
    def __add__(self,other):
	return Vector(self.a + other.a, self.b + other.b)

v1 = Vector (2,10)
v2 = Vector (5,-2)

print (v1 + v2)

#http://www.runoob.com/python3/python3-class.html

#很多的梦在等待着进行201711231209





