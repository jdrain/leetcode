# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
lines = sys.stdin.readlines()

month_map = {
    "Jan":"01",
    "Feb":"02",
    "Mar":"03",
    "Apr":"04",
    "May":"05",
    "Jun":"06",
    "Jul":"07",
    "Aug":"08",
    "Sep":"09",
    "Oct":"10",
    "Nov":"11",
    "Dec":"12"
}
success_rate = {}

for line in lines:
    m = re.match("^.*\[((\d+/\w+/\d+):(\d+:\d+)):\d+.*\].*\"([A-Z]+)\s+((/[\w\.]*)+).*HTTP/1.1\"\s+(\d{3}).*$",line)
    if m:
        # print("match:\n")
        # print(line)
        date = m.group(2).split("/")
        date_str = "-".join([date[len(date)-i-1] if i != 1 else month_map[date[len(date)-i-1]] for i in range(0,len(date))])
        datetime_str = date_str+"T"+m.group(3)

        if datetime_str not in success_rate.keys():
            success_rate[datetime_str] = {}
        if m.group(5) not in success_rate[datetime_str].keys():
            success_rate[datetime_str][m.group(5)] = [0, 0]
        tmp = success_rate[datetime_str][m.group(5)]

        if int(m.group(7)) < 500:
            success_rate[datetime_str][m.group(5)][0] = tmp[0] + 1
        success_rate[datetime_str][m.group(5)][1] = tmp[1] + 1

# sort success rates and format the output
ls = sorted(success_rate.keys(), key=lambda x: x.split("T")[1].split(":")[0])
for i in ls:
    for j in sorted(success_rate[i].keys()):
        tmp = success_rate[i][j]
        r = "{0:.2f}".format((float(tmp[0])/float(tmp[1]))*100.0)
        print(" ".join([i, j, r]))
