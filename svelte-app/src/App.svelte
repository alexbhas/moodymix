<script>
	import EmotionGrid from "./components/EmotionGrid.svelte";

	// Emotions
	let emotions = [
		"Happiness",
		"Relief",
		"Awe",
		"Defiance",
		"Anger",
		"Gratitude",
		"Courage",
		"Triumph",
		"Regret",
		"Jealousy",
		"Surprise",
		"Hope",
		"Apathy",
		"Confusion",
		"Fear",
		"Passion",
		"Longing",
		"Loss",
		"Betrayal",
		"Despair",
		"Love",
		"Desire",
		"Nostalgia",
		"Melancholy",
		"Sadness",
	];
	let selectedEmotions = [];
	let genre = "poppunk"; // Default genre (for now)
	let songs = [];

	let isLoading = false;

	// Request songs based on the emotions
	async function fetchSongs() {
		isLoading = true;
		const response = await fetch("/songs", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				emotions: selectedEmotions,
				genre: genre,
			}),
		});
		songs = await response.json();
		isLoading = false;
	}

	// Selecting an emotion in the grid, update the list
	function selectEmotion(emotion) {
		const index = selectedEmotions.indexOf(emotion);
		if (index === -1) {
			selectedEmotions = [...selectedEmotions, emotion];
		} else {
			selectedEmotions = [
				...selectedEmotions.slice(0, index),
				...selectedEmotions.slice(index + 1),
			];
		}
	}
</script>

<div class="container">
	<h1 class="title">Moodymix</h1>
	<EmotionGrid {emotions} {selectedEmotions} {selectEmotion} />
	<button
		class="get-songs-button {isLoading ? 'loading' : ''}"
		on:click={fetchSongs}
		disabled={isLoading}
	>
		Get Songs
	</button>
	<ul>
		{#each songs as song (song.id)}
			<li>
				<iframe
					title="Song"
					style="border-radius:12px"
					src="https://open.spotify.com/embed/track/{song.spotify}?utm_source=generator&theme=0"
					width="100%"
					height="152"
					frameBorder="0"
					allowfullscreen=""
					allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
					loading="lazy"
				/>
			</li>
		{/each}
	</ul>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 100vh;
	}
	.get-songs-button {
		margin-top: 50px;
		padding: 15px 30px;
		border: none;
		border-radius: 10px;
		background-color: #ccc;
		cursor: pointer;
		outline: none;
		transition: transform 0.5s;
		color: white;
		font-family: "Open Sans", sans-serif;
		font-weight: 700;
		text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000,
			1px 1px 0 #000;
	}
	.get-songs-button:hover {
		transform: scale(1.1);
	}
	.get-songs-button.loading {
		animation: spin 2s infinite linear;
		pointer-events: none;
		transform-origin: center;
	}
	@keyframes spin {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}
	.title {
		font-family: "Open Sans", sans-serif;
		font-weight: 700;
		color: white;
		text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000,
			1px 1px 0 #000;
		font-size: 3em;
		text-align: center;
		margin-top: 50px;
	}
	@media (max-width: 600px) {
		.container {
			padding: 20px;
		}
		.title {
			font-size: 2em;
		}
		.get-songs-button {
			margin-top: 50px;
			padding: 10px 20px;
		}
	}
	ul,
	li {
		padding: 0;
		margin: 0;
		list-style: none;
		text-align: center;
	}
</style>
