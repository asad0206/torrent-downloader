import libtorrent as lt
import time
import datetime

link = input("Magnet Link: \n")

ses = lt.session()
ses.listen_on(6881,6891)

params = {
    'save_path': 'D:\\Torrent',
    'storage_mode': lt.storage_mode_t(2)
}

handle = lt.add_magnet_uri(ses,link,params)
ses.start_dht()

begin = time.time()
print(datetime.datetime.now())

print('Downloading...')
while(not handle.has_metadata()):
    time.sleep(1)
print('Metadata Fetched, starting Torrent Download...')

print('Starting', handle.name())

while(handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    status_str = ['queued','checking','downloading metadata',\
        'downloading', 'finished', 'seeding', 'allocating']
    print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d seeds: %d) %s ' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, s.num_seeds, status_str[s.state]))
    time.sleep(5)

end = time.time()
print(handle.name(), "COMPLETE...")

print("Elapsed Time: ", int((end-begin)//60), "min :", int((end-begin)%60), "sec")
print(datetime.datetime.now())