import yaml, os

def get_lab_data():
    yaml_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'lab/yaml/lab_data.yaml'))
    yaml_data = open(yaml_path, 'r')
    return yaml.load(yaml_data, Loader=yaml.FullLoader)

