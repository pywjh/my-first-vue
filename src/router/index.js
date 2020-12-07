import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import My from '@/components/My'
import Order from '@/components/Order'
import Find from '@/components/Find'
import Detail from '@/components/Detail'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: '/',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/find',
      name: 'Find',
      component: Find
    },
    {
      path: '/my',
      name: 'My',
      component: My
    },
    {
      path: '/order',
      name: 'Order',
      component: Order
    },
    {
      path: '/detail:id',
      name: 'Detail',
      component: Detail
    }
  ]
})
