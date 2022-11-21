<script>
import Base from "../../layouts/base/Base.vue";
import Deck from "../../components/deck/Deck.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";

import API from "../../util/api";

export default {
    components: {
        Base,
        DynamicContent,
        Deck,
    },
    data() {
        return {
            loaded: false,
            decks: [],
        };
    },
    created() {
        this.$store.commit("setTitle", "Manage Decks");
        this.fetchData();
        this.$store.subscribeAction({
            after: action => {
                if (action.type === "deleteDeck") {
                    this.fetchData();
                }
            }
        });
    },
    methods: {
        fetchData() {
            API.get("decks").then(data => {
                this.loaded = true;
                this.decks = data.decks;
            }).catch(() => { });
        }
    }
};
</script>

<template>
    <Base>
        <h2 class="mb-4 d-flex align-items-center">
            Your decks
            <router-link
                class="btn btn-outline-secondary btn-sm ms-3"
                :to="{ name: 'decks.create' }"
            >
                <i class="bi bi-plus me-1"></i>
                Add new
            </router-link>
        </h2>
        <DynamicContent :loaded="loaded">
            <div class="row card-row">
                <div
                    v-if="!decks.length"
                    class="col"
                >No decks have been added yet. Add a deck to get started.</div>

                <div v-for="deck in decks" class="col-xs-12 col-md-6 col-xl-4 mb-2">
                    <Deck :deck="deck" :onDelete="fetchData" />
                </div>
            </div>
        </DynamicContent>
    </Base>
</template>