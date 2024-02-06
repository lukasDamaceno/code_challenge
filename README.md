# Code Challenge for Inclusion Cloud

## How to use
Just run the following command and you will get the test results for all the questions made in the document sent by me
```shell
> pip install -r requirements.txt
> pytest -q tests/test_base.py --capture=sys -vvv
```
Example output
```shell
> pytest -q tests/test_base.py --capture=sys -vvv
==================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0 -- /home/lukinha/code_challenge/.env/bin/python3
cachedir: .pytest_cache
rootdir: /home/lukinha/code_challenge
collected 11 items                                                                           

tests/test_base.py::TestQuestionOne::test_has_three_properties_initialized_at_construction PASSED [  9%]
tests/test_base.py::TestQuestionOne::test_has_1_empty_class_method PASSED              [ 18%]
tests/test_base.py::TestQuestionOne::test_has_1_empty_instance_method PASSED           [ 27%]
tests/test_base.py::TestQuestionTwo::test_is_derived_from_class_a PASSED               [ 36%]
tests/test_base.py::TestQuestionTwo::test_is_class_b_properties_different_to_class_a PASSED [ 45%]
tests/test_base.py::TestQuestionTwo::test_is_there_code_in_methods PASSED              [ 54%]
tests/test_base.py::TestQuestionThree::test_get_even PASSED                            [ 63%]
tests/test_base.py::TestQuestionFour::test_get_x_eq_five PASSED                        [ 72%]
tests/test_base.py::TestQuestionFour::test_no_x_eq_five PASSED                         [ 81%]
tests/test_base.py::TestQuestionFive::test_printed_messages PASSED                     [ 90%]
tests/test_base.py::TestQuestionFive::test_if_datetimes_are_iso_dates PASSED           [100%]

===================================== 11 passed in 0.02s =====================================
```