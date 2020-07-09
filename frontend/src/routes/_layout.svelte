<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>

<style>
	main {
		padding: 3em 3em;
		position: relative;
		box-sizing: border-box;
	}
</style>

<div style="background-image: url(background.svg); background-repeat: no-repeat; background-size: cover;">
	<Nav {segment}/>
	<main>
		<slot></slot>
	</main>
</div>
