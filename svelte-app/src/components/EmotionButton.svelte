<script lang="ts">
    export let emotion: string;
    export let selectedEmotions: string[];
    export let selectEmotion: (emotion: string) => void;

    // Colors for each emotion
    const colorMap: { [key: string]: string[] } = {
        Happiness: ["#FCF81D", "#EAE61B"],
        Relief: ["#F7F591", "#E2E085"],
        Awe: ["#FF7B25", "#ED7222"],
        Defiance: ["#FF6A6A", "#E76060"],
        Anger: ["#FF2626", "#E72222"],
        Gratitude: ["#F7F591", "#E2E085"],
        Courage: ["#F6F6BC", "#E5E5B1"],
        Triumph: ["#FC9959", "#EA8F53"],
        Regret: ["#F48989", "#DF7D7D"],
        Jealousy: ["#FF6A6A", "#E76060"],
        Surprise: ["#FFC85F", "#ECBA59"],
        Hope: ["#F5D494", "#E6C78B"],
        Apathy: ["#EAEAEA", "#D8D8D8"],
        Confusion: ["#CB9AF1", "#BE91E2"],
        Fear: ["#B96EF4", "#AC6BDF"],
        Passion: ["#F17ED2", "#DD74C1"],
        Longing: ["#F0A0DB", "#DC92C9"],
        Loss: ["#F2DDF6", "#DECAE2"],
        Betrayal: ["#8A8EED", "#7E82D9"],
        Despair: ["#4E54F3", "#494FE0"],
        Love: ["#F44BC6", "#E045B6"],
        Desire: ["#F17ED2", "#DD74C1"],
        Nostalgia: ["#EAC8F0", "#D4B6DA"],
        Melancholy: ["#4E54F3", "#494FE0"],
        Sadness: ["#0A2FF6", "#0A2AD9"],
    };
    $: color = colorMap[emotion][0];
    $: selectedColor = colorMap[emotion][1];

    // Set font size based on window and text size
    function getFontSize(emotion: string): string {
        return window.innerWidth <= 600 && emotion.length > 7
            ? "0.8em"
            : emotion.length > 9
            ? "1em"
            : "1.2em";
    }

    $: fontSize = getFontSize(emotion);
</script>

<button
    on:click={() => selectEmotion(emotion)}
    style="background-color: {selectedEmotions.includes(emotion)
        ? selectedColor
        : color}; font-size: {fontSize};"
    class="emotion-button {selectedEmotions.includes(emotion)
        ? 'selected'
        : ''}"
>
    {emotion}
</button>

<style>
    .emotion-button {
        width: 100%;
        height: 100%;
        cursor: pointer;
        outline: none;
        transition: background-color 0.3s, transform 0.3s;
        border-radius: 10px;
        color: white;
        will-change: transform;
        font-family: "Open Sans", sans-serif;
        font-weight: 700;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000,
            1px 1px 0 #000;
    }
    .emotion-button.selected {
        transform: rotate(5deg) scale(0.95);
    }
    @media (hover: hover) {
        .emotion-button:not(.selected):hover {
            transform: scale(1.05);
        }
    }
</style>
