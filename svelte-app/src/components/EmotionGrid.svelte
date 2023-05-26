<script lang="ts">
    import EmotionButton from "./EmotionButton.svelte";
    export let emotions: string[];
    export let selectedEmotions: string[];
    export let selectEmotion: (emotion: string) => void;
</script>

<div class="grid">
    {#each emotions as emotion (emotion)}
        <div class="grid-item">
            <EmotionButton {emotion} {selectedEmotions} {selectEmotion} />
        </div>
    {/each}
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
        gap: 5px;
        width: 600px;
        background-color: black;
        border-radius: 15px;
        padding: 15px;
    }

    .grid-item {
        aspect-ratio: 1 / 1;
    }
    @media (max-width: 600px) {
        .grid {
            width: 100%;
            grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
        }
    }
</style>
