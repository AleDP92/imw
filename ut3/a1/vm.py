from mysql import DB


class VirtualMachine:
    def __init__(self, id):
        self.db = DB("emmet", "78648819c", "vmweb")
        sql = f"select * from vmachine where id={1}"
        query = self.db.query(sql)
        self.id = query[0]["id"]
        self.name = query[0]["name"]
        self.ram = query[0]["ram"]
        self.cpu = query[0]["cpu"]
        self.hdd = query[0]["hdd"]
        self.os = query[0]["os"]
        self.status = query[0]["status"]

    def stop(self):
        sql = "delete from process where vmachine_id=1"
        self.db.run(sql)
        sql = "update vmachine set status=0 where id=1"
        self.db.run(sql)
        self.status = 0

    def start(self):
        sql = "update vmachine set status=1 where id=1"
        self.db.run(sql)
        self.status = 1

    def suspend(self):
        sql = "update vmachine set status=2 where id=1"
        self.db.run(sql)
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def get_processes(self):
        sql = "select * from process where vmachine_id=1"
        return self.db.query(sql)

    def run(self, pid, ram, cpu, hdd):
        sql = f"insert into process (pid, ram, cpu, hdd, vmachine_id) value ({pid}, {ram}, {cpu}, {hdd}, 1)"
        self.db.run(sql)

    def ram_usage(self):
        ram = 0
        for p in self.get_processes():
            ram += p["ram"]
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for p in self.get_processes():
            cpu += p["cpu"]
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for p in self.get_processes():
            hdd += p["hdd"]
        return hdd * 100 / self.hdd

    def get_status(self):
        if self.status == 0:
            return "Stopped"
        elif self.status == 1:
            return "Running"
        elif self.status == 2:
            return "Suspended"

    def __str__(self):
        return """
{} <{}> [{}]
{:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used
        """.format(
            self.os,
            self.name,
            self.get_status(),
            self.ram_usage(),
            self.cpu_usage(),
            self.hdd_usage()
        )
