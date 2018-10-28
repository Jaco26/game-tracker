<template>
  <canvas @mousemove="isHotspot"  ref="canvas"></canvas>
</template>

<script>
import boardImgSRC from '../assets/pandemic-board.png';
import { mapState } from 'vuex'
export default {
  data() {
    return {
      hotspots: [],
      isOnCity: false,
      shouldEmitWhenOff: true,
    }
  },
  computed: {
    ...mapState('cities', [
      'cityCards',
    ]),
  },
  methods: {
    isHotspot(e) {
      const x = e.offsetX;
      const y = e.offsetY;
      this.hotspots.forEach(spot => {
        if (
          spot.x - spot.r < x 
          && spot.x + spot.r > x 
          && spot.y - spot.r < y
          && spot.y + spot.r > y
        ) {
          this.isOnCity = true;
        } else {
          this.isOnCity = false;
        }
        if (this.isOnCity) {
          this.$emit('onCity', spot.city);
          this.shouldEmitWhenOff = true;
        } else {
          if (this.shouldEmitWhenOff) {
            this.$emit('offCity');
            this.shouldEmitWhenOff = false;
          }
        }
      })
    },
    drawGrid(ctx) {
      const width = ctx.canvas.width;
      const height = ctx.canvas.height;
      const nXSlice = 50
      const nYSlice = 30;
      const xIncrement = width / nXSlice;
      const yIncrement = height / nYSlice;
      for (let i = 0; i < nXSlice; i++) {
        const num = i + 1
        const xStart = xIncrement * num;      
        ctx.beginPath();
        ctx.strokeStyle = 'black'
        ctx.moveTo(xStart, 0);
        ctx.lineTo(xStart, height);
        ctx.font = "15px Arial";
        ctx.strokeStyle = 'black';
        ctx.strokeText(num.toString(), xStart, 15);
        ctx.stroke();
      }

      for (let i = 0; i < nYSlice; i++) {
        const num = i + 1;
        const yStart = yIncrement * num;        
        ctx.beginPath();
        ctx.strokeStyle = 'black'
        ctx.moveTo(0, yStart);
        ctx.lineTo(width, yStart);
        ctx.font = "15px Arial";
        ctx.strokeStyle = 'black';
        ctx.strokeText(num.toString(), 5, yStart);
        ctx.stroke();
      }
    },
    setHotspot(x, y, r, city) {
      this.hotspots.push({x,y,r,city})
    },
    drawCanvas() {
      const canvas = this.$refs.canvas;    
      canvas.width = 850;
      canvas.height = 600;
      const ctx = canvas.getContext('2d');
      const boardImg2 = new Image()
      boardImg2.src = boardImgSRC;    
      boardImg2.onload = (e) => {
        ctx.drawImage(boardImg2, 0, 0, canvas.width, canvas.height)
        this.applyGameOverlay(ctx);
      }
    },
    applyGameOverlay(ctx) {
      const width = ctx.canvas.width;
      const height = ctx.canvas.height;
      this.cityCards.forEach(city => {
        const x = width / (city.x_rat_key / city.x_rat);
        const y = height / (city.y_rat_key / city.y_rat);        
        const r = 10;
        this.setHotspot(x, y, r, city);
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.strokeStyle = city.color;
        ctx.fillStyle = 'white';
        ctx.fillText(city.name, x , y - 15)
        ctx.stroke();
        ctx.closePath();
      });
    }
  },
  mounted() {
    if (this.cityCards.length) {
      this.drawCanvas();
    }
  },
  watch: {
    cityCards: {
      deep: true,
      handler(val) {
        this.drawCanvas()
        
      }
    }
  }
}
</script>

<style scoped>
/* .game-board {
  min-height: 600px;
} */
</style>
