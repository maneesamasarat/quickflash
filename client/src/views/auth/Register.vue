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
        handleRegister(e) {
            e.preventDefault();
            API.post('auth/register', new FormData(e.target), false)
                .then(user => {
                    this.$store.dispatch('login', user);
                }).catch(() => { });
        },
    },
};
</script>

<template>
    <Auth>
        <form @submit="handleRegister">
            <div class="form-floating">
                <input
                    type="text"
                    class="form-control"
                    id="text"
                    name="name"
                    placeholder="Name"
                    required
                    maxlength="100"
                />
                <label for="name">Name</label>
            </div>
            <div class="form-floating mt-2">
                <input
                    type="email"
                    class="form-control"
                    id="email"
                    name="email"
                    placeholder="Email"
                    required
                    maxlength="100"
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
                    maxlength="100"
                />
                <label for="password">Password</label>
            </div>
            <button class="w-100 btn btn-lg btn-secondary mt-3" type="submit">Create account</button>
            <router-link
                class="w-100 btn btn-link link-dark mt-3"
                :to="{ name: 'auth.login' }"
            >Back to login</router-link>
        </form>
    </Auth>
</template>