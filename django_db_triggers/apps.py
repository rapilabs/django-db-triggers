from enum import Enum

from django.apps import AppConfig


class EventTiming(Enum):
    BEFORE = 'BEFORE'
    AFTER = 'AFTER'
    INSTEAD_OF = 'INSTEAD OF'


class Event(Enum):
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    TRUNCATE = 'TRUNCATE'


trigger_sql = """\
CREATE {constraint} TRIGGER {name} {event_timing} {events}
  ON {table}
  FOR EACH {statement_or_row}
  {condition}
  EXECUTE PROCEDURE {procedure}
"""


class Trigger:
    is_constraint = False
    event_timing = EventTiming.AFTER
    for_each_statement = False
    condition = ''

    def __init__(self, name, events, table, procedure):
        self.name = name,
        self.table = table,
        self.procedure = procedure,
        self.events = events

    def __str__(self):
        return trigger_sql.format(
            constraint='CONSTRAINT' if self.is_constraint else '',
            name=self.name,
            event_timing=self.event_timing.value,
            events=' OR '.join(event.value for event in self.events),
            table=self.table,
            statement_or_row='STATEMENT' if self.for_each_statement else 'ROW',
            condition='WHEN ({})'.format(self.condition) if self.condition else '',
            procedure=self.procedure,
        )


class DjangoDbTriggersConfig(AppConfig):
    name = 'django_db_triggers'
