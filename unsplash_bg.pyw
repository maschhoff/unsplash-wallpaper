import unsplash
import settings
import time

while True:
        unsplash.main()
        config=settings.loadConfig()
        time.sleep(config["updatetime"]) #TODO Read time from config
        unsplash.del_image()