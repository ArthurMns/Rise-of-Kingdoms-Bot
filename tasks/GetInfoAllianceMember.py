import traceback

from tasks.constants import TaskName
from tasks.Task import Task

from tasks.constants import TaskName


class GetInfoAllianceMember(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task=TaskName.TRAINING):
        print("ça maaaaaarche")
        super().set_text(title="GetInfoAllianceMember", remove=True)
        super().set_text(insert="Init view")
        print(next_task)
