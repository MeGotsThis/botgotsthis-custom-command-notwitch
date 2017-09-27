from lib.data import CustomProcessArgs


async def propertyNoTwitchCommands(args: CustomProcessArgs) -> None:
    if not await args.database.getCustomCommandProperty(
            args.broadcaster, args.level, args.command, 'notwitch'):
        return

    if any(m for m in args.messages if m.startswith(('.', '/'))):
        messages = args.messages[:]
        args.messages.clear()
        if await args.database.getCustomCommandProperty(
                args.broadcaster, args.level, args.command, 'notwitchpartial'):
            args.messages.extend(m for m in messages
                                 if not m.startswith(('.', '/')))
