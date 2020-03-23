// 主要参考[https://www.mmxiaowu.com/article/59b23f5d5b06a403cf687ed6]

import axios from 'axios';
import JSZip from 'jszip';
import FileSaver from 'file-saver';
import { clientHost } from '@/api/common';

/**
 * 批量下载
 *
 * @export
 * @class BatchDownLoad
 */
export class BatchDownLoad {
  private zipNameDefault = 'default.zip';
  getFile(url: string) {
    // TODO:[-] 20-02-27 此处多一步操作，加入 公共的域
    // TODO:[*] 20-02-27 注意此处有一个小bug，就是拼接地址时：会出现多个 //的情况，目前先使用filter过滤掉
    // 由于时间字符串2019\12\13解析时不会受影响 ,暂时先不管
    // eg: "/images/product/data/ftpdownload///2019\12\13/coast04.png"
    const urlSpiltArr = url.split('/').filter(temp => {
      return temp != '';
    });
    url = [clientHost, ...urlSpiltArr].join('/');
    return new Promise((resolve, reject) => {
      // 以二进制流的形式从指定url读取
      axios({
        method: 'get',
        url,
        responseType: 'arraybuffer',
      })
        .then(data => {
          resolve(data.data);
        })
        .catch(error => {
          reject(error.toString());
        });
    });
  }

  /**
   *
   *
   * @param {string[]} urls 注意！暂时传递相对路径，域在此处加上
   * @param {string} [saveZipName]
   * @memberof BatchDownLoad
   */
  batchDownload(urls: string[], saveZipName?: string) {
    const zip = new JSZip();
    const cache = {};
    // promise的数组
    const promises = [];
    urls.forEach(item => {
      const promise = this.getFile(item).then(data => {
        // 下载文件, 并存成ArrayBuffer对象
        const urlTemp = item.split('/');
        // xxx.png
        const fileName = urlTemp[urlTemp.length - 1]; // 获取文件名
        // TODO:[-] 20-03-21 由于下载同一种类不同日期的文件会出现同名的问题，创建文件时会出现覆盖的问题，建议加上时间戳
        // 时间戳精确到毫秒
        const timestamp = new Date().valueOf();
        const filesplitnames = fileName.split('.');
        filesplitnames.splice(1, 0, '_');
        filesplitnames.splice(2, 0, timestamp.toString());
        filesplitnames.splice(3, 0, '.');
        const fileSaveName = filesplitnames.join('');
        console.log(timestamp);
        zip.file(fileSaveName, data, { binary: true }); // 逐个添加文件
        cache[fileSaveName] = data;
      });
      promises.push(promise);
    });
    // promise的数组均变为resolve后，才then的方法
    Promise.all(promises).then(() => {
      zip.generateAsync({ type: 'blob' }).then(content => {
        // 生成二进制流
        // 存储
        FileSaver.saveAs(
          content,
          saveZipName ? saveZipName : this.zipNameDefault
        );
      });
    });
  }
}
