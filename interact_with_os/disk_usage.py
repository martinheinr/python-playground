import shutil
du = shutil.disk_usage("C:")
free_pct=du.free/du.total*100
print("Free disk space of you r C drive is ", round(free_pct, 2), "%")
