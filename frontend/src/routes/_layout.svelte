<script>
	import Nav from '../components/Nav.svelte';

	export let segment;
</script>

<style>
	main {
		padding: 3em 3em;
		position: relative;
		background-color: white;
		box-sizing: border-box;
	}
</style>

<Nav {segment}/>

<main>
	<slot></slot>
</main>