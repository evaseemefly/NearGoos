import axios from 'axios';

// 后端的请求地址及端口
//
export const host = 'http://localhost:8083';
axios.defaults.withCredentials = true;
axios.defaults.headers = {};
/**
 * 根据code以及date 读取指定时刻的散点
 *
 * @param {string} code
 * @returns
 */
const getAllArea = () => {
  let url = `${host}/product/area`;
  return axios.get(url, {
    params: {},
  });
};

const getAllTypesMenu = () => {
  let url = `${host}/product/menu/list`
  return axios.get(url, {
    params: {}
  })
}

const getProductResByConCondition = (params: any) => {
  let url = `${host}/product/list`;
  return axios.get(url, {
    params: {
      cateogry: params.cateogry,
      area: params.area,
      period: params.period,
      start: params.start,
      end: params.end
    }
  })
}

export { getAllArea, getAllTypesMenu, getProductResByConCondition };
