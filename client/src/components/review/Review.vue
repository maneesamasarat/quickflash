<script>
import DeckIcon from "../deck/DeckIcon.vue";
import { fromNow } from "../../util/date";

export default {
    props: ["deck", "review"],
    components: { DeckIcon },
    methods: {
        fromNow,
        handleReviewDelete() {
            this.$store.dispatch("deleteReview", {
                deckId: this.deck.id,
                reviewId: this.review.id,
            });
        },
    },
};
</script>

<template>
    <div class="card">
        <div class="card-body pb-4">
            <h3 class="d-flex align-items-center">
                {{ deck.name }}
                <DeckIcon :score="review.score_percent" />
            </h3>
            <p class="mb-4">
                Taken {{ fromNow(review.taken_at) }} ago
                <br />
                Scored
                {{ review.score }}/{{ deck.max_score }} ({{ review.score_percent }}%)
            </p>

            <router-link
                class="btn btn-secondary btn-sm me-1"
                :to="{ name: 'decks.reviews.show', params: { deck_id: deck.id, review_id: review.id } }"
            >View report</router-link>

            <button
                class="btn btn-outline-danger btn-sm"
                type="button"
                @click="handleReviewDelete"
            >Delete</button>
        </div>
    </div>
</template>