from spout.shared.plugin_options import PluginDefinition

PLUGIN_DEFINITION = PluginDefinition(
    name="prompt_booster",
    description="Make improvements to an input text prompt",
    options=[],
    help_text="""
    The prompt_booster plugin improves upon or 'boosts' a given prompt.

    Features:

    - Enhances clarity and coherence

    - Suggests improvements and alternatives

    - Provides context-specific recommendations

    - Maintains the original intent and style

    This plugin is ideal for:

    - Refining prompts for better responses

    - Enhancing the quality of generated content

    """,
    examples=[
        "spout prompt_booster 'Write a story about a dragon'",
        "spout prompt_booster  # uses clipboard content"
    ]
)