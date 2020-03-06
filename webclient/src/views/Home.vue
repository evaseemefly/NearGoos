<template>
  <div class="my-root">
    <header>
      <div class="main-title">
        <!-- header 加几个logo -->
        <div class="logo">
          <!-- <img src="static/nf-logo.png"> -->
          <img src="/images/logo/nmefclog.png" />
          <img src="/images/logo/ioclog.png" />
        </div>
        <ul>
          <li><router-link :to="{ path: '/' }">Home</router-link></li>
          <li>
            <router-link :to="{ path: 'content/overview' }"
              >Overview</router-link
            >
          </li>
          <li>
            <router-link :to="{ path: '/content/data' }">Data</router-link>
          </li>
          <li>
            <router-link :to="{ path: '/content/product' }"
              >Services</router-link
            >
          </li>
        </ul>
      </div>
    </header>
    <div class="my-content">
      <div class="minor-title">
        <h2>NEAR-GOOS China RTDB</h2>
        <h4>
          North-East Asian Regional Global Ocean Observing System (NEAR-GOOS),
          China Real-Time Data Base, run by National Marine Environmental
          Forecasting Center (NMEFC)
        </h4>
        <!-- <button class="btn btn-default">Download Data</button> -->
        <button class="btn btn-default">
          <router-link :to="{ path: 'content' }">Download Data</router-link>
        </button>
      </div>
    </div>
    <footer>
      <!-- 选择成员国的友情链接 -->
      <div class="db-select">
        <div class="dropdown">
          <button
            class="btn btn-default dropdown-toggle"
            type="button"
            id="db"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="true"
          >
            Database
            <span class="caret"></span>
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
            <li><a href="#">China</a></li>
            <li><a href="#">Japan</a></li>
            <li><a href="#">Korea</a></li>
            <li><a href="#">Russia</a></li>
          </ul>
        </div>
      </div>
      <!-- 成员国 -->
      <div class="members">
        <h4>NEAR-GOOS Member Countries</h4>
        <div class="members-img">
          <img src="/images/logo/chn.jpg" />
          <img src="/images/logo/jap.jpg" />
          <img src="/images/logo/korea.jpg" />
          <img src="/images/logo/rus.jpg" />
        </div>
      </div>
      <!-- 版权 -->
      <div class="copyright">        
        <h4>All rights reserved by NMEFC</h4>
      </div>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'home',
  components: {
    HelloWorld,
  },
};
</script>

<style scoped lang="less">
@import '../styles/base.less';
.my-root {
  background: url('/images/background/home_3.png');
  background-size:100% auto;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  .my-content {
    display: flex;
    flex: 10;
    // transition: all 0.25s linear;
    // background: #7f9943;
    .minor-title {
      @minortitle();
      h4 {
        font-size: 1.7rem;
      }
      button {
        a {
          // text-decoration: none;
          // color: white;
          @alinkdefault();
        }
      }
    }
  }
}

.my-content ::before h2,
.my-content ::before h4 {
  transform: translate3d(0, -30%, 0) translate3d(0, -30px, 0);
  transition: all 0.25s linear;
  background: linear-gradient(
    to bottom,
    rgba(72, 76, 97, 0) 0%,
    rgba(72, 76, 97, 0.8) 75%
  );
}

.my-content:hover {
  // opacity: 0.2;
  background-color: rgba(174, 174, 185, 0.15);
  transition: all 1s linear;
}

.my-content:hover h2,
.my-content:hover h4 {
  transform: translate3d(0, -30%, 0) translate3d(0, -30px, 0);
  transition: all 0.25s linear;
  color: #ffffff;
  // transform: translate3d(0, 0, 0);
}

.my-content h2,
.my-content h4 {
  transform: translate3d(0, 0, 0) translate3d(0, 0, 0);
  transition: all 0.25s linear;
  color: #ffffff;
  // transform: translate3d(0, 0, 0);
}

.my-content:hover .minor-title {
  background: rgba(27, 144, 125, 0.411);
  transition: all 0.25s linear;
}
.my-content:hover .minor-title button {
  background: rgba(212, 132, 28, 0.815);
  transform: translate3d(0, 10%, 0) translate3d(0, 10px, 0);
  transition: all 0.25s linear;
}

// 沿主轴居中常量
@centered: {
  display: flex;
  justify-content: center;
};

// 含图片的背景
@basecontent: {
  //   height: 600px;
  //   display: flex;
};
// 所有的描述性文字的样式（主要是行高）
@desfont: {
  line-height: 1.8;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
  // color: #e9d14c;
};

footer {
  height: 100px;
  /* flex: 1; */
  //   background: darkcyan;
}

@minortitle: {
  display: flex;
  color: whitesmoke;
  // flex: row;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  font-size: 20px;
  font-size: 600;
  @basecontent();
  h2 {
    @desfont();
  }
  h4 {
    width: 50%;
    @desfont();
  }
  button {
    // background: rgba(212, 132, 28, 0.815);
    background: rgba(27, 107, 199, 0.815);
    color: white;
    font-size: 20px;
    transform: translate3d(0, 0, 0) translate3d(0, 0, 0);
    transition: all 0.25s linear;
  }
};

// header的父类
@header: {
  // div底图
  // 上面url tab
  // 中间居中title
  // 下面一个button
  //   background: url("image/home_1_2.jpg");
  // height: 100px;
  display: flex;
  flex: 2;
  flex-direction: column;
  //底部增加一个内padding
  padding-bottom: 50px;
  .logo {
    img {
      height: 100px;
    }
  }
  .main-title {
    display: flex;
    flex-direction: row;
    justify-content: center;
    color: wheat;
    font-weight: 700;
    font-size: 30px;
    align-items: center;
    // background: rgba(0, 0, 0, 0.1);
    // background: red;
    @baseheader();
    ul {
      display: flex;
      flex-direction: row;

      li {
        padding-right: 1em;
        // 去掉li的圆点
        list-style: none;
        a {
          color: white;
        }
      }
    }
  }
};
//footer的父类
@footer: {
  //   background: url("image/home_1_2.jpg");
  background: rgba(47, 221, 221, 0.329);
  display: flex;
  flex: 1;
  justify-content: space-around;
  align-items: center;
  .db-select {
    display: flex;
    flex: 1;
    @centered();
  }
  .members {
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
    h4 {
      color: white;
      @centered();
      @basefontshadow();
    }
    .members-img {
      @centered();
      img {
        margin-right: 0.25em;
      }
    }
  }
  .copyright {
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
    h4 {
      color: white;
      @basefontshadow();
    }
  }
};

// 定义的 白色的描述性字体
.deswhite() {
  color: aliceblue;
  font-size: 600;
}
header {
  // .header();
  // transform: translate3d(0, 0, 0) translate3d(0, 0, 0);
  // transition: all 0.25s linear;

  // animation-delay: 1s;
  @header();
}
header {
  .logo {
    animation: logoFadeIn 1.5s linear;
  }
  ul {
    animation: titleFadeIn 1.5s linear;
  }
}

@keyframes logoFadeIn {
  0% {
    opacity: 0;
  }
  25% {
    opacity: 0.25;
  }
  50% {
    opacity: 0.5;
  }
  75% {
    opacity: 0.75;
  }
}

@keyframes titleFadeIn {
  0% {
    opacity: 0;
    // transform: translate3d(0, -50%, 0);
    transform: translateY(-50%);
    // color: #ffffff;
  }
  25% {
    opacity: 0.25;
    // transform: translate3d(0, -37.5%, 0);
    transform: translateY(-37.5%);
    // color: #cabb36;
  }
  50% {
    opacity: 0.5;
    // transform: translate3d(0, -25%, 0);
    transform: translateY(-25%);
    // color: #3dac11;
  }
  75% {
    opacity: 0.75;
    // transform: translate3d(0, -12.5%, 0);
    transform: translateY(-12.5%);
    // color: #2c55da;
  }
}

header::before {
  transform: translate3d(0, -30%, 0) translate3d(0, -30px, 0);
  transition: all 0.25s linear;
}

footer {
  @footer();
  //   @footer();
}
</style>
