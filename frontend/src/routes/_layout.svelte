<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>

<style>
</style>

<div class="bg-light-peach text-md text-primary-blue font-sans tracking-wide">
	<Nav {segment}/>
	<main>
		<slot></slot>
	</main>
</div>
