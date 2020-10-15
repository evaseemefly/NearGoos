import axios from 'axios';
import { ProductImageCondition } from '@/middle_model/product.ts';
// 后端的请求地址及端口
//
// export const host = 'http://localhost:8083';
export const host = 'http://neargoos.nmefc.cn:8083';
axios.defaults.withCredentials = true;
axios.defaults.headers = {};
/**
 * 根据code以及date 读取指定时刻的散点
 *
 * @param {string} code
 * @returns
 */
const getAllArea = () => {
  const url = `${host}/product/area`;
  return axios.get(url, {
    params: {},
  });
};

const getAllTypesMenu = () => {
  const url = `${host}/product/menu/list`;
  return axios.get(url, {
    params: {},
  });
};

const getProductResByConCondition = (params: any) => {
  const url = `${host}/product/list`;
  return axios.get(url, {
    params: {
      cateogry: params.cateogry,
      area: params.area,
      period: params.period,
      start: params.start,
      end: params.end,
      brevity: params.brevity,
    },
  });
};

/**
 * 根据params获取今日的产品 image 对应的url地址
 *
 * @param {ProductImageCondition} params
 * @returns
 */
const getProductImageUrl = (params: ProductImageCondition) => {
  const url = `${host}/product/last`;
  return axios.get(url, {
    params: {
      cateogry: params.cateogry,
      area: params.area,
      period: params.period,
    },
  });
};

/**
 * 从数据库中动态获取types
 *
 * @returns
 */
const getTypesByDb = () => {
  const url = `${host}/product/typesbydb`;
  return axios.get(url, {
    params: {},
  });
};

export {
  getAllArea,
  getAllTypesMenu,
  getProductResByConCondition,
  getProductImageUrl,
  getTypesByDb,
};
