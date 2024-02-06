import inspect
import json
from pathlib import Path

from src.main import A, B, get_even, get_x_eq_five, change_date_format_and_save


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
        # note: had to implement this because inspect has no predicate compatible
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


class TestQuestionTwo:
    b = B()

    def test_is_derived_from_class_a(self):
        assert isinstance(self.b, A)

    def test_is_class_b_properties_different_to_class_a(self):
        b_properties = self.b.a1, self.b.a2, self.b.a3
        a = A()
        a_properties = a.a1, a.a2, a.a3
        assert b_properties != a_properties

    def test_is_there_code_in_methods(self):
        results = self.b.my_instance_method(7), B.my_class_method()
        assert all(results)


class TestQuestionThree:
    @staticmethod
    def test_get_even():
        int_list = list(range(1, 9))
        expected = [2, 4, 6, 8]
        result = get_even(int_list)
        assert expected == result

class TestQuestionFour:
    @staticmethod
    def test_get_x_eq_five():
        dict_list = [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'x': 5}]
        expected = {'x': 5}
        result = get_x_eq_five(dict_list)
        assert result == expected

    @staticmethod
    def test_no_x_eq_five():
        dict_list = [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'e': 5}]
        expected = {}
        result = get_x_eq_five(dict_list)
        assert result == expected

class TestQuestionFive:
    @staticmethod
    def test_printed_messages(capsys):
        sample_file_location = Path('sample.json')
        dest_file_location = Path('test.json')
        expected = 'payee.id = 9999', 'invoiceIds = XXA15839, XXA35832, XXA45830, XXA55831, XXA65833, XXA75834'
        change_date_format_and_save(sample_file_location, save_dest=dest_file_location)
        captured = capsys.readouterr()
        result = tuple(filter(bool, captured.out.split('\n')))
        assert result == expected

    @staticmethod
    def test_if_datetimes_are_iso_dates():
        sample_file_location = Path('sample.json')
        dest_file_location = Path('test.json')
        expected = (
            '2021-10-21T20:50:44',
            '2021-10-21T20:50:44',
            '2021-10-22T14:04:35'
        )
        change_date_format_and_save(sample_file_location, save_dest=dest_file_location)
        with open(dest_file_location, 'r', encoding='utf-8') as dest_file:
            parsed_file = json.load(dest_file)
            result = (
                parsed_file.get('claimDateTime'),
                parsed_file.get('fileDateTime'),
                parsed_file.get('receivedDateTime')
            )
            dest_file.close()
        assert result == expected

