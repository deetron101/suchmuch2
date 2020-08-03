<script>
	export let segment;
	export let page;
	export let slug;
</script>

<style>
</style>

<li>
	<a class="p-4 mx-8 text-brown text-s uppercase" aria-current="{segment === slug ? 'page' : undefined}" href="{slug}">
		{page}
		<slot></slot>
	</a>
</li>
