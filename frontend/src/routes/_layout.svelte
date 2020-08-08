<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>

<style>
</style>

<div class="bg-light-peach text-md text-primary-blue font-sans tracking-wide">
	<header>
		<Nav {segment}/>
	</header>
	<main>
		<slot></slot>
	</main>
	<footer>
		<div class="bg-left-48 bg-no-repeat bg-primary-blue relative" style="height: 466px; background-image: url(images/sea-2.png)">
			<div class="absolute w-full bottom-0 pb-32">
    			<h2 class="text-4xl text-center text-white font-serif pb-8">Personalized skincare products search</h2>
				<p class="text-2xl text-center text-white">Navigate the sea of skincare information</p>
			</div>
		</div>
	</footer>
</div>
