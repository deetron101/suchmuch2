<script>
  import Button from '../components/Button.svelte';
  export let col_span = "col-span-1";
  export let title = "title";
  export let subtitle = "subtitle";
  export let subtitle_width = "w-56";
  export let button = null;
</script>

<style>
</style>

<div class="{col_span} relative bg-light-peach rounded-lg shadow px-8 py-8">
    <h2 class="text-brown text-3xl font-bold mb-4">{title}</h2>
    <p class="{subtitle_width} text-brown text-sm mb-8">{subtitle}</p>
    {#if button}
        <Button label="{button.label}"/>
    {/if}
</div>