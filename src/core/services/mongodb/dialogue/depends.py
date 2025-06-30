from src.core.repositories.mongodb.dialogue_repo import DialogueRepository
from src.core.services.mongodb.dialogue.dialogue_service import DialogueService


def get_dialogue_service() -> DialogueService:
    return DialogueService(repo=DialogueRepository())
