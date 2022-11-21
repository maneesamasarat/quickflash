<script>
import DeckBase from "./DeckBase.vue";
export default {
    props: ['deck', 'onDelete'],
    components: {
        DeckBase,
    },
    methods: {
        handleDeckDelete() {
            this.$store.dispatch('deleteDeck', this.deck.id);
        },
    }
};
</script>

<template>
    <DeckBase :deck="deck">
        <router-link
            class="btn btn-secondary btn-sm me-1 mb-2"
            type="button"
            :to="{ name: 'decks.reviews.create', params: { deck_id: deck.id } }"
        >Review now</router-link>

        <router-link
            class="btn btn-outline-secondary btn-sm me-1 mb-2"
            type="button"
            :to="{ name: 'decks.reviews.index', params: { deck_id: deck.id } }"
        >Past reviews</router-link>

        <router-link
            class="btn btn-outline-secondary btn-sm me-1 mb-2"
            type="button"
            :to="{ name: 'decks.show', params: { deck_id: deck.id } }"
        >View/Edit</router-link>

        <button class="btn btn-outline-danger btn-sm mb-2" @click="handleDeckDelete">Delete</button>
    </DeckBase>
</template>

            