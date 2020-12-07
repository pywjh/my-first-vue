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
    <!-- list -->
    <div class="index-main">
      <ul>
        <li class="lists" v-for="(item, i) in items" :key="i">
          <router-link :to="'/detail/'+item.id">
            <img :src="item.img" width='150' heigth='150'>
          </router-link>
          <label>
            <b class="discount">折扣价：{{item.product_uprice}}</b>
            <span class="price-text">原价：{{item.product_price}}</span>
          </label>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
      ],
      items: []
    }
  },
  methods: {
    getLists: function(){
      axios.get('http://127.0.0.1:8000/list').then(res=>{
        this.items = res.data
      }).catch(error=>{
        console.log(error)
      })
    }
  },
  created: function(){
    this.getLists()
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
