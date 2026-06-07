import random

class AnimeMangaPromptGenerator:
    def __init__(self):
        self.character_types = [
            "beautiful anime girl with confident expression",
            "cool anime boy with determined look",
            "elegant manga heroine in flowing dress",
            "powerful magical girl with glowing aura",
            "stealthy ninja with hidden weapons",
            "honorable samurai with sword",
            "cyberpunk anime hacker with neon visor",
            "fantasy anime mage with spellbook",
            "school anime student with backpack",
            "mysterious villain with dark cloak"
        ]
        
        self.hair_styles = [
            "long flowing pink hair with ribbons",
            "short spiky blue hair with lightning marks",
            "black twin-tails with flower accessories",
            "silver wavy hair reaching waist",
            "golden long hair glowing softly",
            "red short hair with flame tips",
            "purple braided hair with gems",
            "white messy hair with frost effects",
            "green ponytail with leaf decorations",
            "rainbow colored hair shimmering"
        ]
        
        self.eye_styles = [
            "large expressive blue eyes sparkling",
            "vibrant green eyes with butterfly patterns",
            "fiery red eyes glowing intensely",
            "golden anime eyes radiating light",
            "purple mysterious eyes with shadows",
            "heterochromatic eyes red and blue",
            "sparkling teal eyes with star reflections",
            "intense dark eyes with determination",
            "glowing pink eyes with magical aura"
        ]
        
        self.outfits = [
            "traditional Japanese school uniform with red bow",
            "fantasy armor with glowing runes and cape",
            "cyberpunk jacket with LED strips",
            "magical girl dress with wings and tiara",
            "black ninja outfit with hidden daggers",
            "ornate samurai armor with dragon designs",
            "casual streetwear with hoodie and sneakers",
            "witch costume with pointed hat and broom",
            "mecha pilot suit with control interface",
            "medieval fantasy robe with mystical symbols"
        ]
        
        self.backgrounds = [
            "cherry blossom trees in full spring bloom floating",
            "Tokyo cityscape at sunset with tall buildings",
            "mystical forest with floating magical particles",
            "futuristic cyberpunk street with neon signs",
            "ancient medieval castle ruins under storm clouds",
            "school rooftop at dusk with wind blowing",
            "magical academy classroom with floating books",
            "ninja village at night with lantern lights",
            "space station window view with stars",
            "traditional Japanese temple with red gates"
        ]
        
        self.art_styles = [
            "manga style with black and white ink lines, high contrast",
            "anime style with vibrant saturated colors",
            "shonen anime style with dynamic action lines",
            "shojo anime style with soft romantic aesthetics",
            "seinen anime style with detailed realistic proportions",
            "chibi style cute and simplified proportions",
            "cel shaded anime style with smooth gradients",
            "watercolor anime style with soft blending",
            "digital painting anime style with ultra high detail"
        ]
        
        self.lighting = [
            "soft golden hour lighting with warm tones",
            "dramatic shadows with high contrast",
            "neon lights glowing in purple and blue",
            "magical sparkles and particles floating around",
            "backlit by sunset with orange glow",
            "moonlight with soft blue glow",
            "volumetric lighting with light rays",
            "cinematic lighting with depth"
        ]
        
        self.extra_effects = [
            "flower petals swirling in wind",
            "energy aura surrounding character",
            "raindrops falling dramatically",
            "fire embers floating upward",
            "snow flakes gently falling",
            "light beams shining through clouds",
            "magic runes glowing in background"
        ]
    
    def generate_prompt(self):
        character = random.choice(self.character_types)
        hair = random.choice(self.hair_styles)
        eyes = random.choice(self.eye_styles)
        outfit = random.choice(self.outfits)
        background = random.choice(self.backgrounds)
        style = random.choice(self.art_styles)
        lighting = random.choice(self.lighting)
        effect = random.choice(self.extra_effects)
        
        prompt = f"Anime/manga style illustration of {character} with {hair} and {eyes}, wearing {outfit}, {background}. {style}, {lighting}. {effect}. High quality, detailed artwork, professional anime art masterpiece. Sharp focus, vibrant colors, dynamic composition, 8k resolution."
        
        return prompt


if __name__ == "__main__":
    generator = AnimeMangaPromptGenerator()
    print("=== ANIME/MANGA PROMPT ===")
    print(generator.generate_prompt())
    print()
    print("=== ANOTHER PROMPT ===")
    print(generator.generate_prompt())
