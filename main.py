import base
# import ankarateknokent
# import atateknokent
# import atap
# import entertech
# import firatteknokent
# import gaziantepteknopark
# import gbteknokent
# import hacettepeteknokent
# import kirikkaleteknopark
# import konyateknokent
# import malatyateknokent
# import odtuteknokent
# import ostimteknopark
# import pauteknokent
# import teknoparkankara
# import teknoparkistanbul
# import teknoparkizmir
# import trabzonteknokent
# import trakyateknopark
import yildizteknopark

# NOTE : Use rlt variable to get returned value for notify.

# ankarateknokent.execute()
# atateknokent.execute()
# atap.exceute()
# firatteknokent.exceute()
# gaziantepteknopark.exceute()
# gbteknokent.exceute()
# hacettepeteknokent.exceute()
# entertech.exceute()
# kirikkaleteknopark.exceute()
# konyateknokent.exceute()
# malatyateknokent.exceute()
# rlt = odtuteknokent.exceute()
# rlt = ostimteknopark.exceute()
# rlt = pauteknokent.exceute()
# rlt = teknoparkankara.exceute()
# rlt = teknoparkistanbul.exceute()
# rlt = teknoparkizmir.exceute()
# rlt = trabzonteknokent.exceute()
# rlt = trakyateknopark.exceute()
rlt = yildizteknopark.exceute()

base.notify(rlt[0], rlt[1])
base.kill_web_driver_edge()
