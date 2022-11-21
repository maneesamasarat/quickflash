<script>
export default {
    props: ['loaded']
};
</script>

<template>
    <slot v-if="loaded"></slot>
    <div v-else class="loading">
        <div class="progress-bar">
            <div class="progress-bar-value"></div>
        </div>
    </div>
</template>