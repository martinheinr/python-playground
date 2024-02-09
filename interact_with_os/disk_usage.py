import shutil

def bytes_to_gb(bytes):
    return bytes / (1024 * 1024 * 1024)

du = shutil.disk_usage("C:")
free_pct=du.free/du.total*100
print("Free disk space of you r C drive is ", round(free_pct, 2), "%")

dut = shutil.disk_usage("C:")
free_dut=dut.total-dut.used

print(bytes_to_gb(free_dut))


