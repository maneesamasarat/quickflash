<script>
import DeckBase from "./DeckBase.vue";
export default {
    props: ['deck'],
    components: {
        DeckBase,
    }
};
</script>

<template>
    <DeckBase :deck="deck">
        <router-link
            class="btn btn-secondary btn-sm me-1 mb-2"
            type="button"
            :to="{
                name: 'decks.reviews.create',
                params: {
                    deck_id: deck.id
                }
            }"
        >Review now</router-link>
        <router-link
            class="btn btn-outline-secondary btn-sm mb-2"
            type="button"
            :to="{
                name: 'decks.reviews.index',
                params: {
                    deck_id: deck.id
                }
            }"
        >Past reviews</router-link>
    </DeckBase>
</template>