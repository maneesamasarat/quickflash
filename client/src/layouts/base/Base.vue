<script>
import { mapState, mapMutations } from "vuex";

import Header from "../partials/Header.vue";
import Sidebar from "../partials/Sidebar.vue";

export default {
    components: {
        Header,
        Sidebar
    },
    computed: {
        ...mapState(['message', 'user']),
        isAuthenticated() {
            return this.user;
        },
    },
    methods: mapMutations(['removeMessage']),
    beforeMount() {
        if (!this.isAuthenticated) {
            this.$router.replace({ name: 'login' });
        }
    },
};

</script>

<style scoped src="./Base.css"></style>

<template>
    <div v-if="isAuthenticated" class="wrapper wrapper-base">
        <Header />
        <main>
            <Sidebar />
            <div class="container p-3">
                <div v-if="message" class="alert alert-secondary alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" @click="removeMessage"></button>
                </div>

                <slot></slot>
            </div>
        </main>
    </div>
</template>