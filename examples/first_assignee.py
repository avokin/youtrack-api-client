from youtrack.first_assignee_snapshot_strategy import FirstAssigneeSnapshotStrategy
from youtrack.idea_data_set import idea_2019_03_20_to_idea_2020_03_21

issues = idea_2019_03_20_to_idea_2020_03_21(FirstAssigneeSnapshotStrategy())
print("Successfully retrieved {} issues".format(len(issues)))
