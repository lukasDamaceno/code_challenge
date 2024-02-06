import json
from datetime import datetime
from pathlib import Path

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
        pass
    return {}

def change_date_format_and_save(json_file_location, save_dest = Path('../result.json')):
    with open(json_file_location, 'r', encoding='utf-8') as source_file:
        parsed_json_file = json.load(source_file)
        source_file.close()
    payee_id = parsed_json_file['payee']['id']
    invoice_ids = parsed_json_file['invoiceIds']
    print(f'payee.id = {payee_id}')
    print(f'invoiceIds = {", ".join(_id for _id in invoice_ids if "583" in _id)}')
    timestamp_attrs = 'claimDateTime', 'fileDateTime', 'receivedDateTime'
    for attr in timestamp_attrs:
        try:
            datetime_obj = datetime.fromtimestamp(parsed_json_file[attr]/1e3)
            parsed_json_file[attr] = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S')
        except KeyError:
            continue
    with open(save_dest, 'w', encoding='utf-8') as dest_file:
        dest_file.write(json.dumps(parsed_json_file))
        dest_file.close()
