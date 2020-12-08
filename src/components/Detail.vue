<template>
  <div class="detail">
    <div>
      <a class="goback" @click="goBack()">返回</a>
    </div>
    <div>
      <img :src="img">
    </div>
    <div>
      <p>介绍</p>
      <p>{{desc}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Detail',
  data () {
    return {
      img: '',
      desc: ''
    }
  },
  methods: {
    goBack: function(){
      this.$router.push('/home')
    },
    getDetail: function(id){
      axios.get('http://127.0.0.1:8000/detail/'+id).then(res=>{
        const data = res.data
        this.img = data.img
        this.desc = data.desc
      }).catch(error=>{
        console.log(error)
      })
    }
  },
  created: function(){
    this.getDetail(this.$route.params.id)
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
