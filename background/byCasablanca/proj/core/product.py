import re
from abc import ABCMeta, abstractmethod
from common.dictcommon import DICT_COMMON


class ProductBase:
    file_name_common = ''
    file_ext = ''
    match_pattern = ''
    period_dict = DICT_COMMON['1']

    @abstractmethod
    def get_re(self):
        '''
            获取正则表达式
        :return:
        '''
        pass

    def get_interval_str(self, name: str):
        '''
            根据传入的 file name 获取 名称中包含的时间间隔信息
        :param name:
        :return:
        '''
        # re_pattern: str = self.get_re()
        # match_res = re.match(name, re_pattern)
        # return match_res.group()
        # 改为使用re.comile
        pattern = re.compile(self.get_re())
        matches = re.findall(pattern, name)
        if len(matches) > 0:
            return matches[0]
        return None

    def get_interval_index(self, name: str):
        '''
            根据interval str 获取对应的 index
            根据 interval_str从当前的period_dict中找到对应的index(periods->index)
        :return:
        '''
        index = self.period_dict['periods'].index(int(self.get_interval_str(name)))
        # 返回index对应的值
        return self.period_dict['index'][index]

    def get_re(self) -> str:
        # str_list = [self.file_name_common, self.match_pattern, self.file_ext]
        # re_pattern = ''.join(str_list)
        # return re_pattern
        return self.match_pattern


class Wavechinasea(ProductBase):
    file_name_common = 'coast'
    file_ext = '.png'
    match_pattern = r'\d{2,3}'


class Wavenorthwest(ProductBase):
    file_name_common = 'xb'
    file_ext = '.png'
    match_pattern = r'\d{2,3}'


class Currenteastchinasea(ProductBase):
    file_name_common = 'sped-top-'
    file_ext = '.jpg'
    match_pattern = r'\d{2,3}'

    period_dict = DICT_COMMON['2']


class Currentnorthwest(ProductBase):
    file_name_common = 'xb'
    file_ext = '.png'
    match_pattern = r'\d{2,3}'
    period_dict = DICT_COMMON['2']


class Currentfareast(ProductBase):
    file_name_common = 'cur_NMEFC_near_goos_'
    file_ext = 'Hr.png'
    match_pattern = r'\d{2,3}'
    period_dict = DICT_COMMON['3']

# class Icebohai(ProductBase):
#     file_name_common = 'cur_NMEFC_near_goos_'
#     file_ext = 'Hr.png'
#     match_pattern = r'\d{2,3}'

class Ssteastchinasea(ProductBase):
    file_name_common = 'temp-top-'
    file_ext = '.jpg'
    match_pattern = r'\d{2,3}'
    period_dict = DICT_COMMON['2']


class Sstnorthwest(ProductBase):
    file_name_common = 'temp-top-'
    file_ext = '.png'
    match_pattern = r'\d{2,3}'
    period_dict = DICT_COMMON['2']


class Sshfareast(ProductBase):
    file_name_common = 'ssh_NMEFC_near_goos_'
    file_ext = 'Hr.png'
    match_pattern = r'\d{2,3}'
    period_dict = DICT_COMMON['3']


class ProductFactory:
    '''
        product的工厂类，创建对应的product
    '''

    def create_product(self, type):
        '''
            根据type创建指定的class
        :param type:
        :return:
        '''
        target_class = type.capitalize()
        return globals()[target_class]
