from youtrack.snapshot_strategy import SnapshotStrategy


class FirstAssigneeSnapshotStrategy(SnapshotStrategy):
    def is_snapshot_taken(self, issue):
        return 'first_assignee' in issue

    def process(self, issue):
        super().process(issue)

        snapshot_issue = self.issues[issue['id']]
        if 'assignee' not in snapshot_issue and 'assignee' in snapshot_issue:
            snapshot_issue['first_assignee'] = snapshot_issue['assignee']
