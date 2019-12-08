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
                      >{{ child.val }}</el-menu-item>
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
                <div class="title">China Sea XXX Numeric Forecast</div>
                <!-- 预报时效选择框 -->
                <div class="interval-form">
                  <ul class="interval-ul">
                    <li
                      v-for="(item, index) in getIntervalList"
                      :key="index"
                    >
                      {{ item }}
                    </li>
                  </ul>
                </div>
              </div>
              <!-- 产品图片 -->
              <div class="product-img">
                <img
                  src="image/Product_img.jpg"
                  width="70%"
                  height="70%"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 中间区域-->
      <div class="product-data">
        <div class="product-search">
          <!-- 搜索部分 -->
          <div class="center-center">
            <div class="search-form">
              <div class="title">SEARCH</div>
              <!-- 搜索条件form -->
              <form @submit.prevent="submit">
                <div class="form-content">
                  <div class="form-group">
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
                  <div class="form-group">
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
                </div>
                <div class="form-content">
                  <div class="form-group">
                    <label for>Period</label>
                    <el-select
                      v-model="optionPeriodVal"
                      placeholder="请选择"
                    >
                      <el-option
                        v-for="item in optionsPeriod"
                        :key="item.key"
                        :label="item.val"
                        :value="item.key"
                      ></el-option>
                    </el-select>
                  </div>
                  <div class="form-group">
                    <label>Start Date</label>
                    <el-date-picker
                      v-model="startDate"
                      type="date"
                      placeholder="选择日期"
                    >
                    </el-date-picker>
                  </div>
                  <div class="form-group">
                    <label>Start Date</label>
                    <el-date-picker
                      v-model="finishDate"
                      type="date"
                      placeholder="选择日期"
                    >
                    </el-date-picker>
                  </div>
                </div>
                <div class="form-content-btn">
                  <div class="statistics-info">
                    <span>category</span>
                    <span>{{categoryVal}}</span>
                  </div>
                  <div class="statistics-info">
                    <span>area</span>
                    <span>{{areaVal}}</span>
                  </div>
                  <div class="statistics-info">
                    <span>period</span>
                    <span>{{periodsVal}}</span>
                  </div>
                  <div class="statistics-info">
                    <span>files count</span>
                    <span>73</span>
                  </div>
                  <div class="btn">
                    <button
                      type="submit"
                      class="btn btn-primary col-md-6"
                    >
                      SEARCH
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="product-result">
          <!-- 结果部分 -->
          <div class="center-footer">
            <div class="center-footer-card-header">Result</div>
            <div class="center-footer-card-body">
              <table class="table table-striped table-bordered">
                <thead>
                  <!-- <th>
                    <td>header1</td>
                    <td>header2</td>
                    <td>header3</td>
                    <td>header4</td>
                    <td>header5</td>
                    <td>header6</td>
                  </th>-->
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import { SearchCondition } from '@/middle_model/product.ts';
import {
  getAllArea,
  getAllTypesMenu,
  getProductResByConCondition,
} from '@/api/index';
@Component({})
export default class ProductView extends Vue {
  mydata: any = null;
  openList: string[] = [];
  menuList: Array<{
    key: string;
    val: string;
    children: Array<{
      key: string;
      val: string;
      periods: string[];
      periodsIndex: string[];
    }>;
  }> = [];

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

  // 时间搜索框绑定的data
  startDate: Date = new Date();
  finishDate: Date = new Date();
  handleOpen() {
    console.log('展开');
  }
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
    getProductResByConCondition(params).then(res => {
      if (res.status === 200) {
        console.log(res.data);
      }
    });
  }
  mounted() {
    this.openList = ['1', '2'];
    let myself = this;
    // 之前测试使用，现去掉
    // getAllArea().then((res: any) => {
    // });
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
            children: Array<{
              key: string;
              val: string;
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

  get getIntervalList(): string[] {
    let myself = this;
    let res: string[] = [];
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
        res = child.periods;
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
      let areaTemp = typeTemp.children.find(
        temp => temp.key === myself.optionAreaVal
      );
      return areaTemp === undefined ? '' : areaTemp.val;
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
      let areaTemp = typeTemp.children.find(
        temp => temp.key === myself.optionAreaVal
      );
      if (areaTemp !== undefined) {
        let index = areaTemp.periodsIndex.indexOf(myself.optionPeriodVal);
        periodVal = areaTemp.periods[index];
      }
      // return areaTemp === undefined ? '' : areaTemp.val;
    } else {
      // return '';
    }
    return periodVal;
  }
}
</script>
<style scoped lang="less">
@import '../styles/base.less';
@bluebackground: {
  background: rgba(39, 216, 216, 0.897);
  // background: #0b6fb1;
};
// 为二级标题加了一个左+上的间距
@minortitle: {
  // 统计title加一个左+上的间距
  margin-left: 1.5em;
  margin-top: 1em;
  font-size: 200%;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
};
// 统一白色form中的font样式
@whitefont: {
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
  color: white;
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
          height: 50px;
          list-style: none;
          margin: 0;
          padding: 0 20px;
          font-size: 30px;
          line-height: 50px;
          background: #33cccc;
          color: white;
        }

        .interval-ul li {
          width: 70px;
          margin: 0 10px;
          float: left;
        }
      }
    }
  }

  // 中间部分
  // 横向排列
  .product-data {
    display: flex;

    .product-search {
      display: flex;
      flex: 1;
      .center-center {
        display: flex;
        flex: 1;
        flex-direction: column;
        @bluebackground();
        @margindefault();
        @borderradius();

        .title {
          @minortitle();
          // font-size: ;
        }

        form {
          display: flex;
          flex-direction: row;
          justify-content: space-around;

          // TODO:[*] 19-12-03 之前的form中的六个select是水平排列，现改为2*3
          .form-content {
            display: flex;
            flex-direction: column;
            background-color: rgba(3, 3, 3, 0.068);
            flex: 1;
            .form-group {
              display: flex;
              // flex-direction: column;
              justify-content: center;
              align-items: center;
              label {
                @whitefont();
                margin: 1em;
                display: flex;
                width: 5em;
              }
              .el-select {
                display: flex;
              }
            }
          }
          .form-content-btn {
            flex: 1;
            display: flex;
            flex-direction: column;
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
          }

          .btn {
            display: flex;
            justify-content: center;

            button {
              color: #fff;
              // 暂时对提交按钮 先不上色了
              // background-color: #2bbbad !important;
            }
          }
        }
      }
    }

    .product-result {
      display: flex;
      flex: 1.5;
      .center-footer {
        display: flex;
        flex: 2;
        // background: rgb(42, 134, 146);
        @bluebackground();
        flex-direction: column;
        @margindefault();
        @borderradius();

        .center-footer-card-header {
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
