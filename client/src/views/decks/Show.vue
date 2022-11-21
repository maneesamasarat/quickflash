<script>
import Base from "../../layouts/base/Base.vue";
import DeckForm from "./DeckForm.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";

import API from "../../util/api";

export default {
    components: {
        Base,
        DeckForm,
        DynamicContent
    },
    data() {
        return {
            loaded: false,
            deck: {},
            cards: [],
            deckId: this.$route.params.deck_id,
        }
    },
    created() {
        this.$store.commit('setTitle', 'Edit Deck');
        this.fetchData();
    },
    methods: {
        fetchData() {
            API.get(`decks/${this.deckId}`).then(data => {
                this.loaded = true;
                this.deck = data.deck;
                this.cards = data.cards;
            }).catch(() => { });
        },
        deckSubmit(form) {
            API.put(`decks/${this.deckId}`, new FormData(form)).then(() => {
                this.fetchData();
            }).catch(() => { });
        },
    }
};
</script>

<template>
    <Base>
        <h2 class="mb-4">
            {{ deck.name ?? "Edit Deck" }}
            <template
                v-if="cards.length > 0"
            >({{ cards.length }} cards)</template>
        </h2>
        <DynamicContent :loaded="loaded">
            <DeckForm :existingDeck="deck" :existingCards="cards" :deckSubmit="deckSubmit" />
        </DynamicContent>
    </Base>
</template>