# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def _with_ad_unit_mask(flight_request):
    flight_request = json.loads(flight_request)
    if len(flight_request['portfolio']['ad_units']) < 1 or flight_request['portfolio']['ad_units'][0] is None:
        return False
    else:
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    stra = '{"portfolio":{"fee_factor":1.0,"exchange_rate":null,"currency":null,"ad_units":[null]}}'
    ja = json.loads(stra)
    print(ja['portfolio']['ad_units'])
    print(len([None]))
    print(_with_ad_unit_mask(stra))
