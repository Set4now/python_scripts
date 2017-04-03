import commands
cmd = "ls -lrth"
output = commands.getoutput(cmd)
print output
