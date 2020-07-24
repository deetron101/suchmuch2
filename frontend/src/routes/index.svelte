<script>
  import Button from '../components/Button.svelte';
  import Card from '../components/Card.svelte';
  const items = [
  {
    title: "Skin",
    subtitle: "Tell us about your skin and what it needs",
    subtitle_width: "w-40",
    button: {
      label: "Start with the skin quiz"
    },
    style: ""
  },
  {
    title: "Products",
    subtitle: "Choose products you already use to find new effective products",
    style: "flex-1"
  },
  {
    title: "Routines",
    subtitle: "Find routines that work for you and your skin",
    style: "flex-1"
  }
];
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

<div class="my-8 xs:w-full sm:w-full min-w-2/3">
  <Card {...items[0]} />
</div>

<div class="flex flex-wrap">
<Card {...items[1]} />
<Card {...items[2]} />
</div>