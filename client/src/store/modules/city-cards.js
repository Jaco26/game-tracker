import { api } from '@/services'

export default {
  namespaced: true,
  state: {
    cityCards: [],
  },
  mutations: {
    setCityCards(state, payload) {
      state.cityCards = payload;
    }
  },
  actions: {
    async fetchCityCards({ commit }) {
      try {
        const result = await api.getCityCards();
        commit('setCityCards', result);
      } catch (err) {
        console.log('ERROR IN fetchCityCards', err);
      }
    }
  }
}