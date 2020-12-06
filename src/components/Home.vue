<template>
  <div>
    <!-- titlt -->
    <h1>{{msg}}</h1>
    <!-- head -->
    <div class="index-category">
      <div class="category" v-for="(list, i) in lists" :key="i">
        <i class="iconfont" :class="list.icon" :style="{background:list.color}"></i>
        <label>{{list.title}}</label>
      </div>
    </div>
    <!-- banner -->
    <div class="banner">
      <img src="@/assets/img/1.jpg">
      <div class="banner-circle">
        <ul>
          <li class="selected"></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: '首页',
      lists: [
        {title: '在线咨询', icon: 'iconfenlei', color: '#fa69b9'},
        {title: '产品介绍', icon: 'iconcruise-ship', color: '#ecbe35'},
        {title: '活动动态', icon: 'icondingdan', color: '#f60'},
        {title: '限时抢购', icon: 'iconcruise-ship', color: '#fa69b9'},
        {title: '今日秒杀', icon: 'iconcruise-ship', color: '#fa69b9'},
        {title: '领取优惠', icon: 'iconcruise-ship', color: '#fa69b9'},
        {title: '在线咨询', icon: 'iconcruise-ship', color: '#fa69b9'},
        {title: '在线咨询', icon: 'iconcruise-ship', color: '#fa69b9'},
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
