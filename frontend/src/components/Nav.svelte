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

	li {
		display: inline-block;
		float: left;
		margin-right: 5em;
	}

	.logo {
		padding-top: 5px;
	}

</style>

<nav class="pt-16 px-16">
	<ul>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === undefined ? 'page' : undefined}" href="."><img class="logo" alt="Skeen logo" src="logo.svg"/></a></li>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === 'features' ? 'page' : undefined}" href="features">Features</a></li>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === 'technology' ? 'page' : undefined}" href="technology">Technology</a></li>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === 'about' ? 'page' : undefined}" href="about">About</a></li>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === 'signin' ? 'page' : undefined}" href="signin">Sign in</a></li>
		<li><a class="text-brown font-medium text-xs no-underline" aria-current="{segment === 'signup' ? 'page' : undefined}" href="signup">Sign up</a></li>
	</ul>
</nav>
