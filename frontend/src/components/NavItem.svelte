<script>
	export let segment;
	export let page;
	export let slug;
	export let outer_style;
	export let inner_style;
</script>

<style>
</style>

<li class="{outer_style} mr-6">
	<a class="{inner_style} inline-block py-3 px-8 font-medium text-brown text-xs no-underline" aria-current="{segment === slug ? 'page' : undefined}" href="{slug}">
		{page}
		<slot></slot>
	</a>
</li>
