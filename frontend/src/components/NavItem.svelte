<script>
	export let segment;
	export let page;
	export let slug;
</script>

<style>
</style>

<li class="inline-block mr-16">
	<a class="block text-brown font-medium text-xs no-underline" aria-current="{segment === slug ? 'page' : undefined}" href="{slug}">
		{page}
		<slot></slot>
	</a>
</li>
