import Vue from 'vue'
import Vuex from 'vuex'
import cities from './modules/city-cards'

Vue.use(Vuex)


const store = new Vuex.Store({
  modules: {
    cities,
  },
});

export default store;
