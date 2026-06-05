from typing import Generic, TypeVar, Optional, List
from django.db import transaction
from django.db.models import QuerySet
from core.repositories import BaseRepository

T = TypeVar("T")

ModelT = TypeVar("ModelT")


class BaseService(Generic[ModelT]):
    def __init__(self, repository: BaseRepository[ModelT]):
        self.repository = repository

    def get_by_id(self, id: int) -> Optional[ModelT]:
        return self.repository.get_by_id(id)

    def get_all(self) -> QuerySet[ModelT]:
        return self.repository.get_all()

    def get_active(self) -> QuerySet[ModelT]:
        return self.repository.get_active()

    @transaction.atomic
    def create(self, **kwargs) -> ModelT:
        return self.repository.create(**kwargs)

    @transaction.atomic
    def update(self, instance: ModelT, **kwargs) -> ModelT:
        return self.repository.update(instance, **kwargs)

    @transaction.atomic
    def delete(self, instance: ModelT) -> None:
        self.repository.delete(instance)

    @transaction.atomic
    def soft_delete(self, instance: ModelT) -> ModelT:
        return self.repository.soft_delete(instance)

    def count(self) -> int:
        return self.repository.count()
