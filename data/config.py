from environs import Env
env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
channel = (-1002140039617,"Muhammadali","https://t.me/Muhammadali_0797")