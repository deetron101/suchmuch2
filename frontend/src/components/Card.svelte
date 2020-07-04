<script>
    export let title = "title";
    export let subtitle = "subtitle";
    export let subtitle_width = "w-56";
</script>

<style>
</style>

<div class="bg-light-peach rounded-lg shadow px-8 py-8">
    <h2 class="text-brown text-3xl font-bold mb-4">{title}</h2>
    <p class="{subtitle_width} text-brown text-sm mb-8">{subtitle}</p>
    <slot></slot>
</div>