# from MultiFeatures.IndianRailway import whereismytrain
# import asyncio
 
# wit = whereismytrain.WhereIsMyTrain()


# async def main():
#             status = await wit.live_status("18573", '29-08-2024', "VSKP", "BGKT")
#             import ast
#             # data = ast.literal_eval(status)
#             import json
#             print(json.dumps(status, indent=4, ))
#             with open('data.json', 'w') as f:
#                 json.dump(status, f, indent=4)

# if __name__ == "__main__":
#     asyncio.run(main())
import os
import json
from dataclasses import dataclass, field, asdict
from typing import List, Optional

@dataclass
class Schedule:
    actual_arrival_tm: Optional[str] = None
    actual_departure_time: Optional[str] = None
    delay_in_departure: Optional[str] = None
    non_agg_arrival_time: Optional[str] = None
    non_agg_departure_tm: Optional[str] = None
    actual_arrival_time: Optional[str] = None
    sch_arrival_time: Optional[str] = None
    sch_departure_tm: Optional[str] = None
    station_code: Optional[str] = None
    platform: Optional[str] = None
    non_agg_arrival_tm: Optional[str] = None
    actual_departure_tm: Optional[str] = None
    sch_departure_time: Optional[str] = None
    non_agg_departure_time: Optional[str] = None
    distance: Optional[str] = None
    sch_arrival_tm: Optional[str] = None
    delay_in_arrival: Optional[str] = None

@dataclass
class TrainData:
    train_name: str
    train_number: int
    schedule: List[Schedule] = field(default_factory=list)

def process_data(json_data: dict):
    
    
    train_data = TrainData(
        train_name=json_data['train_name'],
        train_number=18573
    )
    
    for schedule in json_data['days_schedule']:
        schedule_data = {k: schedule.get(k) for k in Schedule.__annotations__}
        train_data.schedule.append(Schedule(**schedule_data))
    
    return asdict(train_data)

# Usage
if __name__ == "__main__":
    processed_data = process_data('data.json', 'new_data.json')
    print(processed_data)
    json_data = json.dumps(asdict(processed_data), indent=4)
    with open('new_data.json', 'w') as f:
        f.write(json_data)