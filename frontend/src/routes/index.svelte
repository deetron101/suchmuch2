<script>
  import Button from '../components/Button.svelte';
  import Card from '../components/Card.svelte';

</script>

<style>
</style>

<svelte:head>
	<title>Skeen</title>
</svelte:head>

<div class="bg-peach bg-no-repeat bg-right pt-16" style="height: 356px; background-image: url(images/stephanie-harvey-T0inbt7nRME-unsplash.png)">
  <h1 class="text-5xl text-center font-serif pb-8">Personalized skincare products search</h1>
  <p class="text-2xl text-center">Navigate the sea of skincare information</p>
</div>

<div style="max-width:1340px; margin: 0 auto">

<div class="px-16 pt-16">
  <h2 class="text-4xl font-serif font-bold pb-8">Get tailored product suggestions</h2>
  <p class="text-2xl">Find best skincare products for your skin</p>
</div>

<div class="px-16 pt-32">
  <h3 class="text-3xl font-serif font-bold pb-8">By skin type</h3>
  <div class="flex flex-wrap justify-between">
    <Card title="Normal" bg_image="images/scott-webb-GQD3Av_9A88-unsplash-1.png"/>
    <Card title="Dry" bg_image="images/scott-webb-GQD3Av_9A88-unsplash-2.png"/>
    <Card title="Combined" bg_image="images/scott-webb-GQD3Av_9A88-unsplash-3.png"/>
    <Card title="Oily" bg_image="images/scott-webb-GQD3Av_9A88-unsplash-4.png"/>
  </div>
</div>

<div class="px-16 pt-24">
  <h3 class="text-3xl font-serif font-bold pb-8">By skin goal</h3>
  <div class="flex flex-wrap justify-between">
    <Card title="Healthy"/>
    <Card title="Moisturized"/>
    <Card title="Even"/>
    <Card title="Matte"/>
  </div>
</div>

</div>