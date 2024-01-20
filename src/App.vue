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
          <button @click="editProduct(product.id)">Editar</button>
      </aside>
      <div v-if="product.edit"> <ModalEditForm :id="product.id" :product="product.product" :brand="product.brand" :price="product.price" @confirm="confirmEdit" @cancel="cancelEdit"/> </div>
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
          id: 1,
          product:"Cerveza Heineken 473 Ml",
          brand: "Heineken",
          image: require("./assets/CervezaHeineken473Ml.png"),
          price: 845,
          edit: false,
        },
        {
          id: 2,
          product: "Cerveza Corona 330 Ml",
          brand: "Corona",
          image: require("./assets/CervezaCoronaNoRetornable330Ml.png"),
          price: 840,
          edit: false,
        },
        {
          id: 3,
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
    editProduct(id){
      this.products.forEach((element) => {
        if (element.id == id) {
          element.edit = !element.edit
        }
      })
    },
    confirmEdit(id, product, brand, price) {
      this.products.forEach((element) => {
        if ( element.id === id) {
          element.product = product
          element.brand = brand
          element.price = price
          element.edit = !element.edit
        }
        
      })
    },
    cancelEdit(id) {
      this.products.forEach( element => {
        if(element.id === id) {
          console.log(element)
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
  font-size: 16px;
}

body {
    background: #eee;
    max-width: 980px;
    margin: 20px auto;
}

button {
    text-align: center;
    text-decoration: none;
    border: none;
    font-size: 16px;
    background-color: #367bf0;
    color: #fff;
    padding: 12px;
    border-radius: 4px;
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
