<script>
	import NavItem from '../components/NavItem.svelte';
	const navItems = [
	{
		page: "Features",
		slug: "features"
	},
	{
		page: "Technology",
		slug: "technology"
	},
	{
		page: "About",
		slug: "about"
	},
	{
		page: "Sign in",
		slug: "signin"
	},
	{
		page: "Sign up",
		slug: "signup",
		style: "bg-light-peach rounded-full"
	}
];
</script>

<style>
</style>

<nav class="pt-16 px-8">
	<ul class="flex flex-wrap flex-row">
		<NavItem segment page="" slug="/">
			<img alt="Skeen logo" src="logo.svg"/>
		</NavItem>
		{#each navItems as navItem}
		  	<NavItem segment {...navItem} />
		{/each}
	</ul>
</nav>