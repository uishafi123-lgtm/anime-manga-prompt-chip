import random

class AnimeMangaPromptGenerator:
    def __init__(self):
        self.character_types = ["anime girl", "anime boy", "manga heroine", "magical girl", "ninjas", "samurai"]
        self.hair_styles = ["long pink flowing hair", "short blue spiky hair", "black twin-tails", "silver wavy hair", "golden long hair"]
        self.eye_styles = ["large expressive blue eyes", "vibrant green eyes", "fiery red eyes", "golden anime eyes", "purple mysterious eyes"]
        self.outfits = ["Japanese school uniform", "fantasy armor", "magical girl dress", "ninja outfit", "samurai armor"]
        self.backgrounds = ["cherry blossom trees", "Tokyo cityscape", "mystical forest", "fantasy castle", "cyberpunk street"]
        self.art_styles = ["anime style, vibrant colors", "manga style, ink lines", "shonen style, dynamic", "shojo style, soft"]
        self.lighting = ["golden hour lighting", "dramatic shadows", "neon lights", "magical sparkles", "moonlight"]
    
    def generate_prompt(self):
        character = random.choice(self.character_types)
        hair = random.choice(self.hair_styles)
        eyes = random.choice(self.eye_styles)
        outfit = random.choice(self.outfits)
        background = random.choice(self.backgrounds)
        style = random.choice(self.art_styles)
        lighting = random.choice(self.lighting)
        
        prompt = "Anime/manga style illustration of a " + character + " with " + hair + " and " + eyes + ", wearing " + outfit + ", " + background + ". " + style + ", " + lighting + ". High quality, detailed artwork."
        return prompt


if __name__ == "__main__":
    generator = AnimeMangaPromptGenerator()
    print("=== ANIME/MANGA PROMPT ===")
    print(generator.generate_prompt())
