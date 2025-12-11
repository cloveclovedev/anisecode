```python
import traceback
from discord import Interaction, app_commands
from discord.ext import commands

from bot.services.llm.repository import LLMRepository


class GeminiChatCog(commands.Cog):
    """Simple chat functionality using Gemini AI."""
    
    def __init__(self, bot):
        self.bot = bot
        self.llm_repository = LLMRepository(
            model_name="gemini/gemini-2.5-flash",
            api_key=self.bot.gemini_api_key
        )

    @app_commands.command(name="chat", description="Chat with Gemini AI.")
    @app_commands.describe(message="Your message to Gemini")
    async def chat(self, interaction: Interaction, message: str):
        """Chat with Gemini AI."""
        # Defer response as AI processing might take time
        await interaction.response.defer()

        try:
            # Generate content using Repository
            response_text = await self.llm_repository.generate_content(message)
            await interaction.followup.send(response_text)
            
        except Exception as e:
            print(f"An error occurred with the LLM API call: {e}")
            traceback.print_exc()
            await interaction.followup.send(f"❌ An error occurred while processing your request. Please try again later.")


async def setup(bot):
    """Setup function to add the cog to the bot."""
    await bot.add_cog(GeminiChatCog(bot))

