<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <h1>Welcome to VueJS!!!! <span>&#128512;</span></h1>

  <ul>
    <li v-for="product in products" >
      <img :src="product.image" :alt="product.product">
      <aside>
          <h2>{{ product.product }} </h2>
          <h3>{{ product.brand }}</h3>
          <h3>$ {{ product.price }}</h3>
          <button @click="editProduct(product.product)">Editar</button>
      </aside>
      <div v-if="product.edit"> <ModalEditForm /></div>
    </li>
  </ul>

</template>

<script>
import ModalEditForm from './components/ModalEditForm.vue';

export default {

  name: 'App',
  data() {
    return {
      products: [
        {
          product:"Cerveza Heineken 473 Ml",
          brand: "Heineken",
          image: require("./assets/CervezaHeineken473Ml.png"),
          price: 845,
          edit: false,
        },
        {
          product: "Cerveza Corona 330 Ml",
          brand: "Corona",
          image: require("./assets/CervezaCoronaNoRetornable330Ml.png"),
          price: 840,
          edit: false,
        },
        {
          product: "Cerveza Grolsch 925 Ml",
          brand : "Grolsch",
          image : require("./assets/CervezaGrolschRetornable925Ml.png"),
          price: 1571.25,
          edit: false,
        }
      ],
    }
  },
  components: {
    ModalEditForm
},
  methods: {
    editProduct(product){
      console.log(product)
      this.products.forEach((element) => {
        if (element.product == product) {
          element.edit = !element.edit
        }
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
    background: #eee;
    max-width: 980px;
    margin: 20px auto;
}
p, h3, ul {
    margin: 0;
    padding: 0;
}
ul {
    display: flex;
    justify-content: space-between;
}
li {
    list-style-type: none;
    background: #fff;
    margin: 20px 20px;
    padding: 10px 20px;
    border-radius: 20px;
    display: flex;
    /* flex-direction: column; */
    align-items: center;
    justify-content: space-between;
}

li > img {
    width: 100px;
}

li > aside {
    margin: auto 20px;
}

li.fav {
    background: #FFFDAD;
}
</style>
