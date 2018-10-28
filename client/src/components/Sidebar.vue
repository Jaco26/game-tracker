<template>
  <section :style="`min-height: ${height}px; min-width: ${width}px;`" class="beige bg-blue" id="sidebar">
    <div class="column">
      <h1 class="f1">Hello</h1>
      <div class="f1">
         <button @click="loadGame">Load Game</button>
      </div>
      <div class="f1">
        <button @click="newGame">New Game</button>
      </div>
    </div>   
  </section>
</template>

<script> 
export default {
  props: {
    height: String,
    width: String,
  },
  methods: {
    loadGame() {

    },
    newGame() {

    }
  }
}
</script>


<style scoped>

/* #sidebar {
  min-width: 400px;
  padding: 1em;
} */

</style>
