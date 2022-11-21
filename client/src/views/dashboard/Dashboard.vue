<script>
import Base from "../../layouts/base/Base.vue";
import DeckMinimal from "../../components/deck/DeckMinimal.vue";
import DynamicContent from "../../components/misc/DynamicContent.vue";

import API from "../../util/api";

export default {
    components: {
        Base,
        DynamicContent,
        DeckMinimal,
    },
    data() {
        return {
            loaded: false,
            decks: [],
        };
    },
    created() {
        this.$store.commit('setTitle', 'Dashboard');
        API.get('').then(dashboard => {
            this.loaded = true;
            this.decks = dashboard.decks;
        }).catch(() => { });
    }
};
</script>

<template>
    <Base :loaded="loaded">
        <h2 class="mb-4">Your progress</h2>
        <DynamicContent :loaded="loaded">
            <div class="row card-row">
                <div
                    v-if="!decks.length"
                    class="col"
                >No decks have been added yet. Add a deck to get started.</div>

                <div v-for="deck in decks" class="col-xs-12 col-md-6 col-xl-4 mb-2">
                    <DeckMinimal :deck="deck" />
                </div>
            </div>
        </DynamicContent>
    </Base>
</template> 