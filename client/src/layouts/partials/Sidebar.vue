<style scoped src="./Sidebar.css"></style>

<template>
    <nav class="mt-0">
        <div class="p-3 bg-white" style="width: 250px">
            <ul class="list-unstyled">
                <li>
                    <router-link :to="{ name: 'dashboard' }" class="nav-link link-dark rounded">
                        <i class="bi bi-speedometer2 me-2", id="dashboard"></i>
                        Dashboard
                    </router-link>
                </li>
                <li>
                    <router-link :to="{ name: 'decks.index' }" class="nav-link link-dark rounded">
                        <i class="bi bi-card-text me-2", id ="manage"></i>
                        Manage decks
                    </router-link>
                </li>
                <li class="border-top my-3 p-2 credit text-muted">&copy; 2022, QuickFlash</li>
            </ul>
        </div>
    </nav>
</template>