from typing import Generic, TypeVar, Optional, List, Type
from django.db.models import Model, QuerySet

T = TypeVar("T", bound=Model)


class BaseRepository(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def get_queryset(self) -> QuerySet[T]:
        return self.model_class.objects.all()

    def get_by_id(self, id: int) -> Optional[T]:
        return self.get_queryset().filter(id=id).first()

    def get_all(self) -> QuerySet[T]:
        return self.get_queryset()

    def get_active(self) -> QuerySet[T]:
        return self.get_queryset().filter(is_active=True)

    def create(self, **kwargs) -> T:
        return self.model_class.objects.create(**kwargs)

    def update(self, instance: T, **kwargs) -> T:
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance: T) -> None:
        instance.delete()

    def soft_delete(self, instance: T) -> T:
        instance.is_active = False
        instance.save()
        return instance

    def count(self) -> int:
        return self.get_queryset().count()

    def exists(self, **kwargs) -> bool:
        return self.get_queryset().filter(**kwargs).exists()


class BaseModelRepository(BaseRepository[T]):
    def get_by_field(self, field: str, value) -> Optional[T]:
        return self.get_queryset().filter(**{field: value}).first()

    def filter_by(self, **kwargs) -> QuerySet[T]:
        return self.get_queryset().filter(**kwargs)

    def bulk_create(self, objects: List[T]) -> List[T]:
        return self.model_class.objects.bulk_create(objects)

    def get_or_create(self, defaults: dict = None, **kwargs) -> tuple:
        return self.model_class.objects.get_or_create(defaults=defaults, **kwargs)
