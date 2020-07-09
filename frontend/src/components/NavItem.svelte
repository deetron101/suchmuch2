<script>
	export let segment;
	export let page;
	export let slug;
	export let style;
</script>

<style>
</style>

<li>
	<a class="{style} inline-block py-3 px-8 font-medium text-brown text-xs no-underline" aria-current="{segment === slug ? 'page' : undefined}" href="{slug}">
		{page}
		<slot></slot>
	</a>
</li>
