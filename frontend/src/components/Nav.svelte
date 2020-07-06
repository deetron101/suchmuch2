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
		<NavItem segment page="." slug="">
			<img alt="Skeen logo" src="logo.svg"/>
		</NavItem>
		<NavItem segment page="Features" slug="features"/>
		<NavItem segment page="Technology" slug="technology"/>
		<NavItem segment page="About" slug="about"/>
		<NavItem segment page="Sign in" slug="signin"/>
		<NavItem segment page="Sign up" slug="signup"/>
	</ul>
</nav>