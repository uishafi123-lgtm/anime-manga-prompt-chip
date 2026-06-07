import random

class AnimeMangaPromptGenerator:
    """Generates anime/manga style art prompts for AI image generators"""
    
    def __init__(self):
        self.character_types = [
            "anime girl", "anime boy", "manga heroine", "manga hero",
            "shonen protagonist", "shojo heroine", "seinen warrior", "magical girl",
            "cyberpunk anime character", "fantasy anime mage", "school anime student",
            "villain anime character", "mecha pilot", "ninjas", "samurai"
        ]
        
        self.hair_styles = [
            "long pink flowing hair", "short blue spiky hair", "black twin-tails",
            "silver wavy hair", "golden long hair", "red short hair",
            "purple braided hair", "white messy hair", "green ponytail",
            "rainbow colored hair", "black bob cut", "blonde curly hair"
        ]
        
        self.eye_styles = [
            "large expressive blue eyes", "vibrant green eyes", "fiery red eyes",
            "golden anime eyes", "purple mysterious eyes", "heterochromatic eyes",
            "sparkling teal eyes", "intense dark eyes", "glowing pink eyes"
        ]
        
        self.outfits = [
            "Japanese school uniform", "fantasy armor with runes", "cyberpunk jacket",
            "magical girl dress", "ninja outfit", "samurai armor",
            "casual streetwear", "witch costume", "mecha pilot suit",
            "medieval fantasy robe", "modern hoodie and jeans", "battle gear"
        ]
        
        self.backgrounds = [
            "cherry blossom trees in spring", "Tokyo cityscape at sunset",
            "mystical forest with floating particles", "futuristic cyberpunk street",
            "medieval castle ruins", "school rooftop at dusk",
            "magical academy classroom", "ninja village at night",
            "space station window view", "traditional Japanese temple"
        ]
        
        self.art_styles = [
            "manga style, black and white ink lines", "anime style, vibrant colors",
            "shonen anime style, dynamic action", "shojo anime style, soft and romantic",
            "seinen anime style, detailed and realistic", "chibi style, cute and simplified",
            "cel shaded anime style", "watercolor anime style",
            "digital painting anime style, high detail"
        ]
        
        self.lighting = [
            "soft golden hour lighting", "dramatic shadows",
            "neon lights glowing", "magical sparkles and particles",
            "backlit by sunset", "moonlight with soft glow",
            "volumetric lighting", "cinematic lighting"
        ]
    
    def generate_prompt(self):
        character = random.choice(self.character_types)
        hair = random.choice(self.hair_styles)
        eyes = random.choice(self.eye_styles)
        outfit = random.choice(self.outfits)
        background = random.choice(self.backgrounds)
        style = random.choice(self.art_styles)
        lighting = random.choice(self.lighting)
        
        prompt = f"""
Anime/manga style illustration of a {character} with {hair} and {eyes},
wearing {outfit}, {background}.
{style}, {lighting}.
High quality, detailed artwork, professional anime art.
Manga ink lines, vibrant colors, dynamic composition.
"""
        return prompt.strip()
    
    def generate_multiple_prompts(self, count=3):
        prompts = []
        for i in range(count):
            prompts.append(f"Prompt {i+1}:
{self.generate_prompt()}")
        return prompts


if __name__ == "__main__":
    generator = AnimeMangaPromptGenerator()
    
    print("=== ANIME/MANGA PROMPT ===")
    print(generator.generate_prompt())
    print("
" + "="*50)
    
    print("
=== 3 MORE PROMPTS ===")
    for prompt in generator.generate_multiple_prompts(3):
        print(prompt)
        print()
