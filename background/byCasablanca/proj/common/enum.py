from enum import Enum,unique

@unique
class ProductType(Enum):
    '''
        预报产品种类
    '''

    '''
        海浪
    '''
    WAVE=1
    '''
        海流
    '''
    CURRENT=2
    '''
        海冰
    '''
    # todo:[*] 19-12-12 注意所有海冰相关的暂时注释掉
    # ICE=3
    '''
        海表面温度
    '''
    SST=4
    '''
        海表面高度
    '''
    SSH=5

@unique

class Area(Enum):
    '''
        预报区域枚举
    '''

    '''
        中国海
    '''
    CHINASEA=1
    '''
        西北太
    '''
    NORTHWEST=2
    '''
        东海
    '''
    EASTCHINASEA=3
    '''
        深远海
    '''
    FAREAST=4
    '''
        渤海
    '''
    BOHAI=5
