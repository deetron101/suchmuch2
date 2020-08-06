<script>
  import Button from '../components/Button.svelte';
  import Card from '../components/Card.svelte';

</script>

<style>
</style>

<svelte:head>
	<title>Skeen</title>
</svelte:head>

<div class="bg-top bg-no-repeat bg-blue-green bg-center relative pt-16" style="height: 755px; background-image: url(images/sea-1.png)">
  <div class="absolute w-full bottom-0 pb-32">
    <h1 class="text-5xl text-center text-white font-serif pb-8">Personalized skincare products search</h1>
    <p class="text-2xl text-center text-white">Navigate the sea of skincare information</p>
  </div>
</div>

<div style="max-width:1440px; margin: 0 auto">

<div class="px-32 pt-32">
  <h2 class="text-4xl text-center font-serif font-bold pb-8">Browse Products</h2>
</div>

<div class="px-32 pt-16">
  <h3 class="text-2xl font-serif font-bold pb-8">By skin type</h3>
  <div class="flex flex-wrap justify-between">
    <Button label="Normal"/>
    <Button label="Dry"/>
    <Button label="Combination"/>
    <Button label="Oily"/>
    <Button label="Acne-prone"/>
  </div>
</div>

<div class="px-32 pt-16">
  <h3 class="text-2xl font-serif font-bold pb-8">By skin goal</h3>
  <div class="flex flex-wrap justify-between">
    <Button label="Healthy"/>
    <Button label="Moisturized"/>
    <Button label="Even"/>
    <Button label="Matte"/>
    <Button label="No acne"/>
  </div>
</div>

</div>