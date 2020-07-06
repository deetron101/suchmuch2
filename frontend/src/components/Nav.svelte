<script>
	import NavItem from '../components/NavItem.svelte';
</script>

<style>
	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

</style>

<nav class="pt-16 px-16">
	<ul>
		<NavItem segment page=".">
			<img alt="Skeen logo" src="logo.svg"/>
		</NavItem>
		<NavItem segment page="Features"/>
		<NavItem segment page="Technology"/>
		<NavItem segment page="About"/>
		<NavItem segment page="Sign in"/>
		<NavItem segment page="Sign up"/>
	</ul>
</nav>