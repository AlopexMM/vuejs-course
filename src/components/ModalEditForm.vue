<template>
    <div class="backdrop">
        <div class="modal">
            <div>
                <label for="product">Nombre: </label>
                <input type="text" name="product" v-if="name !== undefined" :value="product">
                <input type="text" name="product" v-else>
            </div>
            <div>
                <label for="brand">Marca: </label>
                <input type="text" name="brand" v-if="brand !== undefined" :value="brand">
                <input type="text" name="brand" v-else>
            </div>
            <div>
                <label for="price">Precio: $ </label>
                <input type="number" name="price" v-if="price !== undefined" :value="price">
                <input type="number" name="price">
            </div>        
        </div>
    </div>
</template>

<script>

export default {
    data() {
        props: [ product, brand, price ]
    }
}

</script>

<style scoped>

.backdrop {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: #000;

}

.modal {
    width: 400px;
    padding: 20px;
    margin: 100px auto;
    background: #fff;
    border-radius: 10px;
}
</style>