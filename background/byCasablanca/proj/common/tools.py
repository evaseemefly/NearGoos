import os


def check_path_exist(self, local_path: str):
    '''
        检查本地指定路径是否存在
    :param local_path:
    :return:
    '''
    if not os.path.exists(local_path):
        os.makedirs(local_path)
