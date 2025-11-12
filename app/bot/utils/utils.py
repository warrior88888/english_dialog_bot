from app.infrastructure.models.enums import RolesEnum

def add_new_message(
        msg_role: str, messages: str | None, message_text: str
) -> str:
    """
    Refactor dialog after adding new message.
    """
    new_message = (f'{getattr(RolesEnum, msg_role).value} : '
                   f'{message_text} {RolesEnum.msg_split}'
                   )
    if messages is not None:
        current_messages = messages.split(RolesEnum.msg_split)
        current_messages.append(new_message)
        if len(current_messages) >= 6:
            current_messages = current_messages[1:]
        return ''.join(current_messages)
    else:
        return new_message
