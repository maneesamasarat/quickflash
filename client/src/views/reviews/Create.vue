<script>
import { mapState } from "vuex";
import Base from "../../layouts/base/Base.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";
import API from "../../util/api";
import ReviewFlashcard from "../../components/review/ReviewFlashcard.vue";

export default {
    components: {
        Base,
        DynamicContent,
        ReviewFlashcard
    },
    computed: mapState(["title"]),
    data() {
        return {
            loaded: false,
            deck: {},
            cards: [],
        }
    },
    created() {
        this.$store.commit('setTitle', 'Create review');
        API.get(`decks/${this.$route.params.deck_id}`).then(data => {
            this.loaded = true;
            this.deck = data.deck;
            this.cards = data.cards.map((card, index) => {
                return {
                    ...card,
                    state: index == 0 ? "shown" : "hidden", // hidden, shown, flipped, closed
                }
            });
            this.cards
            this.$store.commit('setTitle', `Review: ${this.deck.name}`);
        }).catch(() => { });
    },
    methods: {
        moveTo(index) {
            if (index < this.cards.length) {
                this.cards[index].state = "shown";
            }
        },
        handleReviewSubmit(e) {
            e.preventDefault();
            API.post(`decks/${this.$route.params.deck_id}/reviews`, new FormData(e.target))
                .then(data => {
                    this.$router.replace({ name: 'decks.reviews.show', params: { deck_id: this.deck.id, review_id: data.review.id } });
                }).catch(() => { });
        }
    }
};
</script>

<template>
    <Base>
        <h2 class="mb-4">{{ title }}</h2>
        <DynamicContent :loaded="loaded">
            <form class="row review" @submit="handleReviewSubmit">
                <div v-for="card, index in cards" class="col-4 card-col pb-4">
                    <ReviewFlashcard
                        :index="index"
                        :card="card"
                        :isLast="index == cards.length - 1"
                        :moveTo="moveTo"
                    />
                </div>
            </form>
        </DynamicContent>
    </Base>
</template>

<style src="../../components/review/ReviewFlashcard.scss"></style>