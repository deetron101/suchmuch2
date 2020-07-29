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

<div class="bg-peach bg-no-repeat bg-right pt-16 pb-40" style="background-image: url(stephanie-harvey-T0inbt7nRME-unsplash.png)">
  <h1 class="text-5xl text-brown text-center font-bold font-serif pb-2">Personalized skincare products search</h1>
  <p class="text-xl text-brown text-center">Navigate the sea of skincare information</p>
</div>

<div class="my-8 xs:w-full sm:w-full min-w-2/3">
  <Card {...items[0]} />
</div>

<div class="flex flex-wrap">
<Card {...items[1]} />
<Card {...items[2]} />
</div>