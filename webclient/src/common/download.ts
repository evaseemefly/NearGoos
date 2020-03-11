// 本包用来实现批量文件下载功能
// 目前自己梳理的流程
/*
  1- 使用 FileSaver.js 实现对远端文件的下载
  2- 使用jszip 实现对已经下载的文件的打包
*/
import 'jszip';
import JSZip from 'jszip';
// import { saveAs } from 'file-saver';
import FileSaver from 'file-saver';

export interface IFileOption {
  // http://localhost:8080/images/product/data/ftpdownload//wave/2019/12/13/coast08.png
  url: string;
  filename: string;
  ext?: string;
}

export class DownLoad<T extends IFileOption> {
  /**
   * 需要批量下载的文件地址
   *
   * @private
   * @type {string[]}
   * @memberof DownLoad
   */
  private fileUrls: T[] = [];
  private zip: JSZip;
  private dirName: string;
  constructor(urls: T[]) {
    this.fileUrls = urls;
    // TODO:[*] 20-02-27 注意此处有一个类型提示
    this.zip = new JSZip();
    this.dirName = 'defalut';
  }

  /**
   * 创建本地的保存文件夹 -> .zip
   *
   * @param {string} dirName
   * @memberof DownLoad
   */
  private initFolder(dirName?: string): JSZip {
    return this.zip.folder(dirName ? dirName : this.dirName);
  }

  private urlToPromise(url: string) {
    // return new Promise(function(resolve, reject) {
    //   JSZipUtils.getBinaryContent(url, function(err, data) {
    //     if (err) {
    //       reject(err);
    //     } else {
    //       resolve(data);
    //     }
    //   });
    // });
  }

  /**
   * 根据url从远端下载文件存储在本地指定folder(dirName)中
   *
   * @param {string} url
   * @memberof DownLoad
   */
  private storeFileFromRemote(url: string, name: string): void {
    // 可以通过file-saver 直接对指定路径的文件进行下载(对于数量较大的文件，最好还是加入一个打包的流程)
    FileSaver.saveAs(url, name);
  }
  download(): void {
    
    this.fileUrls.forEach(temp => {
      this.storeFileFromRemote(temp.url, temp.filename);
    });
  }

  /**
   * 将当前的 fileUrls 批量添加至zip 压缩 路径下并统一打包
   *
   * @memberof DownLoad
   */
  private toZip(): void {
    this.fileUrls.forEach(fileUrlTemp => {
      this.zip.file(
        fileUrlTemp.filename + (fileUrlTemp.ext ? fileUrlTemp.ext : '.jpg'),
        fileUrlTemp.url
      );
    });
  }
  private imgeToBase64(url: string) {
    const image = new Image();
    image.crossOrigin = 'Anonymous';
    image.src = url;
    const deferred = $.Deferred();
    if (url) {
      image.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
        }
        const dataURL = canvas.toDataURL();
        deferred.resolve(dataURL);
      };
      return deferred.promise();
    }
    //     }
  }
}
