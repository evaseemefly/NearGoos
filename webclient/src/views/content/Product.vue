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
                    <el-submenu v-for="(father, x) in menuList" :index="father.key" :key="x">
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
                    <li v-for="(item, index) in getIntervalList" :key="index">{{ item }}</li>
                  </ul>
                </div>
              </div>
              <!-- 产品图片 -->
              <div class="product-img">
                <img src="image/Product_img.jpg" width="70%" height="70%" />
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
              <form>
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
                    <el-select v-model="optionAreaVal" placeholder="please select">
                      <el-option
                        v-for="item in optionsArea"
                        :key="item.key"
                        :label="item.val"
                        :value="item.key"
                      ></el-option>
                    </el-select>
                  </div>
                  <!-- <div class="form-group">
                    <label for>Elements</label>
                    <el-select v-model="value" placeholder="please select">
                      <el-option
                        v-for="item in optionsElements"
                        :key="item.val"
                        :label="item.lab"
                        :value="item.val"
                      ></el-option>
                    </el-select>
                  </div>-->
                </div>
                <div class="form-content">
                  <div class="form-group">
                    <label for>Period</label>
                    <el-select v-model="optionPeriodVal" placeholder="请选择">
                      <el-option
                        v-for="item in optionsPeriod"
                        :key="item"
                        :label="item"
                        :value="item"
                      ></el-option>
                    </el-select>
                  </div>
                  <!--<div class="form-group">
                    <label for>start date</label>
                    <el-select v-model="value" placeholder="请选择">
                      <el-option
                        v-for="item in optionsCategory"
                        :key="item.val"
                        :label="item.lab"
                        :value="item.val"
                      ></el-option>
                    </el-select>
                  </div>
                  <div class="form-group">
                    <label for>end date</label>
                    <el-select v-model="value" placeholder="请选择">
                      <el-option
                        v-for="item in optionsCategory"
                        :key="item.val"
                        :label="item.lab"
                        :value="item.val"
                      ></el-option>
                    </el-select>
                  </div>-->
                </div>
                <div class="form-content-btn">
                  <div class="statistics-info">
                    <span>category</span>
                    <span>wave</span>
                  </div>
                  <div class="statistics-info">
                    <span>area</span>
                    <span>china sea</span>
                  </div>
                  <div class="statistics-info">
                    <span>period</span>
                    <span>48</span>
                  </div>
                  <div class="statistics-info">
                    <span>files count</span>
                    <span>73</span>
                  </div>
                  <div class="btn">
                    <button type="submit" class="btn btn-primary col-md-6">SEARCH</button>
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
      period: string;
    }>;
  }> = [
    // {
    //   key: '0',
    //   val: 'null',
    //   children: [{ key: '0', val: 'null' }],
    // },
    {
      key: '1',
      val: 'wave',
      children: [
        { key: '1-1', val: 'ChinaSea', period: '1-1' },
        { key: '1-2', val: 'Northwest', period: '1-2' },
      ],
    },
    {
      key: '2',
      val: 'Current',
      children: [
        { key: '2-1', val: 'EastChinaSea', period: '1-1' },
        { key: '2-2', val: 'Northwest', period: '1-1' },
        { key: '2-3', val: 'FarEast', period: '1-2' },
      ],
    },
    // {
    //   key: "8",
    //   val: "Ice",
    //   children: [{ key: "9", val: "Bohai" }]
    // },
    // {
    //   key: "10",
    //   val: "Template",
    //   children: [
    //     { key: "11", val: "EastChinaSea" },
    //     { key: "12", val: "Northwest" }
    //   ]
    // }
  ];

  intervalList: Array<{ key: string; val: number[] }> = [
    { key: '1-1', val: [24, 48, 72, 96] },
    { key: '1-2', val: [24, 48, 72, 96, 120] },
    { key: '2-1', val: [24, 48, 72, 96, 120] },
  ];

  // 下拉框
  // optionsCategory: Array<{ val: string; lab: string> }> = [
  //   { val: "选项1", lab: "测试" }
  // ];
  // optionsCategory: Array<{ lab: string; val: string }> = [
  //   { val: '1', lab: 'wave' },
  //   { val: '2', lab: 'current' },
  //   { val: '3', lab: 'ice' },
  //   { val: '4', lab: 'template' },
  // ];

  // optionsArea: Array<{ lab: string; val: string }> = [
  //   { lab: '', val: '' },
  //   { lab: '', val: '' },
  //   { lab: '', val: '' },
  // ];

  optionsElements: Array<{ lab: string; val: string }> = [
    { lab: '', val: '' },
    { lab: '', val: '' },
    { lab: '', val: '' },
  ];
  // optionsPeriod: Array<{ lab: string; val: string }> = [
  //   { lab: '', val: '' },
  //   { lab: '', val: '' },
  //   { lab: '', val: '' },
  // ];
  // optionVal: string = '1';
  optionCategoryVal: string = '';
  optionAreaVal: string = '';
  // optionElementsVal: string = '1';
  optionPeriodVal: string = '';

  menuIndex: string = '1';

  handleOpen() {
    console.log('展开');
  }
  selectMenu(father: string, child: string) {
    // console.log(father + "|" + child);
    this.menuIndex = child;
  }
  handleClose() {}
  mounted() {
    this.openList = ['1', '2'];
  }
  get computedTest() {
    return null;
  }

  get optionsCategory(): { key: string; val: string }[] {
    let list: { key: string; val: string }[] = [];
    this.menuList.map(temp => list.push({ key: temp.key, val: temp.val }));
    return list;
  }

  get optionsArea(): { key: string; val: string }[] {
    let list: { key: string; val: string }[] = [];
    let myself = this;
    // 找到当前 category 选择的对应的menulist中的 obj
    let res = this.menuList.find(temp => myself.optionCategoryVal === temp.key);
    if (res !== undefined) {
      return res.children;
    } else {
      return [];
    }
  }

  get optionsPeriod(): number[] {
    let list: { key: string; val: string }[] = [];
    let myself = this;
    // 找到当前 area 选择对应的 intervalList 中的时间间隔数组
    let res = this.intervalList.find(temp => myself.optionAreaVal === temp.key);
    if (res !== undefined) {
      return res.val;
    } else {
      return [];
    }
  }

  get getIntervalList(): number[] {
    let myself = this;
    // TODO:[-] 19-12-02 此处bug已解决
    let res = myself.intervalList.find(temp => myself.menuIndex === temp.key);
    if (res !== undefined) {
      return res.val;
    } else {
      return [];
    }
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
          padding:1em;
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
</style>
