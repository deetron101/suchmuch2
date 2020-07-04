<script>
  import Button from '../components/Button.svelte';
  import Card from '../components/Card.svelte';
</script>

<style>
</style>

<svelte:head>
	<title>Skeen</title>
</svelte:head>

<div class="mx-auto max-w-md mb-16">
  <h1 class="text-xl text-brown leading-relaxed py-12">Skeen suggests skincare products and routines based on your personal skin profile</h1>
  <Button label='Start with the skin quiz'/>
  <a class="text-sm font-bold px-8 text-brown" href="features">Learn more</a>
</div>

<div class="max-w-4xl mb-8">
  <Card title="Skin" subtitle="Tell us about your skin and what it needs" subtitle_width="w-40">
    <Button label='Start with the skin quiz'/>
  </Card>
</div>

<div class="grid grid-cols-2 gap-8">
  <Card title="Products" subtitle="Choose products you already use to find new effective products"/>
  <Card title="Routines" subtitle="Find routines that work for you and your skin"/>
</div>