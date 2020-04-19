# youtrack-api-client

It's a library to work with YouTrack API. Right now it's useful to restore issues state till specified moment.

## Getting Started

To download activities and restore issues to defined state use the method 
`youtrack/idea_data_set.py#idea_2019_03_20_to_idea_2020_03_21(snapshot_strategy)`.

Example:
```python
from youtrack.idea_data_set import idea_2019_03_20_to_idea_2020_03_21
from youtrack.first_assignee_snapshot_strategy import FirstAssigneeSnapshotStrategy
issues = idea_2019_03_20_to_idea_2020_03_21(FirstAssigneeSnapshotStrategy())
```

Or just check file `examples/first_assignee.py`

At the moment there are 2 snapshot strategy defined:
 * SnapshotStrategy - restores actual issue state
 * FirstAssigneeSnapshotStrategy - restores state of the issue to the moment when it first time assigned