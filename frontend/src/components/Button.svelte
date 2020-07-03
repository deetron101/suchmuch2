<script>
    export let type = 'primary';
    export let label;
</script>

<style>
</style>

{#if type == 'primary'}
<button class="bg-peach text-sm font-bold text-white py-4 px-12 rounded-full">{label}</button>
{:else}
<button class="bg-peach text-sm font-bold text-white py-4 px-12 rounded-full">{label}</button>
{/if}