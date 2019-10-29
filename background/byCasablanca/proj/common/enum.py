from enum import Enum,unique

@unique
class ProductType(Enum):
    '''
        预报产品种类
    '''

    '''
        海浪
    '''
    WAVE=0
    '''
        海流
    '''
    CURRENT=1
    '''
        海冰
    '''
    ICE=2
    '''
        海表面温度
    '''
    SST=3
    '''
        海表面高度
    '''
    SSH=4

@unique

class Area(Enum):
    '''
        预报区域枚举
    '''

    '''
        中国海
    '''
    CHINASEA=0
    '''
        西北太
    '''
    NORTHWEST=1
    '''
        东海
    '''
    EASTCHINASEA=2
    '''
        深远海
    '''
    FAREAST=3
