<script>
import Base from "../../layouts/base/Base.vue";
import DeckIcon from "../../components/deck/DeckIcon.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";
import { fromNow } from "../../util/date";
import API from "../../util/api";

export default {
    components: {
        DeckIcon,
        Base,
        DynamicContent
    },
    methods: {
        fromNow,
        handleReviewDelete() {
            this.$store.dispatch('deleteReview', {
                deckId: this.deck.id,
                reviewId: this.review.id,
            });
        },
    },
    data() {
        return {
            loaded: false,
            deck: {},
            review: {},
            reviewCards: [],
        };
    },
    created() {
        this.$store.commit('setTitle', 'Review report');
        API.get(`decks/${this.$route.params.deck_id}/reviews/${this.$route.params.review_id}`).then(data => {
            this.loaded = true;
            this.deck = data.deck;
            this.review = data.review;
            this.reviewCards = data.review_cards;
            this.$store.commit('setTitle', `${this.deck.name} - Review #${this.review.id}`);
        }).catch(() => { });

    },
};
</script>

<template>
    <Base>
        <DynamicContent :loaded="loaded">
            <h2>
                <router-link
                    :to="{ name: 'decks.reviews.index', params: { deck_id: deck.id } }"
                    class="btn btn-outline-secondary btn-sm me-1"
                >
                    <i class="bi bi-arrow-left m-2"></i>
                    Return to
                    <b>{{ deck.name }}</b> reviews
                </router-link>
                <router-link
                    :to="{ name: 'decks.reviews.create', params: { deck_id: deck.id } }"
                    class="btn btn-outline-secondary btn-sm me-1"
                >
                    Retry review
                    <i class="bi bi-arrow-right m-2"></i>
                </router-link>
            </h2>
            <h2 class="my-4 d-flex align-items-center">
                {{ deck.name }} - Review #{{ review.id }}
                <DeckIcon :score="review.score_percent"></DeckIcon>
                <button
                    @click="handleReviewDelete"
                    class="btn btn-outline-danger btn-sm ms-3"
                >
                    <i class="bi bi-trash me-1"></i>
                    Delete
                </button>
            </h2>
            <div
                class="alert mb-4"
                :class="review.score_percent >= 50 ? 'alert-success' : 'alert-danger'"
            >
                You took this review
                <b>{{ fromNow(review.taken_at) }} ago</b> and you
                scored
                <b>
                    {{ review.score }}/{{ review.max_score }} ({{
                        review.score_percent
                    }}%).
                </b>
                Hence, you {{ review.score_percent >= 50 ? 'passed' : 'failed' }} the review.
            </div>
            <div class="table-responsive">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Serial No.</th>
                            <th>Front</th>
                            <th>Back</th>
                            <th>Difficulty</th>
                            <th>Score</th>
                            <th>Remarks</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="reviewCard, index in reviewCards">
                            <td>{{ index + 1 }}</td>
                            <td>{{ reviewCard.card.front }}</td>
                            <td>{{ reviewCard.card.back }}</td>
                            <td>
                                {{
                                    ["Couldn't recall", "Difficult", "Moderate", "Easy", "Piece of cake"][reviewCard.difficulty]
                                }}
                            </td>
                            <td>
                                {{ reviewCard.score }}/{{ reviewCard.card.max_score }} ({{
                                    reviewCard.score_percent
                                }}%)
                            </td>
                            <td>
                                <DeckIcon :score="reviewCard.score_percent" />
                                <span
                                    class="ms-2"
                                >{{ reviewCard.score_percent >= 50 ? 'You\'re good to go!' : 'Work harder on this card.' }}</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </DynamicContent>
    </Base>
</template>