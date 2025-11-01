from schedulers.de.scheduler import DeSheduler
# from schedulers.au.scheduler import AuSheduler
# from schedulers.tj.scheduler import TjSheduler
# from schedulers.vi.scheduler import ViSheduler
# from schedulers.rh.scheduler import RhSheduler
from interface.schedulerInterface import ScheduleInterface

de_sheduler = DeSheduler()
de_sheduler.set_tasks()

# au_sheduler = AuSheduler()
# au_sheduler.set_tasks()

# tj_sheduler = TjSheduler()
# tj_sheduler.set_tasks()

# vi_sheduler = ViSheduler()
# vi_sheduler.set_tasks()

# rh_sheduler = RhSheduler()
# rh_sheduler.set_tasks()

print("🕒 Scheduler iniciado...")

ScheduleInterface.scheduler.start()
