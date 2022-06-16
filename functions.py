def getUser(ctx, names):
    guild = ctx.author.guild
    return guild.get_member_named(names)