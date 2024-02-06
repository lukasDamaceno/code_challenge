class A():
    def __init__(self, a1=1, a2=2, a3=3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    @classmethod
    def my_class_method(cls):
        pass

    def my_instance_method(self):
        pass


class B(A):
    def __init__(self, a1=4, a2=5, a3=6):
        super().__init__(a1, a2, a3)

    @classmethod
    def my_class_method(cls):
        return dir(cls())

    # pylint: disable=arguments-differ
    def my_instance_method(self, a3):
        self.a3 = a3
        return a3


def get_even(int_list: list):
    return [n for n in int_list if n % 2 == 0]

def get_x_eq_five(dict_list: list):
    dict_iter = iter(dict_list)
    x = None
    try:
        while x := next(dict_iter):
            if not isinstance(x.get('x'), int):
                continue
            return x
    except StopIteration:
        return {}
