import inspect

from src.main import A


class TestQuestionOne:
    a = A()

    def test_has_three_properties_initialized_at_construction(self):
        expected = 3
        result = len(vars(self.a))
        assert expected == result

    def test_has_1_empty_class_method(self):
        expected = 1, None
        class_methods = inspect.getmembers(self.a, predicate=inspect.isclass)
        result = len(class_methods), self.a.my_class_method()
        assert expected == result
    
    def test_has_1_empty_instance_method(self):
        # had to implement this because inspect has no predicate compatible
        instance_methods = []
        for name, member in inspect.getmembers(self.a, predicate=inspect.ismethod):
            if name == '__init__':
                continue
            parameters = member.__code__.co_varnames
            print(parameters)
            if 'self' in parameters:
                instance_methods.append(name)

        expected = 1, None
        result = len(instance_methods), self.a.my_instance_method()
        assert expected == result