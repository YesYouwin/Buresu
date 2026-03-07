from discord import app_commands

def is_staff():
    """Check if a user has a staff role or is an admin."""
    async def predicate(interaction: app_commands.Interaction) -> bool:
        allowed_roles = [1446622781356769430]
        if any(role.id in allowed_roles for role in interaction.user.roles):
            return True
        if interaction.user.guild_permissions.administrator:
            return True
        return False
    return app_commands.check(predicate)
