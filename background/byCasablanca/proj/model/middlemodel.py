from common.enum import Area, ProductType


class AreaNameMidModel():
    '''
        区域与对应的名称re的 middle model
    '''

    def __init__(self, area: Area, re: str):
        self.area = area
        self.re = re


class ProductMidModel():
    '''
        产品与区域以及对应的名称re 的中间model
        todo:[*] 19-10-29 存储路径放置此处
    '''

    def __init__(self, type: ProductType, areanames: [], root: str):
        self.producttype = type
        self.areanames = areanames
        self.root = root
