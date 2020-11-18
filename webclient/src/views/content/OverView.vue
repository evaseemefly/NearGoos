<template>
  <div class="my-content">
    <div class="content-introduce isOpacity" @mouseenter="over">
      <!-- 左侧导航栏 -->
      <ul>
        <li
          :key="item.key"
          v-for="item in tabContent"
          @click="setTabIndex(item.key)"
        >
          {{ item.title }}
        </li>
        <!-- <li>About NEAR-GOOS</li>
        <li>First Phase Success</li>
        <li>Objectives Basis</li>
        <li>Activities</li>
        <li>Scientific Basis</li>
        <li>Principles</li>
        <li>Data</li> -->
      </ul>
      <!-- <div class='left-bar'>
        </div> -->
      <!-- 右侧具体内容 -->

      <div class="right-content">
        <transition name="tabcontent" mode="out-in">
          <h4 class="item" :key="TabContent.key" v-html="TabContent.val">
            <!-- {{ TabContent.val }} -->
          </h4>
        </transition>
      </div>
    </div>
    <div class="content-1 fade-in-slow" @mouseenter="over">
      <div class="content-1-title">
        <h1>NEAR-GOOS</h1>
        <h4>
          NEAR (North-East Asian Regional)-GOOS is a regional pilot project of
          GOOS in the North-East Asian Region, implemented by China, Japan, the
          Republic of Korea and the Russian Federation as one activity of IOC
          Sub-Commission for the Western Pacific (WESTPAC). NEAR-GOOS was
          conceived and initiated upon the formal adoption of the NEAR-GOOS
          Implementation Plan and Operational Manual the Intergovernmental
          Oceanographic Commission following a recommendation from the WESTPAC
          Regional Sub commission of IOC earlier in the year. It became one of
          the first regional pilot projects of GOOS. The primary aim of
          NEAR-GOOS in its first phase was to facilitate the sharing of
          oceanographic data gathered by agencies of the partner countries using
          the internet, to support the daily mapping of conditions in the
          marginal seas bordered by the partner countries. Although it was
          anticipated that this should eventually lead to improvement in the
          availability of information and ocean services for all kinds of
          beneficial purposes, it is important to note that these flow-on
          outcomes were not specific goals for the first phase.
        </h4>
      </div>
    </div>

    <div class="content-2 isOpacity" @mouseenter="over">
      <div class="content-1-title">
        <h1>Goals</h1>
        <h4>
          The goals of NEAR-GOOS in its second phase is to development of a
          basic integrated ocean observing and operational forecasting system in
          the NEAR-GOOS area adhering to the GOOS Principles and building on the
          data management and exchange mechanisms developed in the first phase
          through the inclusion of additional parameters, increased coverage in
          space and time, the generation of a generic suite of data products and
          adequate quality control and quality assurance procedures.
        </h4>
      </div>
    </div>
    <div class="content-3 isOpacity" @mouseenter="over">
      <div class="content-1-title">
        <h1>Missions</h1>
        <div class="minor_title">
          <h4>
            The mission of NEAR-GOOS in its second phase is to develop a
            comprehensive and sustained ocean observing network in the
            North-East regional seas and coastal regions, especially focused on
            observations, monitoring and other activities that cannot be easily
            implemented by countries acting independently. This network will
            embrace a wide range of data types and will be accompanied by the
            participating members and as a contribution to the GOOS and other
            global observing initiatives.
          </h4>
        </div>
      </div>
    </div>
    <div class="content-4 isOpacity" @mouseenter="over">
      <div class="content-1-title">
        <h1>Area of NEAR-GOOS</h1>
        <div class="minor_title">
          <h4>
            The area of NEAR-GOOS is the North-East Asian Region, which is a
            part of the WESTPAC region, bounded by China, Republic of Korea,
            Democratic People's Republic of Korea and the Russian Federation
            along its western boundary, and by the Russian Federation and Japan
            along the eastern boundary.
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>
<script scoped lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
@Component({})
export default class OverView extends Vue {
  mydata: any = null;
  tabIndex: number = 0;
  tabContent: { key: number; title: string; val: string }[] = [
    {
      key: 0,
      title: 'About Us',
      val:
        'China Real Time Data Base (RTDB) of North-East Asian Regional Global Ocean Observing System (NEAR-GOOS) is operated by National Marine Environmental Forecasting Center (NMEFC) of Ministry of Natural Resources of China. <br>China RTDB of NEAR-GOOS provides real-time observation data and services to all users freely and openly through this website.<br> Real-time observation data based on coastal observing stations, buoys and Volunteer ships are shared at their respectively fixed frequency every day. Services including forecasting products of wave, temperature, current and ice with different forecasting periods near to the coast of China or in Northwest of Pacific are also provided each day. ',
    },
    {
      key: 1,
      title: 'Activities',
      val:
        'The 18th Session of NEAR-GOOS Coordinating Committee Meeting was hosted by NMEFC in Fujian of China during 20-22 November 2017.<br>The 8th Session of NEAR-GOOS Coordinating Committee Meeting was hosted in Beijing of China during 8-10 December of 2003.<br>The 3rd session of NEAR-GOOS Coordinating Committee Meeting was hosted in Beijing of China during 3-6 August 1998.',
    },
    {
      key: 2,
      title: 'About NEAR-GOOS',
      val:
        'The North-East Asian Regional Global Ocean Observing System (NEAR-GOOS) is a regional pilot project of GOOS in the North-East Asian Region, implemented by China, Japan, the Republic of Korea and the Russian Federation as one activity of IOC Sub-Commission for the Western Pacific (WESTPAC). <br> NEAR-GOOS was conceived and initiated upon the formal adoption of the NEAR-GOOS Implementation Plan and Operational Manual the Intergovernmental Oceanographic Commission following a recommendation from the WESTPAC Regional Sub commission of IOC earlier in the year. <br>It became one of the first regional pilot projects of GOOS.',
    },
    {
      key: 3,
      title: 'First Phase Success',
      val:
        'The most important success of NEAR-GOOS in its first phase were:<br>1. The consolidation of a functional two-mode distributed Internet-based database structure in the partner countries as a workable model for the enhancement and coordinated handing of oceanographic data at national level;<br>2. The linking of this structure with two Regional Databases that are responsible for the receipt and merging of data concerning the NEAR-GOOS region as a whole, thus creating a regional database system which is part of GOOS;<br>3. The adoption and practice of a free and open data exchange policy, predating the formulation of such a policy for GOOS as a whole;4. The implementation of coordinated and approved data exchange management training for regional participants.',
    },
    {
      key: 4,
      title: 'Objectives Basis',
      val:
        'The initial objectives are to establish a real-time data base and a delayed mode data base for NEAR-GOOS, which are operationally closely linked. The oceanographic data are reported to the NEAR-GOOS Real-Time Data Base through the GTS (Global Telecommunication System, WMO), or directly by electronic means. The whole data sets are to be transferred on a periodic basis from the Real-time data base to the NEAR-GOOS Delayed Mode data base. The two data bases are accessible by the participating countries and other countries through an electronic mail system.<br>As it enters its second phase greater attention needs to be placed on how NEAR-GOOS should be strategically developed to deliver benefit and utility of its ocean data-gathering effort to its member states. This might involve a greater range of data types and the deriving of generic products such as model analyses and synthesized maps. For this to be possible, it will also require more direct involvement of the agencies concerned and the recruitment of a wider range of organizations and disciplines.',
    },
    {
      key: 5,
      title: 'Scientific Basis',
      val:
        'The process directly induced by atmospheric forcing, such as winds, waves, storm surges, and wind-induced surface current, can be modeled with provision of the proper atmospheric forcing. The prediction accuracy of the models relies on the improvement of estimation of the wind at the ocean surface. Data assimilation made from the daily data set is useful for ocean services and other applications.<br> physical processes in semi-enclosed seas are governed not only by local forcing such as surface fluxes from the atmosphere and mass fluxes from rivers , but also by water exchange with outer regions . The volume flux can now be estimated from sea level differences, satellite measurements by altimeter, electric measurement by submarine cables, and other means on a daily basis. <br>Accurate forecasting of oceanographic conditions is at hand, but forecasting also needs a timely supply of in situ data. Long-term observations are currently the only way to ascertain trends and low frequency variability of the ocean. There is a crucial need for robust and reliable data management system on a regional scale because of the quantity of data required.',
    },
    {
      key: 6,
      title: 'Principles',
      val:
        '1. The participating countries recognize the importance of regional cooperation, in particular in the North-East Asian Region, for ocean observing and research activities, within the framework of the Global Ocean Observing System;<br>2. Each participating country shall designate responsible organizations to participate in NEAR-GOOS;<br>3. Each participating country shall implement NEAR GOOS in co-operation with IOC and the other organizations co-sponsoring GOOS;<br>4. The data obtained within the context of NEAR-GOOS shall be made available to the Data Bases, and shall be accessible to other countries within the framework of GOOS.<br>5. ALL IOC-and particularly WESTPAC-Member States, is encouraged to participate in NEAR-GOOS through the submission of data and use of the NEAR-GOOS data bases.',
    },
    {
      key: 7,
      title: 'Data',
      val:
        'The oceanographic data for NEAR-GOOS are temperature, currents, waves, sea-level, and other meteorological elements. Collection of observation data in real-time is very expensive. <br>It also has limitation in space and time for the operational service, which can be overcome by means of in-directed method of data producing, such as numerical modeling. <br>They are complementary to each other, and will enhance the operational capability. The NEAR-GOOS region is one of the most densely and frequently surveyed areas in the world. <br>Observations by research vessels have taken place routinely along sections for more than 50 years. Human activities in the region are extensive; thus, the need for environmental monitoring is crucial. <br>Ocean monitoring activities in the region include in situ data -by moored surface buoys, drifting buoys, towers, coastal stations, research vessels, and voluntary observation ships. <br>The implementation of NEAR-GOOS will require the collection of oceanographic data, as well as marine meteorological and other data.',
    },
    {
      key: 8,
      title: 'Services',
      val:
        'Oceans covering almost 70% of the Earth’s surface are a major driver of the world’s weather and climate.<br> Ocean foresting services play an important role in human and property safety at seas, coastal management, climate change, economic growth, etc. A series of marine forecasting services including numeric forecasting products of wave, temperature, current and ice with different forecasting periods near to the coast of China or in Northwest of Pacific are freely and openly provided every day',
    },
  ];
  mounted() {}
  setTabIndex(val: number) {
    this.tabIndex = val;
  }
  get computedTest() {
    return null;
  }

  over(item: {
    target: {
      classList: any;
    };
  }) {
    //为动态添加class使用
    console.log('触发移入效果' + item);
    // 先判断当前classlist中是否已经包含了fade-in-slow
    // const isMatch = item.target.classList.filter(temp => {
    //   return temp === 'fade-in-slow';
    // });
    let isMatch = false;
    item.target.classList.forEach((temp: any) => {
      if (temp === 'fade-in-slow') {
        isMatch = true;
      }
    });
    if (!isMatch) {
      item.target.classList.add('fade-in-slow');
    }
  }
  @Watch('tabIndex')
  onTabIndex(val: number) {}

  get TabContent() {
    const tempContent = this.tabContent.find(temp => {
      if (temp.key === this.tabIndex) {
        return temp;
      }
    });
    if (tempContent != undefined) {
      return tempContent;
    }
  }
}
</script>
<style scoped lang="less">
@import '../../styles/base.less';
// TODO:[-] 20-03-06 统一放在base中了
// @basefontshadow: {
//   text-shadow: 2px 2px 10px #000;
// };
@basebackgroundimage: {
  // background-size: 100% auto;
  background-size: cover;
  background-color: #3434353b;
};

.isOpacity {
  // opacity: 0.1;
}

.fade-in-slow {
  animation: 0.8s fade-in-slow;
}
@keyframes fade-in-slow {
  0% {
    // background-color: #001f3f;
    opacity: 0.8;
    transform: translateY(30px);
    // transform: translateZ(-50px)
  }
  100% {
    // background-color: #ff4136;
    opacity: 1;
    transform: translateY(-0px);
    // transform: translateZ(0px);
  }
}
// 含图片的背景
.basecontent() {
  height: 900px;
  display: flex;
  font-family: Arial, Helvetica, sans-serif;
}
// 所有的描述性文字的样式（主要是行高）
.desfont() {
  line-height: 1.8;
}
// 定义的 白色的描述性字体
.deswhite() {
  color: aliceblue;
  font-size: 600;
}
.h4() {
  font-size: 25px;
  text-align: justify;
  @basefontshadow();
}
.content-1 {
  background: url('/images/background/home_1_11.jpg');
  @basebackgroundimage();
  .basecontent();
  flex-direction: column;
  .content-1-title {
    display: flex;
    justify-content: center;
    flex: 1;
    flex-direction: column;
    align-items: center;
    h1 {
      margin-top: 5rem;
      display: flex;
      justify-content: center;
      flex: 1;
      font-weight: 700;
      color: rgba(255, 255, 255, 0.849);
      @basefontshadow();
    }
    h4 {
      display: flex;
      justify-content: center;
      flex: 3;
      // color: rgba(199, 190, 159, 0.801);
      color: aliceblue;
      font-size: 600;
      width: 50%;
      .desfont();
      .h4();
    }
  }
}
// 具体的介绍含导航栏
.content-introduce {
  .basecontent();
  // display: flex;
  // background: url('/images/background/home_1_9.jpg');
  background: url('/images/background/home_1_12.jpg');
  flex-direction: row;
  justify-content: center;
  align-items: center;
  @basebackgroundimage();
  // width: 80%;
  ul {
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: flex-end;
    .desfont();
    .deswhite();
    // justify-content: flex-start;
    li {
      // 取消光标效果改为箭头
      cursor: pointer;
      font-size: 30px;
    }
  }
  .right-content {
    display: flex;
    flex: 2;
    text-align: justify;
    // margin-left: 50px;
    h4 {
      padding: 100px;
      .desfont();
      .deswhite();
      .h4();
    }
  }
}
.content-introduce:fullscreen {
  background: red;
}
@keyframes content-fade-in {
  0% {
    opacity: 0.8;
  }
  100% {
    opacity: 1;
  }
}
// .fade-in-slow:hover {
//   // transform: translateY(0) translateY(500px);
//   // transition-duration: 1s;
//   // transition-delay: 0.5s;
//   // transition-timing-function: ease;
//   animation: 2s content-fade-in;
// }
// goals
.content-2 {
  // background: url('/images/background/home_1_2.jpg');
  background: url('/images/background/home_2_3.jpg');
  @basebackgroundimage();
  // TODO:[-] 20-03-06 里面嵌套了一层div了，在外侧的div使用副轴end对齐方式
  align-items: flex-end;
  .basecontent();
  .content-1-title {
    display: flex;
    flex-direction: row;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      align-items: center;
      color: aliceblue;
      @basefontshadow();
    }
    h4 {
      display: flex;
      flex: 2;
      align-items: center;
      color: aliceblue;
      width: 50%;
      // TODO:[*] 19-11-11暂时先加内间距
      padding: 100px;
      .desfont();
      .h4();
    }
  }
}
// mission
.content-3 {
  .basecontent();
  background: url('/images/background/home_1_3.jpg');
  @basebackgroundimage();
  .content-1-title {
    display: flex;
    flex-direction: column;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      color: aliceblue;
      align-items: center;
      @basefontshadow();
    }
    .minor_title {
      display: flex;
      flex: 1;
      // width: 70%;
      justify-content: center;
      color: aliceblue;
      h4 {
        width: 50%;
        .desfont();
        .h4();
      }
    }
  }
}
// area
.content-4 {
  // background: url('/images/background/home_1_5.jpg');
  background: url('/images/background/home_2_4.png');
  @basebackgroundimage();
  .basecontent();
  .content-1-title {
    display: flex;
    flex-direction: row;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      align-items: center;
      order: 2;
      color: aliceblue;
      @basefontshadow();
    }
    .minor_title {
      display: flex;
      flex: 1;
      // 交叉轴上的对齐方式
      align-items: center;
      h4 {
        display: flex;
        justify-content: center;
        flex: 1;
        order: 1;
        color: aliceblue;
        @basefontshadow();
        // TODO:[*] 19-11-11暂时先加内间距
        padding: 100px;
        .desfont();
        .h4();
      }
    }
  }
}

// 加入切换时的过度效果
// .tabcontent-enter-active,
// .tabcontent-leave-active {
//   transition: all 1s;
// }
// .tabcontent-enter,
// .tabcontent-leave-to {
//   opacity: 0;
//   transform: translateY(30px);
// }

.tabcontent-enter-active {
  animation: tabFade 1s;
}

@keyframes tabFade {
  0% {
    // background-color: yellow;
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
  }
}

// 0% {
//   background: black;
// }
// 100% {
//   background: red;
//   // opacity: 0;
//   // transform: translateY(30px);
// }
</style>
