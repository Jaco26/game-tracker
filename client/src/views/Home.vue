<template>
  <div class="home">
    <button @click="getItem">Get Item</button>
  </div>
</template>

<script>

export default {
  name: 'home',
  components: {

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
