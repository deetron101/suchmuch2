<script>
  import Button from '../components/Button.svelte';
  export let title = "title";
  export let bg_image = "none";
</script>

<style>
</style>

<div class="border-solid border-2 border-primary-blue relative mb-8">
    <img src="{bg_image}" alt="{title}"/>
    <h2 class="text-primary-blue text-3xl font-bold serif text-center absolute w-full -mt-16">{title}</h2>
</div>