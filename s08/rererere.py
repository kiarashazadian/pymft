class rectangular():
    """
      >>> r = Rectangle(2, 5)
      >>> r.width, r.height, r.get_area(), r.get_perimeter()
      (2, 5, 10, 14,)
      >>> r.set_area(40)
      >>> r.width, r.height, r.get_area(), r.get_perimeter()
      (4, 10, 40, 28,)
      >>> r.set_perimeter(7)
      >>> r.width, r.height, r.get_area(), r.get_perimeter()
      (1, 2.5, 2.5, 7,)
      """

    def __init__(self, a, b):
        self.lenght = a




    def get_area(self):
        return 2 * (self.lenght + self.width)





    def get_masahat(self):
        return self.lenght * self.width


    def set_masahat(self, masahat_karbar):
        return ((masahat_karbar / self.masahat) / 2) * self.lenght * ((masahat_karbar / self.masahat) / 2) * self.width


obj_1 = rectangular(2, 5)

res_2 = obj_1.get_masahat()
res_3 = obj_1.set_masahat(40)

print(res_2)
print(res_3)
