<script>
	export let segment;
</script>

<style>

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

</style>

<nav>
	<ul>
		<li><a aria-current="{segment === undefined ? 'page' : undefined}" href="."><img alt="Skeen logo" src="logo.svg"/></a></li>
		<li><a aria-current="{segment === 'features' ? 'page' : undefined}" href="features">features</a></li>
		<li><a aria-current="{segment === 'technology' ? 'page' : undefined}" href="technology">technology</a></li>
		<li><a aria-current="{segment === 'about' ? 'page' : undefined}" href="about">about</a></li>
		<li><a aria-current="{segment === 'signin' ? 'page' : undefined}" href="signin">signin</a></li>
		<li><a aria-current="{segment === 'signup' ? 'page' : undefined}" href="signup">signup</a></li>
	</ul>
</nav>
