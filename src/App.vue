<template>
  <div id="app">
    <!-- 动态路由视图展示 -->
    <router-view /> 
    <!-- 底部导航栏 -->
    <NavBottom/>
  </div>
</template>

<script>
import NavBottom from './components/NavBottom'

export default {
  name: "App",
  components: {
    NavBottom
  }
}
</script>

<style>
@import './assets/css/index.css'
</style>
