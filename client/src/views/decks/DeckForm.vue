<script>
import { h, ref } from "vue";
import Papa from "papaparse";

export default {
    props: ['existingDeck', 'existingCards', 'deckSubmit'],
    data() {
        return {
            loaded: false,
            deck: {},
            cards: [],
        }
    },
    created() {
        this.deck = this.existingDeck ?? {
            'name': ''
        };

        if (!this.existingCards) {
            this.addCard();
        } else {
            this.cards = this.existingCards.map(card => {
                return {
                    key: this.generateKey(),
                    ...card,
                }
            });
        }

    },
    methods: {
        generateKey() {
            return `card-${(Math.random() * 1000).toString().toString().replace('.', '')}`;
        },
        handleDeckSave(e) {
            e.preventDefault();
            this.deckSubmit(e.target);
        },
        openFileSelect() {
            this.$refs.csvFileSelect.click();
        },
        handleDeckImport(e) {
            const file = e.target.files[0];
            if (!file) {
                return;
            }

            Papa.parse(e.target.files[0], {
                header: true,
                worker: true,
                skipEmptyLines: true,
                complete: (results) => {
                    this.cards = results.data.map(card => {
                        return {
                            key: this.generateKey(),
                            id: '',
                            points: card.Points,
                            front: card.Front,
                            back: card.Back,
                        }
                    });
                    this.$store.commit("setMessage", "CSV imported successfully. Please review and save.");
                    if (!this.$refs.deckName.value) {
                        this.$refs.deckName.focus();
                    }
                },
                error: () => this.$store.commit("setMessage", "Could not process the CSV file.")
            });
        },
        handleDeckExport() {
            this.$store.dispatch('exportDeck', this.deck.id);
        },
        handleDeckDelete() {
            this.$store.dispatch('deleteDeck', this.deck.id);
        },
        addCard() {
            this.cards.push({
                key: this.generateKey(),
                id: '',
                points: '',
                front: '',
                back: '',
            });
        },
        removeCard(key) {
            if (this.cards.length == 1) {
                alert("At least one card is required.");
                return;
            }
            this.cards = this.cards.filter(card => card.key !== key);
        },
    }
};
</script>

<template>
    <form @submit="(e) => e.preventDefault()">
        <input type="file" class="d-none" @change="handleDeckImport" ref="csvFileSelect" accept=".csv" />
    </form>
    <form @submit="handleDeckSave">
        <input v-if="existingDeck" type="hidden" name="deck_id" v-model="deck.id">

        <div class="row">
            <div class="col-md-3">
                <div class="mb-3">
                    <input class="form-control" type="text" required name="name" placeholder="Name of the deck"
                        v-model="deck.name" maxlength="100" minlength="3" ref="deckName">
                </div>
            </div>
            <div class="col-md-9">
                <button class="btn btn-secondary pe-3 add-card me-1 mb-1" type="button" @click="addCard">
                    <i class="bi bi-plus"></i>
                    Add card to deck
                </button>
                <button class="btn btn-secondary pe-3 me-1 mb-1" type="submit">
                    <i class="bi bi-check"></i>
                    Save deck
                </button>

                <template v-if="existingDeck">
                    <button class="btn btn-secondary pe-3 me-1 mb-1" @click="handleDeckExport" type="button">
                        <i class="bi bi-file-earmark-spreadsheet"></i>
                        Export
                    </button>
                    <router-link class="btn btn-secondary pe-3 me-1 mb-1"
                        :to="{ name: 'decks.reviews.index', params: { deck_id: deck.id } }">
                        <i class="bi bi-card-checklist"></i>
                        Reviews
                    </router-link>
                    <button class="btn btn-danger pe-3 mb-1" @click="handleDeckDelete" type="button">
                        <i class="bi bi-trash"></i>
                        Delete
                    </button>
                </template>
                <template v-else>
                    <button class="btn btn-secondary pe-3 me-1 mb-1" @click="openFileSelect" type="button">
                        <i class="bi bi-file-earmark-spreadsheet"></i>
                        Import CSV
                    </button>
                </template>

            </div>
        </div>

        <div class="row mt-2">
            <div v-for="card in cards" :key="card.key" class="col-12 col-md-6 col-lg-4 col-xl-3 card-col pb-4">
                <div class="card">
                    <div class="card-body">
                        <p class="card-text m-0">
                        <div class="mb-3">
                            <input class="form-control" type="number" max="10" min="0" required name="score[]"
                                placeholder="Score multiplier (1-10)" v-model="card.points">
                        </div>
                        <div class="mb-3">
                            <textarea class="form-control" rows="2" required name="front[]" placeholder="Front side"
                                maxlength="100" v-model="card.front"></textarea>
                        </div>
                        <div class="mb-3">
                            <textarea class="form-control" rows="2" required name="back[]" placeholder="Back side"
                                maxlength="100" v-model="card.back"></textarea>
                        </div>
                        <input class="card_id" type="hidden" name="card_ids[]" :value="card.id">
                        </p>
                        <button class="card-link btn btn-outline-danger remove-card" type="button"
                            @click="() => { removeCard(card.key) }">Remove</button>
                    </div>
                </div>
            </div>
        </div>
    </form>
</template>