<template>
  <div class="detail">
    <div>
      <a class="goback" @click="goBack()">返回</a>
    </div>
    <div>
      <img src="https://gma.alicdn.com/bao/uploaded/i4/46562752/O1CN01boSkKv1WCSbZP6a29_!!0-saturn_solar.jpg" alt="">
    </div>
    <div>
      <p>介绍</p>
      <p>具体信息</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Detail',
  data () {
    return {
    }
  },
  methods: {
    goBack: function(){
      this.$router.push('/home')
    },
    getDetail: function(id){
      axios.get('http://127.0.0.1:8000/detail/'+id).then(res=>{
        console.log(res)
      }).catch(error=>{
        console.log(error)
      })
    }
  },
  mounted: function(){
    this.getDetail(this.$router.params.id)
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
