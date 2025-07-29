from datetime import datetime

def uri_params(params, spider):
    return {'time': datetime.now().strftime('%Y%m%d_%H%M%S')}