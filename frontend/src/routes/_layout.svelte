<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>

<style>
</style>

<div>
	<Nav {segment}/>
	<main>
		<slot></slot>
	</main>
</div>
