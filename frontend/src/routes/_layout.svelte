<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>

<style>
</style>

<div class="text-m text-brown font-sans tracking-wide">
	<Nav {segment}/>
	<main>
		<slot></slot>
	</main>
</div>
