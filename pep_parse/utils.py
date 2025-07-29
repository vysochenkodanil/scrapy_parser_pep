from datetime import datetime

def uri_params(params, spider):
    return {'time': datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}