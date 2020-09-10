<script>
  import Button from '../components/Button.svelte';
  import Card from '../components/Card.svelte';
  import { stores } from '@sapper/app';
  import { onMount } from "svelte";

  let api_url = '';
  let products;

  const { session } = stores();
  session.subscribe(value => {
    api_url = value.API_URL;
  });

  onMount(async () => {
    await fetch(api_url.concat('products/moisturizers'))
      .then(r => r.json())
      .then(data => {
        products = data;
      });
  })

</script>

<style>
</style>

<svelte:head>
	<title>Skeen</title>
</svelte:head>

<div class="bg-top bg-no-repeat bg-primary-blue relative pt-16" style="height: 755px; background-image: url(images/sea-1.png)">
  <div class="absolute w-full bottom-0 pb-32">
    <h1 class="text-5xl text-center text-white font-serif pb-8">Personalized skincare products search</h1>
    <p class="text-2xl text-center text-white">Navigate the sea of skincare information</p>
  </div>
</div>

<div class="mx-48">
  <div class="mt-32">
    <h2 class="text-4xl text-center font-serif font-bold pb-8">Browse Products</h2>
  </div>

  <div class="mt-16">
    <h3 class="text-2xl font-serif font-bold pb-8">By skin type</h3>
    <div class="flex flex-wrap space-x-12">
      <Button label="Normal"/>
      <Button label="Dry"/>
      <Button label="Combination"/>
      <Button label="Oily"/>
      <Button label="Acne-prone"/>
    </div>
  </div>

  <div class="mt-20">
    <h3 class="text-2xl font-serif font-bold pb-8">By skin goal</h3>
    <div class="flex flex-wrap space-x-16">
      <Button label="Healthy"/>
      <Button label="Moisturized"/>
      <Button label="Even"/>
      <Button label="Matte"/>
    </div>
  </div>

  <div class="mt-16 text-right">
    <a class="mr-4 text-lg font-bold" href="/">Advanced Filters</a>
  </div>

  <div class="mt-32">
    <h2 class="text-4xl text-center font-serif font-bold pb-8">Moisturizers</h2>
    {#if products}
      {#each products as product}
        <Card header={product.brand} title={product.name} subtitle={product.platform}/>
      {/each}
    {:else}
      <p class="loading">Loading...</p>
    {/if}
  </div>

</div>