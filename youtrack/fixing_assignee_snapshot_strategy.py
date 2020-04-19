from youtrack.snapshot_strategy import SnapshotStrategy


class FixingAssigneeSnapshotStrategy(SnapshotStrategy):
    def is_snapshot_taken(self, issue):
        return 'fixed_by' in issue

    def process(self, issue):
        super().process(issue)

        snapshot_issue = self.issues[issue['id']]
        if 'fixed_by' not in snapshot_issue:
            if 'state' in issue and issue['state'] == 'Fixed':
                if 'assignee' in snapshot_issue:
                    snapshot_issue['fixed_by'] = snapshot_issue['assignee']
