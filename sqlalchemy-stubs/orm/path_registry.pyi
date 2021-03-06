from typing import Any

log: Any = ...

class PathRegistry(object):
    is_token: bool = ...
    is_root: bool = ...
    def __eq__(self, other): ...
    def set(self, attributes, key, value): ...
    def setdefault(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def __len__(self): ...
    @property
    def length(self): ...
    def pairs(self): ...
    def contains_mapper(self, mapper): ...
    def contains(self, attributes, key): ...
    def __reduce__(self): ...
    def serialize(self): ...
    @classmethod
    def deserialize(cls, path): ...
    @classmethod
    def per_mapper(cls, mapper): ...
    @classmethod
    def coerce(cls, raw): ...
    def token(self, token): ...
    def __add__(self, other): ...

class RootRegistry(PathRegistry):
    path: Any = ...
    has_entity: bool = ...
    is_aliased_class: bool = ...
    is_root: bool = ...
    def __getitem__(self, entity): ...

class TokenRegistry(PathRegistry):
    token: Any = ...
    parent: Any = ...
    path: Any = ...
    def __init__(self, parent, token) -> None: ...
    has_entity: bool = ...
    is_token: bool = ...
    def generate_for_superclasses(self): ...
    def __getitem__(self, entity): ...

class PropRegistry(PathRegistry):
    prop: Any = ...
    parent: Any = ...
    path: Any = ...
    def __init__(self, parent, prop) -> None: ...
    @property
    def has_entity(self): ...
    @property
    def entity(self): ...
    @property
    def mapper(self): ...
    @property
    def entity_path(self): ...
    def __getitem__(self, entity): ...

class EntityRegistry(PathRegistry, dict):
    is_aliased_class: bool = ...
    has_entity: bool = ...
    key: Any = ...
    parent: Any = ...
    entity: Any = ...
    path: Any = ...
    entity_path: Any = ...
    def __init__(self, parent, entity) -> None: ...
    @property
    def mapper(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __getitem__(self, entity): ...
    def __missing__(self, key): ...
