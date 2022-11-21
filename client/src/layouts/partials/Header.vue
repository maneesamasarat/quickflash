<script>
import { mapState, mapActions } from 'vuex';
import API from '../../util/api';
export default {
    computed: {
        ...mapState({
            title: 'title',
            user: 'user'
        }),
    },
    methods: {
        ...mapActions(['logout']),
        handleLogout() {
            this.$store.dispatch('logout');
        }
    },

};
</script>

<template>
    <header class="p-3 border-bottom">
        <div class="container-fluid">
            <div class="d-flex flex-wrap align-items-center justify-content-between">
                <div>
                    <router-link
                        :to="{ name: 'dashboard' }"
                        class="d-inline-block text-dark text-decoration-none text-logo me-2"
                    >
                        <span>⚡ Quick</span>
                        <b>Flash</b>
                    </router-link>»
                    <span class="fs-6 ms-2">{{ title }}</span>
                </div>

                <div class="d-flex align-items-center">
                    <span>
                        Hello,
                        <b>{{ user.name }}</b>!
                    </span>
                    <button
                        class="btn btn-outline-secondary btn-sm align-items-center rounded ms-4"
                        @click="$store.dispatch('logout')"
                    >
                        Sign out
                        <i class="bi bi-box-arrow-right ms-2"></i>
                    </button>
                </div>
            </div>
        </div>
    </header>
</template>