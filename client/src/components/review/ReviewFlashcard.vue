<script>
export default {
    props: ['index', 'card', 'moveTo', 'isActive', 'isLast'],
    data() {
        return {
            difficultySelected: false,
        }
    },
    methods: {
        flipCard() {
            this.card.state = "flipped";
        },
        next() {
            if (this.$refs.difficulty.value == "none") {
                alert("Please select a difficulty level before proceeding.");
                return;
            }

            this.card.state = "closed";
            this.moveTo(this.index + 1);
        }
    }
};
</script>

<template>
    <div class="card border-0 text-white d-flex">
        <div class="card-body unopened d-flex flex-column align-items-center justify-content-between p-4"
            :class="{ visible: card.state == 'hidden' }">
            <p class="card-text m-0 d-flex flex-column justify-content-center flex-grow-1">
            <h1>?</h1>
            </p>
        </div>
        <div class="card-body front d-flex flex-column align-items-center justify-content-center p-4"
            :class="{ visible: card.state == 'shown' }">
            <p class="card-text m-0 d-flex flex-column justify-content-center flex-grow-1">
            <h3>#{{ index + 1 }}</h3>
            <h3>{{ card.front }}</h3>
            <p><b>{{ card.points }}x</b> multiplier</p>
            </p>
            <div class="card-text">
                <button class="btn btn-outline-light flip" type="button" @click="flipCard">
                    <i class="bi bi-arrow-repeat"></i>
                    Flip and check
                </button>
            </div>
        </div>
        <div class="card-body back d-flex flex-column align-items-center justify-content-between p-4"
            :class="{ visible: card.state == 'flipped' }">
            <p class="card-text m-0 d-flex flex-column justify-content-center flex-grow-1">
            <h5>{{ card.front }}</h5>
            <h3>{{ card.back }}</h3>
            <p class="mt-2 text-center">
                How difficult did you find this card?
                <select class="form-select m-2" aria-label="Default select example" name="difficulties[]"
                    ref="difficulty">
                    <option selected value="none">Select difficulty</option>
                    <option value="0">Couldn't recall it (0 points)</option>
                    <option value="1">Difficult ({{ card.points * 1 }} points)</option>
                    <option value="2">Moderate ({{ card.points * 2 }} points)</option>
                    <option value="3">Easy ({{ card.points * 3 }} points)</option>
                    <option value="4">Piece of cake ({{ card.points * 4 }} points)</option>
                </select>
                <input type="hidden" name="cards[]" :value="card.id">
            </p>
            <button v-if="isLast" class="btn btn-outline-light submit mt-4" type="submit">Submit <i
                    class="bi bi-check"></i></button>
            <button v-else class="btn btn-outline-light mt-4" type="button" @click="next">Next <i
                    class="bi bi-arrow-right"></i></button>
            </p>
        </div>
        <div class="card-body finished d-flex flex-column align-items-center justify-content-between p-4"
            :class="{ visible: card.state == 'closed' }">
            <p class="card-text m-0 d-flex flex-column justify-content-center flex-grow-1">
            <h5>{{ card.front }}</h5>
            <h3>{{ card.back }}</h3>
            <span class="fs-5 mt-3"><i class="bi bi-check"></i> Completed</span>
            </p>
        </div>
    </div>
</template>