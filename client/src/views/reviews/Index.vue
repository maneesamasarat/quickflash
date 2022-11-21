<script>
import { mapState } from "vuex";

import Base from "../../layouts/base/Base.vue";
import Review from "../../components/review/Review.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";

import API from "../../util/api";

export default {
    components: {
        Base,
        Review,
        DynamicContent
    },
    data() {
        return {
            deck: {},
            reviews: []
        };
    },
    computed: mapState(['title']),
    created() {
        this.$store.commit("setTitle", "Reviews");
        this.fetchData();
        this.$store.subscribeAction({
            after: action => {
                if (action.type === "deleteReview") {
                    this.fetchData();
                }
            }
        });
    },
    methods: {
        fetchData() {
            API.get(`decks/${this.$route.params.deck_id}/reviews`).then(data => {
                this.loaded = true;
                this.deck = data.deck;
                this.reviews = data.reviews;
                this.$store.commit("setTitle", `${this.deck.name} - Reviews`);
            }).catch(() => { });
        }
    }
};
</script>

<template>
    <Base>
        <h2 class="mb-4">
            {{ title }}
            <router-link
                :to="{ name: 'decks.reviews.create', params: { deck_id: deck.id } }"
                class="btn btn-outline-secondary btn-sm ms-3"
            >
                <i class="bi bi-plus"></i>
                Review now
            </router-link>
        </h2>

        <DynamicContent :loaded="loaded">
            <div class="row">
                <div v-if="!reviews.length" class="col">No reviews for this deck yet.</div>
                <div v-for="review in reviews" class="col-12 col-md-6 col-xl-4">
                    <Review :deck="deck" :review="review" />
                </div>
            </div>
        </DynamicContent>
    </Base>
</template>