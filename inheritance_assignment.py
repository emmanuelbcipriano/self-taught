# class Shape():
#     def __init__(self):
#         pass

#     def what_am_i(self):
#         print('I am a shape')

# class Square(Shape):
#     pass

# class Rectangle(Shape):
#     pass

# sq = Square()
# sq.what_am_i()

# rec = Rectangle()
# sq.what_am_i()

##EXERCISE
# class Square():
#     square_list = []
    
#     def __init__(self, s):
#         self.s1 = s
#         self.square_list.append((self.s1))
    
# sq = Square(3)
# sq1 = Square(4)
# print(sq.square_list)


##OOPEX2##
# class Square():
#     def __init__(self,s):
#         self.s1 = s
    
#     def __repr__(self):
#         return '{} by {} by {} by {}'.format(str(self.s1))
#     #     # return '{} by {} by {} by {}'.format(self.s1)
        
# sq = Square(3)
# print(sq)

##OOPEX3##
# class Square:
#     def __init__(self):
#         self.name = 'Square'
 
# def same(a, b):
#     return a is b