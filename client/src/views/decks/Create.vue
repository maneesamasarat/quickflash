<script>
import Base from "../../layouts/base/Base.vue";
import DeckForm from "./DeckForm.vue";
import API from "../../util/api";
export default {
    components: {
        Base,
        DeckForm
    },
    created() {
        this.$store.commit('setTitle', 'Create Deck');
    },
    methods: {
        deckSubmit(form) {
            API.put('decks', new FormData(form)).then(data => {
                this.$router.push({ name: 'decks.show', params: { deck_id: data.deck.id } });
            }).catch(() => { });
        }
    }
};
</script>

<template>
    <Base>
        <h2 class="mb-4">{{ "Add new deck" }}</h2>
        <DeckForm :deckSubmit="deckSubmit" />
    </Base>
</template>