import json


def load_data(filepath):
    with open(filepath, 'r') as raw_content:
        data = json.load(raw_content)
    return data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    data = load_data('Alco_drinks.json')
    pretty_print_json(data)
