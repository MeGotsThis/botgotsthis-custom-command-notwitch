from typing import Collection, Iterable

from lib.data import CustomCommandField, CustomCommandProcess

from .. import custom


def fields() -> Iterable[CustomCommandField]:
    return []


def properties() -> Collection[str]:
    if not hasattr(properties, 'properties'):
        setattr(properties, 'properties', [
            'notwitch',
            'notwitchpartial',
            ])
    return getattr(properties, 'properties')


def postProcess() -> Iterable[CustomCommandProcess]:
    yield custom.propertyNoTwitchCommands
