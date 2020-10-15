html = "/var/sensordata/html/data_visualization.html"
message = """
<html>
<title></title>
<head></head>
<body>
<a href="/var/sensordata/html/comparison_line_7.html">7天数据可视化</a>
<p> </p>
<a href="/var/sensordata/html/comparison_line_30.html">30天数据可视化</a>
</body>
</html>
"""
with open(html, 'w') as f:
    f.write(message)
    f.close()
input = open('/var/sensordata/html/data_visualization.html','r',)
text=input.read()
output = open('/var/sensordata/html/506_devices_status.html','a+',encoding="utf-8")
output.write(text)