<script>
import { mapMutations, mapState } from "vuex";
export default {
    computed: {
        ...mapState(['message'])
    },
    methods: {
        ...mapMutations(['setMessage']),
    }
};
</script>

<style scoped src="./Auth.css"></style>

<template>
    <div class="wrapper wrapper-auth">
        <main>
            <form method="POST">
                <h1 class="mb-4 text-center">
                    ⚡ Quick
                    <b>Flash</b>
                </h1>
                <div v-if="message" class="alert alert-secondary p-2 px-3 text-start">{{ message }}</div>
                <slot></slot>
                <p class="mt-5 mb-3 text-muted credit text-center">&copy; 2022, QuickFlash</p>
            </form>
        </main>
    </div>
</template>