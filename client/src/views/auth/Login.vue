<script>
import Auth from "../../layouts/auth/Auth.vue";
import API from "../../util/api";
export default {
    components: {
        Auth,
    },
    created() {
        this.$store.commit("setTitle", "Login");
    },
    methods: {
        handleLogin(e) {
            e.preventDefault();
            API.post('auth/login', new FormData(e.target), false)
                .then(user => {
                    this.$store.dispatch('login', user);
                }).catch(() => { });
        },
    },
};
</script>

<template>
    <Auth>
        <form @submit="handleLogin">
            <div class="form-floating">
                <input
                    type="email"
                    class="form-control"
                    id="email"
                    name="email"
                    placeholder="Email"
                    required
                />
                <label for="email">Email</label>
            </div>
            <div class="form-floating mt-2">
                <input
                    type="password"
                    class="form-control"
                    id="password"
                    name="password"
                    placeholder="Password"
                    required
                />
                <label for="password">Password</label>
            </div>
            <button class="w-100 btn btn-lg btn-secondary mt-3" type="submit">Login</button>
            <router-link
                class="w-100 btn btn-link link-dark mt-3"
                :to="{ name: 'auth.register' }"
            >Create an account</router-link>
        </form>
    </Auth>
</template>