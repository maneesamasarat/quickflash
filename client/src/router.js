import { createRouter, createWebHistory } from "vue-router";

const routes = [
    // Auth routes
    {
        path: "/login",
        name: "auth.login",
        component: () => import("./views/auth/Login.vue"),
    },
    {
        path: "/register",
        name: "auth.register",
        component: () => import("./views/auth/Register.vue"),
    },

    // Dashboard routes
    {
        path: "/",
        name: "dashboard",
        component: () => import("./views/dashboard/Dashboard.vue"),
    },

    // Decks routes
    {
        path: "/decks",
        name: "decks.index",
        component: () => import("./views/decks/Index.vue"),
    },
    {
        path: "/decks/:deck_id",
        name: "decks.show",
        component: () => import("./views/decks/Show.vue"),
    },
    {
        path: "/decks/create",
        name: "decks.create",
        component: () => import("./views/decks/Create.vue"),
    },

    // Reviews routes
    {
        path: "/decks/:deck_id/reviews",
        name: "decks.reviews.index",
        component: () => import("./views/reviews/Index.vue"),
    },
    {
        path: "/decks/:deck_id/reviews/:review_id",
        name: "decks.reviews.show",
        component: () => import("./views/reviews/Show.vue"),
    },
    {
        path: "/decks/:deck_id/reviews/create",
        name: "decks.reviews.create",
        component: () => import("./views/reviews/Create.vue"),
    },
];

const router = createRouter({
    history: createWebHistory("/"),
    routes,
});

export default router;
