<script>
import DeckIcon from "./DeckIcon.vue";
import { fromNow } from "../../util/date";
export default {
    props: ['deck'],
    components: {
        DeckIcon,
    },
    methods: {
        fromNow
    }
};
</script>

<template>
    <div class="card">
        <div class="card-body pb-4">
            <h4 class="d-flex align-items-center">
                {{ deck.name }}
                <DeckIcon v-if="deck.last_review" :score="deck.last_review.score_percent" />
            </h4>
            <p class="mb-4">
                {{
                    deck.last_review ?
                        "Last reviewed " + fromNow(deck.last_review.taken_at) + " ago"
                        : 'Never reviewed'
                }}
                <br />Last score:
                <b>{{ deck.last_review ? deck.last_review.score_percent + "%" : 'Unavailable' }}</b>
            </p>
            <slot></slot>
        </div>
    </div>
</template>