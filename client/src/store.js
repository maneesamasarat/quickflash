import { createStore } from "vuex";
import router from "./router";
import API from "./util/api";

const loadUser = () => {
    return JSON.parse(localStorage.getItem("user") ?? "{}");
};

export default createStore({
    state() {
        return {
            title: "QuickFlash",
            message: null,
            user: loadUser(),
        };
    },
    getters: {
        user: loadUser,
    },
    actions: {
        login(store, user) {
            store.commit("removeMessage");
            store.commit("setUser", user);
            router.replace({ name: "dashboard" });
        },
        async logout(store) {
            store.commit("removeMessage");
            await router.replace({ name: "auth.login" });
            store.commit("setUser", {});
            store.commit("setMessage", `Logged out successfully.`);
        },

        async deleteDeck(store, deckId) {
            if (!confirm("Are you sure you want to delete this deck?")) {
                return;
            }

            await API.delete(`decks/${deckId}`);

            router.replace({
                name: "decks.index",
            });
        },

        async exportDeck(store, deckId) {
            await API.get(`decks/${deckId}/export`);
        },

        async deleteReview(store, { deckId, reviewId }) {
            if (!confirm("Are you sure you want to delete this review?")) {
                return;
            }

            await API.delete(`decks/${deckId}/reviews/${reviewId}`);

            router.replace({
                name: "decks.reviews.index",
                params: {
                    deck_id: deckId,
                },
            });
        },
    },
    mutations: {
        setTitle(store, title) {
            document.title = `${title} - QuickFlash`;
            store.title = title;
        },

        // Messages
        setMessage(store, message) {
            store.message = message;
        },
        removeMessage(store) {
            store.message = null;
        },

        // User
        setUser(store, user) {
            store.user = user;
            localStorage.setItem("user", JSON.stringify(user));
        },
    },
});
