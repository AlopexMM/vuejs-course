<template>
    <div class="backdrop">
        <div class="modal">
            <p hidden id="id">{{ id }}</p>
            <div>
                <label for="product">Nombre: </label>
                <input type="text" id="product" name="product" v-if="product !== undefined" :value="product">
                <input type="text" id="product" name="product" v-else>
            </div>
            <div>
                <label for="brand">Marca: </label>
                <input type="text" id="brand" name="brand" v-if="brand !== undefined" :value="brand">
                <input type="text" id="brand" name="brand" v-else>
            </div>
            <div>
                <label for="price">Precio: $ </label>
                <input type="text" id="price" name="price" v-if="price !== undefined" :value="price">
                <input type="text" id="price" name="price" v-else>
            </div> 
            <div>
                <button @click="confirmButton">Confirmar</button>
                <button @click="cancelButton">Cancelar</button>
            </div>      
        </div>
    </div>
</template>

<script>

export default {
    el: '.backdrop',
    props: [ 'id', 'product', 'brand', 'price' ],
    methods: {
        confirmButton() {
            const id = parseInt(this.$el.querySelector('#id').innerText)
            const product = this.$el.querySelector('#product').value
            const brand = this.$el.querySelector('#brand').value
            const price = parseFloat(this.$el.querySelector('#price').value)
            this.$emit('confirm', id, product, brand, price)
        },
        cancelButton() {
            const id = parseInt(this.$el.querySelector('#id').innerText)
            this.$emit('cancel', id)
        }
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
    background: rgba(0,0,0,0.5)

}

.modal {
    width: 400px;
    padding: 20px;
    margin: 100px auto;
    background: #fff;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;

}

</style>