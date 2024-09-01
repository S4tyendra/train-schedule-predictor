from datetime import datetime, timedelta
import asyncio
import json
from MultiFeatures.IndianRailway import whereismytrain
import filter

TRAIN_NO = "22204"
SOURCE = "SC"
DESTINATION = "VSKP"

schedule = ["MONDAY", "WEDNESDAY", "SATURDAY"]

def get_dates(year, end_date):
    dates = []
    start_date = datetime(year, 1, 1)
    end_date = datetime.strptime(end_date, "%d-%m-%Y")
    
    current_date = start_date
    while current_date <= end_date:
        if current_date.strftime("%A").upper() in schedule:
            dates.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    
    return dates

year = 2024
end_date = "01-09-2024"
dates = get_dates(year, end_date)

print(dates)
input("Press Enter to continue...")

wit = whereismytrain.WhereIsMyTrain()
complete_data = {}

async def main():
    for date in dates:
        try:
            status = await wit.live_status(TRAIN_NO, date, SOURCE, DESTINATION)
            filtered_data = filter.process_data(status)
            complete_data[date] = filtered_data
        except Exception as e:
            print(f"An error occurred: {e} for date: {date}")

def write_to_file(data, filename):
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
    write_to_file(complete_data, TRAIN_NO)