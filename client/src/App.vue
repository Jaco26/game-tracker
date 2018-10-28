<template>
  <div id="app">
    <div id="nav" class="row">
      <div class="f1">
         <router-link to="/">Home</router-link> 
      </div>
    </div>
    <div class="row">
      <app-sidebar height="600" width="200"></app-sidebar>
    </div>
  </div>
</template>

<script>
import appSidebar from '@/components/Sidebar';
import { mapActions } from 'vuex';
export default {
  data() {
    return {
      
    };
  },
  components: {
    appSidebar,
  },
  methods: {
    ...mapActions('cities', [
      'fetchCityCards',
    ]),
  },
  mounted() {
    this.fetchCityCards();
  }
} 
</script>


<style lang="scss">

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
 
.container {
  display: block;
  width: 100%;
}

.row {
  display: flex;
}

.column {
  display: flex;
  flex-direction: column;
}

.f1 {
  flex: 1;
  padding: .2em;
}

.f2 {
  flex: 2;
  padding: .2em;
}

.f3 {
  flex: 3;
  padding: .2em;
}

.f4 {
  flex: 4;
  padding: .2em;
}

.f5 {
  flex: 5;
  padding: .2em;
}

.t-center {
  text-align: center;
}

.bg-blue {
  background-color: #455e77;
}

.bg-purple {
  background-color: #7660a0;
}

.bg-beige {
  background-color: beige;
}

.blue {
  color: #455e77;
}

.purple {
  color: #7660a0;
}

.beige {
  color: beige;
}

</style>
