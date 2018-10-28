<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <button @click="getItem">Get Item</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  },
  methods: {
    async getItem() {      
      const item = await this.$api.get('/citycards')
        .then(res => res.data)
        .catch(err => err);

      console.log(item);
      
    }
  }
}
</script>
