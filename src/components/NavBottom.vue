<template>
  <div class="nav-bottom">
      <router-link to='/home'>
        <i class="iconfont iconiconfontzhizuobiaozhun023101"></i>
        <label>首页</label>
      </router-link>
      <router-link to='/find'>
        <i class="iconfont iconfaxian3"></i>
          <label>搜索</label>
      </router-link>
      <router-link to='/order'>
        <i class="iconfont icondingdan"></i>
        <label>订单</label>
      </router-link>
      <router-link to='/my'>
        <i class="iconfont iconwode1"></i>
        <label>我的</label>
      </router-link>
    </div>
</template>

<script>
export default {
  name: 'NavBottom'
}
</script>

<style scoped>
.active {
    color: red;
}
</style>