from core.services import Crawler, Mover

crawler = Crawler("~/Music/iTunes/iTunes Media/Music")
mover = Mover("~/Music/iTunes/iTunes Bulk Media/Music")

mover.copy_files(crawler.get_files())
