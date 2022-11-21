<script>
export default {
    props: ['score'],
    computed: {
        last_review_grade() {
            if (this.score >= 50) {
                return 0;
            } else {
                return 1;
            }
        },
    }
};
</script>

<template>
    <span
        class="d-inline-flex align-items-center justify-content-center text-white rounded-circle ms-2 fs-6"
        style="height: 20px; width: 20px"
        :class="['bg-success', 'bg-danger'][last_review_grade]"
        :title="`You ${['passed', 'failed'][last_review_grade]} this review.`"
    >
        <i class="bi" :class="['bi-check', 'bi-x'][last_review_grade]"></i>
    </span>
</template>