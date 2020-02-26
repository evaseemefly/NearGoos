<template>
  <div class="center">
    <!-- 主要内容 -->
    <div class="my-content">
      <!-- 中间上部区域 -->
      <div class="center-header">
        <!-- 产品内容 -->
        <div class="product-show">
          <!-- 中间上部左侧区域 -->
          <div class="center-header-left">
            <!-- 菜单栏 -->
            <div class="product-menu">
              <!-- 此处只为示意，之后使用elementui实现功能 -->
              <!-- <ul class="elements-ul">
                <li>Wave</li>
                <li>Sea Surface Temperature</li>
                <li>Current</li>
                <li>Sea Ice</li>
                <li>Far East</li>
              </ul>-->
              <!-- TODO:[*] 19-12-02 此处改为使用elementui -->
              <el-row class="tac">
                <el-col :span="24">
                  <!-- <h5>Type</h5> -->
                  <el-menu
                    default-active="2"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose"
                    background-color="#33cccc"
                    text-color="#fff"
                    active-text-color="#ffd04b"
                    :default-openeds="openList"
                  >
                    <el-submenu
                      v-for="(father, x) in menuList"
                      :index="father.key"
                      :key="x"
                    >
                      <template slot="title">
                        <i class></i>
                        <span>{{ father.val }}</span>
                      </template>
                      <el-menu-item
                        :index="child.key"
                        v-for="(child, y) in father.children"
                        :key="y"
                        @open="selectMenu"
                        @click.native="selectMenu(father.key, child.key)"
                        background-color="#0b6fb1"
                        >{{ child.val }}</el-menu-item
                      >
                    </el-submenu>
                  </el-menu>
                </el-col>
              </el-row>
            </div>
          </div>
          <!-- 中间上部右侧区域 -->
          <div class="center-header-right">
            <!-- 产品展示 -->
            <div class="product-exhibition">
              <!-- 标题 -->
              <div class="product-title">
                <div class="title">{{ titleVal }}</div>
                <!-- 预报时效选择框 -->
                <div class="interval-form">
                  <ul class="interval-ul">
                    <li
                      v-for="(item, index) in getIntervalList"
                      :key="index"
                      @click="loadProductImageUrl(item)"
                    >
                      {{ item.val }}
                    </li>
                  </ul>
                </div>
              </div>
              <!-- 产品图片 -->
              <div class="product-img" v-show="imgShow">
                <img
                  :src="currentImgUrl"
                  width="70%"
                  height="70%"
                  @load="imgShow = true"
                  :style="imgConsumerStyle"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 中间区域-->
      <div class="product-data">
        <!-- 多条件搜索栏 -->
        <div class="product-search">
          <!-- 搜索部分 -->
          <div class="center-center">
            <div class="search-form">
              <div class="title">
                <h2>多条件搜索</h2>
                <h4>根据产品种类-> 产品区域 -> 对应时效 -> 起止时间</h4>
              </div>
              <!-- 搜索条件form -->
              <form @submit.prevent="submit">
                <!-- TODO:[20-01-04] 此处修改改为横向排列 -->
                <div class="form-content">
                  <!-- 产品种类 -->
                  <div class="form-group">
                    <div class="form-select">
                      <label for>Category</label>
                      <el-select
                        v-model="optionCategoryVal"
                        mulitple="true"
                        placeholder="please select"
                      >
                        <el-option
                          v-for="item in optionsCategory"
                          :key="item.key"
                          :label="item.val"
                          :value="item.key"
                        ></el-option>
                      </el-select>
                    </div>
                    <figure>
                      <figcaption>
                        <font-awesome-icon
                          :icon="['far', 'list-alt']"
                          size="2x"
                        />
                        <div>
                          <h4>产品种类</h4>
                          <p>包含各类产品XXXXXXXXXX</p>
                        </div>
                      </figcaption>
                    </figure>
                  </div>
                  <!-- 产品区域 -->
                  <div class="form-group">
                    <div class="form-select">
                      <label for>Area</label>
                      <el-select
                        v-model="optionAreaVal"
                        placeholder="please select"
                      >
                        <el-option
                          v-for="item in optionsArea"
                          :key="item.key"
                          :label="item.val"
                          :value="item.key"
                        ></el-option>
                      </el-select>
                    </div>
                    <figure>
                      <figcaption>
                        <font-awesome-icon
                          :icon="['fas', 'globe-americas']"
                          size="2x"
                        />
                        <div>
                          <h4>产品区域</h4>
                          <p>共包含xxx区域，xxx区域</p>
                        </div>
                      </figcaption>
                    </figure>
                  </div>
                  <!-- 产品时间间隔 -->
                  <div class="form-group">
                    <div class="form-select">
                      <label for>Period</label>
                      <el-select v-model="optionPeriodVal" placeholder="请选择">
                        <el-option
                          v-for="item in optionsPeriod"
                          :key="item.key"
                          :label="item.val"
                          :value="item.key"
                        ></el-option>
                      </el-select>
                    </div>
                    <figure>
                      <figcaption>
                        <font-awesome-icon
                          :icon="['fas', 'history']"
                          size="2x"
                        />
                        <div>
                          <h4>产品时效</h4>
                          <p>时效包括xxxxx,xxxxx,xxxxxx</p>
                        </div>
                      </figcaption>
                    </figure>
                  </div>
                  <!-- 起始时间 -->
                  <div class="form-group">
                    <div class="form-select">
                      <label>Start Date</label>
                      <el-date-picker
                        v-model="startDate"
                        type="date"
                        placeholder="选择日期"
                      ></el-date-picker>
                    </div>
                    <figure>
                      <figcaption>
                        <font-awesome-icon
                          :icon="['fas', 'calendar-check']"
                          size="2x"
                        />
                        <div>
                          <h4>起始时间</h4>
                          <p>包含各类产品XXXXXXXXXX</p>
                        </div>
                      </figcaption>
                    </figure>
                  </div>
                  <div class="form-group">
                    <div class="form-select">
                      <label>End Date</label>
                      <el-date-picker
                        v-model="finishDate"
                        type="date"
                        placeholder="选择日期"
                      ></el-date-picker>
                    </div>
                    <figure>
                      <figcaption>
                        <font-awesome-icon
                          :icon="['fas', 'calendar-week']"
                          size="2x"
                        />
                        <div>
                          <h4>产品种类</h4>
                          <p>包含各类产品XXXXXXXXXX</p>
                        </div>
                      </figcaption>
                    </figure>
                  </div>
                </div>
                <div class="form-content-btn">
                  <!-- TODO:[*] 20-01-04 去掉 种类 区域 间隔 -->
                  <!-- <div class="statistics-info">
                    <span>category</span>
                    <span>{{ categoryVal }}</span>
                  </div>
                  <div class="statistics-info">
                    <span>area</span>
                    <span>{{ areaVal }}</span>
                  </div>
                  <div class="statistics-info">
                    <span>period</span>
                    <span>{{ periodsVal }}</span>
                  </div>
                  <div class="statistics-info">
                    <span>files count</span>
                    <span>73</span>
                  </div>-->
                  <div class="btn">
                    <button type="submit" class="btn btn-primary col-md-6">
                      SEARCH
                    </button>
                  </div>
                </div>
              </form>
              <div class="search-footer">
                <h4>查询符合条件的所有结果</h4>
                <p>若结果没有你满意的结果请联系管理员</p>
                <p>查询只能查询6个月之内的数据</p>
              </div>
            </div>
          </div>
        </div>
        <!-- 选中会加载的数量显示栏 -->
        <div class="product-statistics">
          <div class="center">
            <div class="statistics-info">
              <h4>下载列表</h4>
              <p>{{ countSelected }}个文件</p>
            </div>
            <div class="statistics-btn">
              <button
                class="btn btn-primary col-md-6"
                @click="submitSelectFile"
              >
                下载
              </button>
            </div>
          </div>
        </div>
        <!-- 结果显示栏 -->
        <div class="product-result">
          <!-- 结果部分 -->
          <div class="center-footer">
            <div class="center-footer-card-header">Result</div>
            <div class="center-footer-card-body">
              <el-table
                ref="multipleTable"
                :data="tableData"
                tooltip-effect="dark"
                style="width: 100%"
                @selection-change="handleSelectionChange"
                @select="selectRow"
              >
                <el-table-column type="selection" width="55"></el-table-column>
                <el-table-column label="date" show-overflow-tooltip>
                  <template slot-scope="scope">{{
                    scope.row.date | formatDate2HM
                  }}</template>
                </el-table-column>
                <el-table-column
                  prop="name"
                  label="name"
                  width="120"
                ></el-table-column>
                <el-table-column prop="area" width="120" label="area">
                  <template slot-scope="scope">{{
                    areaConvert(scope.row.area)
                  }}</template>
                </el-table-column>
                <el-table-column
                  prop="interval"
                  label="interval"
                  width="120"
                ></el-table-column>
                <el-table-column
                  prop="type"
                  label="type"
                  width="120"
                ></el-table-column>
              </el-table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import moment from 'moment';

import {
  SearchCondition,
  ProductImageCondition,
} from '@/middle_model/product.ts';
import {
  getAllArea,
  getAllTypesMenu,
  getProductResByConCondition,
  getProductImageUrl,
  getTypesByDb,
} from '@/api/index';
@Component({
  filters: {
    //TODO:[*] 19-12-09 注意在filters中无法使用this
    formatDate2HM(val: Date): string {
      return moment(val).format('YYYY-MM-DD hh:mm');
    },
  },
})
export default class ProductView extends Vue {
  mydata: any = null;
  openList: string[] = [];
  category: Array<{ key: string; val: string }> = [];

  menuList: Array<{
    key: string;
    val: string;
    remark: string;
    children: Array<{
      key: string;
      val: string;
      remark: string;
      periods: string[];
      periodsIndex: string[];
    }>;
  }> = [];
  areaList: Array<{
    key: string;
    val: string;
  }> = [];
  // 暂时不需要type list 直接从menuList的一级数组中查找即可
  // typeList: Array<{ key: string; val: string }> = [];
  intervalList: Array<{ key: string; val: number[] }> = [
    { key: '1-1', val: [24, 48, 72, 96] },
    { key: '1-2', val: [24, 48, 72, 96, 120] },
    { key: '2-1', val: [24, 48, 72, 96, 120] },
  ];

  optionsElements: Array<{ lab: string; val: string }> = [
    { lab: '', val: '' },
    { lab: '', val: '' },
    { lab: '', val: '' },
  ];

  // optionVal: string = '1';
  // 中间左侧的搜索框中select绑定的val
  optionCategoryVal: string = '';
  optionAreaVal: string = '';
  optionPeriodVal: string = '';

  menuIndex: string = '1';
  menuFatherIndex: string = '1';
  menuChildIndex: string = '1';
  // 选中的result的行
  countSelected: number = 0;
  // 时间搜索框绑定的data
  startDate: Date = new Date();
  finishDate: Date = new Date();
  tableData: Array<{
    name: string;
    area: number;
    interval: number;
    date: Date;
    type: number;
    relativePath: string;
  }> = [];
  // 用来存储选中的tableData对应的路径数组
  tableDataPath: string[] = [];

  // 选中的最近的图片的url
  // currentImageUrl: string =
  // '/images/product/data/ftpdownload/wave/2019/10/30/coast04.png';

  rootPath: string = '/images/product/data/ftpdownload/';
  rootType: string = '';
  currentImgRelativePath: string = '';
  currentImgFileName: string = '';

  imgShow: boolean = false;
  imgConsumerStyle: string = 'max-width:500px;';
  handleOpen() {
    console.log('展开');
  }

  handleSelectionChange() {
    console.log('选中改变');
  }
  // TODO:[*] 20-01-05 计算点击个数未实现
  selectRow(selection: any, row: any) {
    console.log(selection);
    console.log(row);
    this.countSelected = selection.length;
  }
  // TODO:[*] 19-12-09 此处加入了新的功能:根据选择的father和child加载对应的 interval list
  selectMenu(father: string, child: string) {
    // console.log(father + "|" + child);
    // TODO:[*] 19-12-07 由于此处修改为读取后台的api返回的menuList动态生成
    // this.menuIndex = child;
    this.menuFatherIndex = father;
    this.menuChildIndex = child;
  }
  handleClose() {}

  submit() {
    let myself = this;
    console.log('提交表单');
    // 1 获取提交的数据
    let params = new SearchCondition(
      myself.optionCategoryVal,
      myself.optionAreaVal,
      myself.optionPeriodVal,
      myself.startDate,
      myself.finishDate
    );
    // 2 提交之后注意要清除当前的tableData
    myself.tableData = [];
    getProductResByConCondition(params).then(res => {
      if (res.status === 200) {
        // console.log(res.data);
        res.data.forEach(
          (temp: {
            name: string;
            area: number;
            interval: number;
            targetDate: Date;
            type: number;
            relativePath: string;
          }) => {
            myself.tableData.push({
              name: temp.name,
              area: temp.area,
              interval: temp.interval,
              date: temp.targetDate,
              type: temp.type,
              relativePath: temp.relativePath,
            });
          }
        );
      }
    });
  }

  // TODO:[*] 20-02-26 获取对应的url地址
  submitSelectFile() {
    this.tableData.forEach(temp => {
      this.tableDataPath.push(
        [
          this.rootPath,
          this.getTypePath(temp.type.toString()),
          temp.relativePath,
          temp.name,
        ].join('/')
      );
    });
  }

  // TODO:[-] 20-02-26 根据传入的type获取对应的typePath(中间的拼接字符串)
  getTypePath(type: string): string | undefined {
    let typePath: string | undefined;
    const targetCategory = this.category.find(
      (temp: { key: string; val: string }) => {
        return temp.key === type;
      }
    );
    if (targetCategory !== undefined) {
      typePath = targetCategory.val;
    }
    return typePath;
  }
  mounted() {
    this.openList = ['1', '2'];
    let myself = this;
    // 之前测试使用，现去掉
    // getAllArea().then((res: any) => {
    // });
    // 获取所有的area的字典
    getAllArea().then((res: any) => {
      if (res.status === 200) {
        res.data.forEach((temp: { key: string; val: string }) => {
          myself.areaList.push({
            key: temp.key,
            val: temp.val,
          });
        });
      }
    });
    getAllTypesMenu().then((res: any) => {
      if (res.status === 200) {
        // console.log(res.data);
        // 将结果赋值给menuList
        /*
        0:
          children: Array(2)
            0:
              key: "1"
              periods: (5) ["24", "48", "72", "96", "120"]
              periodsIndex: (5) ["04", "08", "12", "16", "18"]
              val: "ChinaSea"
              __proto__: Object
            1: {
                key: "2",
               val: "Northwest",
               periods: Array(5),
               periodsIndex: Array(5)
               }
          length: 2
          __proto__: Array(0)
          key: "1"
          val: "wave"
          __proto__: Object
        */
        // 循环res.data
        res.data.forEach(
          (temp: {
            key: string;
            val: string;
            remark: string;
            children: Array<{
              key: string;
              val: string;
              remark: string;
              periods: string[];
              periodsIndex: string[];
            }>;
          }) => {
            // temp.children.forEach(child:{
            //   key: string;
            //   val: string;
            //   periods: string[];
            //   periodsIndex: string[];
            // }=>{

            // })
            // TODO:[*] 19-12-07 此处有一个后台的bug，后台返回的res中，每一项有可能出现不包含children的情况
            // 在判断时需要加入必要的判断
            myself.menuList.push(temp);
          }
        );
      }
    });

    //TODO:[-] 19-12-15 每次加载页面统一从后台获取一次动态的types列表
    getTypesByDb().then(res => {
      if (res.status === 200) {
        // console.log(res.data);
        res.data.forEach((temp: any) => {
          myself.category.push({
            key: temp.id,
            val: temp.name,
          });
        });
      }
    });

    // TODO:[*] 20-01-05 新加入的功能
    /*
      每次加载页面时，获取当前日期的指定 种类 及 区域 的所有的产品列表
      注意：
          截取参数时，截取menuList，而不要使用 areaList (key与db中的id相差1)
          可以只传入
              cateogry area start 不传入 period
    */
    //
    // let cateogryTemp = myself.menuList[0].key;
    // let areaTemp = myself.menuList[0].children[0].key;
    // let now = Date();
    // getProductResByConCondition({
    //   category: cateogryTemp,
    //   area: areaTemp,
    //   start: now,
    // }).then(res => {
    //   console.log(res);
    // });

    this.imgShow = true;
  }
  areaConvert(val: string): string {
    const that = this;
    if (that.areaList) {
      let areas = that.areaList.find(temp => temp.key === val);
      if (areas !== undefined) {
        return areas.val;
      }
    }
    return '';
    // return this.areaList.find(temp => temp.key === val)['val'];
  }

  // TODO:[*] 19-12-10 此处为根据 father child interval 加载获取对应的图片地址
  loadProductImageUrl(interval: { index: string; val: string }): void {
    let _that = this;
    // console.log(interval);
    const params = new ProductImageCondition(
      _that.menuFatherIndex,
      _that.menuChildIndex,
      interval.index
    );
    this.imgShow = false;
    // console.log(params);
    getProductImageUrl(params).then(
      (res: {
        data: {
          name: string;
          relativePath: string;
          type: string;
        };
        status: number;
      }) => {
        if (res.status === 200) {
          // console.log(res.data);
          // _that.currentImageUrl = res.data.imageUrl;
          _that.currentImgRelativePath = res.data.relativePath;
          _that.currentImgFileName = res.data.name;
          /*
          TODO:[-] 19-12-15
              此处新加入了通过页面加载时获取的 动态的（从数据库中读取的）types
              根据返回的type找到对应的types的 val，作为root_type
        */
          // TODO:[-] 20-02-26 此处重新做了封装(-> getTypePath)，以下部分暂时注释掉
          // const targetCategory = _that.category.find(
          //   (temp: { key: string; val: string }) => {
          //     return temp.key === res.data.type;
          //   }
          // );
          // if (targetCategory !== undefined) {
          //   _that.rootType = targetCategory.val;
          // }
          let rootPath = this.getTypePath(res.data.type);
          this.rootType = rootPath != undefined ? rootPath : '';
        }
      }
    );
  }

  get currentImgUrl(): string {
    return [
      this.rootPath,
      this.rootType,
      this.currentImgRelativePath,
      this.currentImgFileName,
    ].join('/');
  }

  get computedTest() {
    return null;
  }

  // 产品种类的下拉选项
  get optionsCategory(): { key: string; val: string }[] {
    // TODO:[*] 19-12-07 注意每个下拉框的计算方法都需要加入清除当前选中的值
    this.optionCategoryVal = '';
    let list: { key: string; val: string }[] = [];
    this.menuList.map(temp => list.push({ key: temp.key, val: temp.val }));
    return list;
  }

  // 产品区域的下拉选项
  get optionsArea(): { key: string; val: string }[] {
    this.optionAreaVal = '';
    let list: { key: string; val: string }[] = [];
    let myself = this;
    // 找到当前 category 选择的对应的menulist中的 obj
    let res = this.menuList.find(temp => myself.optionCategoryVal === temp.key);
    if (res !== undefined) {
      return res.children === undefined ? [] : res.children;
    } else {
      return [];
    }
  }

  // 产品时间间隔的下拉选项
  get optionsPeriod(): { key: string; val: string }[] {
    this.optionPeriodVal = '';
    let list: { key: string; val: string }[] = [];
    let listStr: string[] = [];
    let myself = this;

    // 找到当前 area 选择对应的 intervalList 中的时间间隔数组
    // let res = this.intervalList.find(temp => myself.optionAreaVal === temp.key);
    // TODO:[*] 19-12-05 此处所有的间隔也从menuList中取
    // menuList->children->periods
    if (
      myself.menuList.length > 0 &&
      myself.optionCategoryVal !== '' &&
      myself.optionAreaVal !== ''
    ) {
      let children: Array<{
        key: string;
        val: string;
        periods: string[];
        periodsIndex: string[];
      }> = this.menuList.filter(temp => {
        return temp.key === myself.optionCategoryVal;
      })[0].children;
      if (children !== undefined && children.length > 0) {
        let periods: string[] = [];
        let periodsIndex: string[] = [];
        periods = children.filter(temp => {
          return temp.key === myself.optionAreaVal;
        })[0].periods;
        periodsIndex = children.filter(temp => {
          return temp.key === myself.optionAreaVal;
        })[0].periodsIndex;
        periods.forEach((val, key, arr) => {
          list.push({ key: periodsIndex[key], val: val });
        });
      }
    }

    return list;

    // if (res !== undefined) {
    //   return periods;
    // } else {
    //   return [];
    // }
  }

  get getIntervalList(): Array<{ index: string; val: string }> {
    let myself = this;
    // let res: string[] = [];
    let res: Array<{ index: string; val: string }> = [];
    // TODO:[-] 19-12-02 此处bug已解决
    // let res = myself.intervalList.find(temp => myself.menuIndex === temp.key);
    // if (res !== undefined) {
    //   return res.val;
    // } else {
    //   return [];
    // }
    // TODO:[*] 之前的方式已过期，获取periods通过监听menuFatherIndex与menuChildIndex
    let father = myself.menuList.find(
      temp => myself.menuFatherIndex === temp.key
    );
    if (father !== undefined) {
      let children = father.children;
      let child = children.find(x => myself.menuChildIndex === x.key);
      if (child !== undefined) {
        let periods = child.periods;

        periods.forEach((val, index) => {
          res.push({
            index: child !== undefined ? child.periodsIndex[index] : '',
            val: val,
          });
        });
      }
    }
    return res;
  }

  get categoryVal(): string {
    let myself = this;
    let val = this.menuList.find(temp => temp.key === myself.optionCategoryVal);
    return val === undefined ? '' : val.val;
  }

  get areaVal(): string {
    let myself = this;
    let typeTemp = this.menuList.find(
      temp => temp.key === myself.optionCategoryVal
    );
    if (typeTemp !== undefined) {
      if (typeTemp.hasOwnProperty('children')) {
        let areaTemp = typeTemp.children.find(
          temp => temp.key === myself.optionAreaVal
        );
        return areaTemp === undefined ? '' : areaTemp.val;
      }
    } else {
      return '';
    }
  }

  get periodsVal(): string {
    let myself = this;
    let periodVal = '';
    let typeTemp = this.menuList.find(
      temp => temp.key === myself.optionCategoryVal
    );
    if (typeTemp !== undefined) {
      if (typeTemp.hasOwnProperty('children')) {
        let areaTemp = typeTemp.children.find(
          temp => temp.key === myself.optionAreaVal
        );
        if (areaTemp !== undefined) {
          let index = areaTemp.periodsIndex.indexOf(myself.optionPeriodVal);
          periodVal = areaTemp.periods[index];
        }
      }

      // return areaTemp === undefined ? '' : areaTemp.val;
    } else {
      // return '';
    }
    return periodVal;
  }

  // 20-01-02 ：加入根据选择的菜单动态变化title
  get titleVal(): string {
    // 根据 menuFatherIndex 与 menuChildIndex 获取对应的remark
    let fatherRemark: string = '';
    let childRemark: string = '';
    let myself = this;
    let father = this.menuList.find(
      temp => temp.key === myself.menuFatherIndex
    );
    if (father !== undefined) {
      fatherRemark = father.remark;
      let child = father.children.find(
        temp => temp.key === myself.menuChildIndex
      );
      if (child !== undefined) {
        childRemark = child.remark;
      }
    }

    return fatherRemark + childRemark;
  }

  @Watch('imgShow')
  onIsShow(val: boolean): void {
    let _that = this;
    if (val === true) {
      let parent = document.getElementsByClassName('product-img');
      if (parent.length > 0) {
        let children = parent[0].getElementsByTagName('img');
        if (children.length > 0) {
          let imgNode = children[0];
          console.log(imgNode);
          //naturalWidth: 674
          //naturalHeight: 1057
          //
          /*
          判断原始图片的长宽，
            height > width: 竖着
            height < width:横着
        */
          if (imgNode.naturalHeight > imgNode.naturalWidth) {
            // 竖着
            _that.imgConsumerStyle = 'max-width:500px;';
          } else {
            // 横着
            _that.imgConsumerStyle = 'max-height:500px;';
          }
        }
      }
    }
  }

  @Watch('menuList')
  onMenuList(val: any): void {
    let _that = this;
    // TODO:[*] 20-01-05 每当menulist发生变化时，清空结果table
    _that.tableData = [];
    let cateogryTemp: string = _that.menuList[0].key;
    let areaTemp: string = _that.menuList[0].children[0].key;
    let now: Date = new Date(2019, 11, 13);
    let params: any = {
      category: cateogryTemp,
      area: areaTemp,
      start: now,
    };

    getProductResByConCondition(params).then(res => {
      if (res.status === 200) {
        // console.log(res.data);
        res.data.forEach(
          (temp: {
            name: string;
            area: number;
            interval: number;
            targetDate: Date;
            type: number;
          }) => {
            _that.tableData.push({
              name: temp.name,
              area: temp.area,
              interval: temp.interval,
              date: temp.targetDate,
              type: temp.type,
            });
          }
        );
      }
      // console.log(res);
    });
  }

  // get maxStyle(): any {
  //   // 大体思路，找到 .product-img->img 的长宽
  //   let node = document
  //     .getElementsByClassName('product-img')
  //     .getElemntByTagName('img');
  //   return null;
  // }
}
</script>
<style scoped lang="less">
@import '../styles/base.less';
@bluebackground: {
  // background: rgba(39, 216, 216, 0.377);
  // background: #33cccc;
  background: #1971c2;
  // background: #0b6fb1;
};
@searchtitle: {
};
@middlewidth: {
  width: 80%;
};
@btn: {
  background-color: #00b5ad;
  box-shadow: 0 0 0 0 rgba(34, 36, 38, 0.15) inset;
};
@searchminortitle: {
  // color: #72e9e9;
  // font-size: 1rem;

  margin-left: 2rem;
  margin-top: 0;
  margin-bottom: 0;
  line-height: 2;
  color: #72e9e9;
  font-size: 1rem;
};
// 为二级标题加了一个左+上的间距
@minortitle: {
  // 统计title加一个左+上的间距
  margin-left: 1.5em;
  // margin-top: 1em;
  font-size: 200%;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
};
@fontcolor: {
  color: white;
};
// 统一白色form中的font样式
@whitefont: {
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
  // color: white;
  @fontcolor();
};
// menu中的子menu样式
@menu-child: {
  background: #0b6fb1;
};
// 中间的区域
.center {
  flex: 1;
  display: flex;
  flex-direction: column;

  //产品展示区域,横向排列
  .center-header {
    display: flex;
    flex: 1;
    flex-direction: row;
    justify-content: space-around;

    .product-show {
      display: flex;
      .center-header-left {
        //菜单栏
        display: flex;
        flex: 1;
        flex-direction: row;
        justify-content: flex-start;
        margin-right: 3em;

        .elements-ul {
          display: flex;
          flex: 1;
          flex-direction: column;
          // width: 700px;
          // height: 50px;
          list-style: none;
          margin: 0;
          padding: 0 20px;
          font-size: 30px;
          line-height: 50px;
          // background: #33cccc;
          color: white;
        }
        .product-menu {
          .el-submenu {
            ul {
              li {
                background-color: #0b6fb1 !important;
              }
            }
          }
        }
      }
      .center-header-right {
        //产品
        display: flex;
        flex: 3;
        flex-direction: row;
        justify-content: flex-end;

        .title {
          font-size: 36px;
          line-height: 50px;
          background: #33cccc;
          color: white;
        }

        .interval-ul {
          width: 700px;
          // height: 50px;
          // TODO:[*] 20-01-02 使用flex，不再使用浮动的方式布局li
          display: flex;
          flex-wrap: wrap;
          list-style: none;
          margin: 0;
          padding: 0 20px;
          font-size: 1.5rem;
          // line-height: 50px;
          background: #33cccc;
          color: white;
        }

        .interval-ul li {
          // width: 1.6rem;
          // margin: 0 10px;
          // padding: 0 1ppx;
          padding: 0.5rem;
          // background-color: #0b6fb1 !important;
          // float: left;
        }
        .interval-ul li:hover {
          // transform: scale(2);
          transition: all 1s linear;
          background: #0b6fb1;
          // width: 1.6rem;
          padding: 0.5rem;
        }
      }
    }
  }

  // 中间部分
  // 横向排列
  // 搜索栏区域
  .product-data {
    display: flex;
    flex-direction: column;
    align-items: center;
    // 多条件搜索栏
    .product-search {
      display: flex;
      flex: 1;
      @middlewidth();
      // width: 70%;
      .center-center {
        display: flex;
        flex: 1;
        flex-direction: column;
        @bluebackground();
        @margindefault();
        @borderradius();
        // 搜索栏的title
        .title {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          padding: 1rem;
          h2 {
            @minortitle();
          }
          h4 {
            @searchminortitle();
          }

          // font-size: ;
        }
        // 搜索栏的中间的搜索下拉框及btn
        form {
          display: flex;
          flex-direction: row;
          justify-content: space-around;
          background-color: rgba(3, 3, 3, 0.068);
          // TODO:[*] 19-12-03 之前的form中的六个select是水平排列，现改为2*3
          // .form-content {
          //   display: flex;
          //   flex-direction: column;
          //   background-color: rgba(3, 3, 3, 0.068);
          //   flex: 1;
          //   .form-group {
          //     display: flex;
          //     // flex-direction: column;
          //     justify-content: center;
          //     align-items: center;
          //     label {
          //       @whitefont();
          //       margin: 1em;
          //       display: flex;
          //       width: 5em;
          //     }
          //     .el-select {
          //       display: flex;
          //       max-width: 133px;
          //     }
          //     .el-input {
          //       max-width: 133px;
          //     }
          //   }
          // }

          // TODO:[*] 20-01-04 现又改回横向排列
          .form-content {
            display: flex;
            flex-direction: row;
            // background-color: rgba(3, 3, 3, 0.068);
            flex: 7;
            .form-group {
              padding: 1rem;
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
              .form-select {
                display: flex;
                label {
                  @whitefont();
                  margin: 1em;
                  display: flex;
                  width: 5em;
                }
                .el-select {
                  display: flex;
                  max-width: 133px;
                }
                .el-input {
                  max-width: 133px;
                }
              }
              figure {
                figcaption {
                  display: flex;
                  svg {
                    margin: 1em;
                    @fontcolor();
                  }
                  div {
                    display: flex;
                    flex-direction: column;
                    @fontcolor();
                    h4 {
                      font-weight: 500;
                    }
                    // 给p一个浅色一点的颜色，建议以底色纵向取颜色
                    p {
                      color: #72e9e9;
                    }
                  }
                }
              }
            }
          }

          .form-content-btn {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            .statistics-info {
              display: flex;
              justify-content: space-between;
              color: #838e95;
              padding: 1em;
              border-bottom: 1px solid #d5dce5;
              span:first-child {
                font-weight: 600;
                color: #272727;
              }
              span:last-child {
                font-weight: 500;
                color: #838e95;
              }
            }

            .btn {
              display: flex;
              justify-content: center;
              align-items: center;

              button {
                color: #fff;
                height: 3em;
                @btn();
                // 暂时对提交按钮 先不上色了
                // background-color: #2bbbad !important;
              }
            }
          }
        }
        // TODO:[*] 20-01-04 新加入了一个底部的提示栏
        .search-footer {
          padding: 1rem;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          // background: #98c2c2;
          h4 {
            margin-left: 2rem;
            color: white;
            font-weight: 600;
            font-size: 1rem;
          }
          p {
            @searchminortitle();
          }
        }
      }
    }
    // 中间显示选中数量的统计栏
    .product-statistics {
      display: flex;
      @middlewidth();
      // justify-content: space-between;
      // align-items: center;
      // background: #838e95;
      .center {
        @paddingdefaultxs();
        @borderradius();
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        color: white;
        // background: #b2c2cc;
        @bluebackground();
        @margindefault();
        .statistics-info {
          display: flex;
          align-items: center;
          h4 {
            margin-left: 2rem;
            // font-weight: 600;
            // font-size: 1rem;
            // 和多条件搜索 与 下面的列表的title样式统一
            @minortitle();
          }
          p {
            margin-left: 2rem;
            margin-top: 0;
            margin-bottom: 0;
            // line-height: 2;
            color: #72e9e9;
            font-size: 1rem;
          }
        }
        .statistics-btn {
          width: 15rem;
          button {
            @btn();
          }
        }
      }
    }
    // 结果栏
    .product-result {
      display: flex;
      flex: 1.5;
      @middlewidth();
      .center-footer {
        display: flex;
        flex: 2;
        // background: rgb(42, 134, 146);
        @bluebackground();
        flex-direction: column;
        @margindefault();
        @borderradius();

        .center-footer-card-header {
          display: flex;
          justify-content: flex-start;
          padding: 1rem;
          @minortitle();
        }

        .center-footer-card-body {
          background: white;
        }
      }
    }
  }
}
</style>
