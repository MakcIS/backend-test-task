from core.repositories.mongodb.dialogue import DialogueRepository
from core.services.dialogue_service import DialogueService


def get_dialogue_service() -> DialogueService:
    return DialogueService(repo=DialogueRepository())
