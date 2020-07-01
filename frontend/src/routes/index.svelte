<script>
  import Button from '../components/Button.svelte';
</script>

<style>
</style>

<svelte:head>
	<title>Skeen</title>
</svelte:head>

<div class="mx-auto max-w-md mb-16">
  <h1 class="text-xl text-brown leading-relaxed py-12">Skeen suggests skincare products and routines based on your personal skin profile</h1>
  <Button type='primary' label='Start with the skin quiz'/>
  <a class="text-sm font-bold px-8 text-brown" href="features">Learn more</a>
</div>

<div class="max-w-4xl rounded-lg shadow px-10 py-12 mb-8 bg-light-peach">
  <h2 class="text-3xl font-bold text-brown mb-4">Skin</h2>
  <p class="w-40 text-brown text-sm mb-8">
    Tell us about your skin and what it needs
  </p>
  <Button type='secondary' label='Start with the skin quiz'/>
</div>

<div class="grid grid-cols-2 gap-8">
<div class="max-w-4xl rounded-lg shadow px-10 py-12 mb-8 bg-light-peach">
  <h2 class="text-3xl font-bold text-brown mb-4">Products</h2>
  <p class="w-56 text-brown text-sm mb-8">
    Choose products you already use to find new effective products
  </p>
</div>

<div class="max-w-4xl rounded-lg shadow px-10 py-12 mb-8 bg-light-peach">
  <h2 class="text-3xl font-bold text-brown mb-4">Routines</h2>
  <p class="w-56 text-brown text-sm mb-8">
    Find routines that work for you and your skin
  </p>
</div>
</div>