<script>
	import NavItem from '../components/NavItem.svelte';
	export let segment;

	const navItems = [
	{
		page: "Mission",
		slug: "mission"
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
		page: "Contact Us",
		slug: "contact"
	}
];
</script>

<style>
</style>

<nav class="pt-24 px-8">
	<div class="flex justify-center">
		<a class="p-4" href="/">
			<img class="h-8" alt="Skeen logo" src="logo.svg"/>
		</a>
	</div>
	<ul class="flex flex-wrap justify-center pt-20 pb-10">
		{#each navItems as navItem}
		  	<NavItem {segment} page={navItem.page} slug={navItem.slug}  />
		{/each}
	</ul>
</nav>