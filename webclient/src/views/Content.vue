<template>
  <div class="content">
    <Header></Header>
    <Center></Center>
    <Footer></Footer>
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

<style lang="less"></style>
