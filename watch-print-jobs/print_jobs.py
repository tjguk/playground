#!python3
import os, sys
import wmi

c = wmi.WMI()
watcher = c.Win32_PrintJob.watch_for()

while True:
    try:
        job = watcher(timeout_ms=500)
    except wmi.x_wmi_timed_out:
        continue
    else:
        print(job.Name, "-", job.Document, "-", job.JobStatus, "-", "-", job.StatusMask)
