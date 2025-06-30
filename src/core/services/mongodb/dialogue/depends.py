from src.core.services.mongodb.dialogue import dialogue_service
from src.core.repositories.mongodb import dialogue_repo

def get_dialogue_service() -> dialogue_service.DialogueService:
    return dialogue_service.DialogueService(repo=dialogue_repo.DialogueRepository)
    