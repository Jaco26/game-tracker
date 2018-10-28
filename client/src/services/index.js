import axios from 'axios'

const myAxios = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

export const api = {
  getCityCards() {
    return myAxios.get('/citycards')
      .then(res => res.data)
      .catch(err => err);
  }
}