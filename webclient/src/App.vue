<template>
  <div id="app">
    <router-view></router-view>
    <!-- TODO:[-] 19-11-27 由于首页的header与footer无法与其他页面的服用，所以在入口页面直接加入路由跳转 -->
    <!-- <Header></Header>
    <Center></Center>
    <Footer></Footer> -->
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Header from "@/views/header/Header.vue";
import Center from "@/views/center/Center.vue";
import Footer from "@/views/footer/Footer.vue";

@Component({
  components: {
    Header,
    Center,
    Footer
  }
})
export default class App extends Vue {}
</script>

<style lang="less">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // margin-top: 60px;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}
</style>
