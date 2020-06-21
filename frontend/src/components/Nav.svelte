<script>
	export let segment;
</script>

<style>
	nav {
		font-weight: 300;
		padding: 0 1em;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	li {
		display: block;
		float: left;
	}

	[aria-current] {
		position: relative;
		display: inline-block;
	}

	[aria-current]::after {
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: rgb(255,62,0);
		display: block;
		bottom: -1px;
	}

	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}
</style>

<nav>
	<ul>
		<li><a aria-current="{segment === undefined ? 'page' : undefined}" href=".">skeen</a></li>
		<li><a aria-current="{segment === 'features' ? 'page' : undefined}" href="features">features</a></li>
		<li><a aria-current="{segment === 'technology' ? 'page' : undefined}" href="technology">technology</a></li>
		<li><a aria-current="{segment === 'about' ? 'page' : undefined}" href="about">about</a></li>
		<li><a aria-current="{segment === 'signin' ? 'page' : undefined}" href="signin">signin</a></li>
		<li><a aria-current="{segment === 'signup' ? 'page' : undefined}" href="signup">signup</a></li>
	</ul>
</nav>
