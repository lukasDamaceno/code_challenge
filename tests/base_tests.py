import inspect

from . import A


class QuestionOneTests:
    a = A(a1=1, a2=2, a3=3)

    def has_three_properties_initialized_at_construction(self):
        expected = 3
        result = len(vars(self.a))
        assert expected == result

    def has_1_empty_class_method(self):
        expected = 1, None
        result = (len(inspect.getmembers(self.a, predicate=inspect.isclass)), self.a.my_class_method())
        assert expected == result
    
    def has_1_empty_instance_method(self):
        expected = 1, None
        result = (len(inspect.getmembers(self.a, predicate=inspect.ismethod)), self.a.my_class_method())
        assert expected == result