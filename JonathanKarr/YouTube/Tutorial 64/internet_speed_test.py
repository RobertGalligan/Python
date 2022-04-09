#pip install speedtest-cli
import speedtest
test = speedtest.Speedtest()
#print("Loading server list...")
#test.get_servers()
print("Choosing the server...")
best = test.get_best_server()
#print(best)
print("Found:", best["host"], "located in", best["name"], best["country"])
upload_result = round(test.upload() / 1024 / 1024, 2)
print("Upload speed:", upload_result , "Mbps")
download_result = round(test.download() / 1024 / 1024, 2)
print("Download speed:", download_result , "Mbps")
ping_result = round(test.results.ping, 2)
print("Ping:", ping_result, "ms")