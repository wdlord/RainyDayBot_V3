# from Tomorrow import OWM
import Send_SMS
import schedule, time
import NWS_API as Weather


def rainy_day_bot():
    forecast = Weather.check_rain()

    if Weather.will_rain(forecast):
        Send_SMS.send_message("FORECAST ", forecast)

    print(f"FORECAST - {forecast}")


# MAIN program
# --------------------------
rainy_day_bot()

# NOTE: this server runs on GMT Timezone, adjust schedules accordingly
schedule.every().day.at("02:00").do(rainy_day_bot)

# infinite loop
while True:
  schedule.run_pending()
  time.sleep(1)
