from app.infrastructure.models.database import UserOrm

def make_prompt(task: str, user: UserOrm) -> str:
    return (f'{task}'
            f'User name: {user.name}. User English Level: {user.level.value}'
            f'Your current dialog with that user {user.dialog}'
            f'Your last feedback: {user.last_feedback}'
            )
