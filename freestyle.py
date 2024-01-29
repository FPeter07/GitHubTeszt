import requests

URL = 'http://www.boredapi.com/api/activity'


def main():
    activity = int(input('A program ötletet ad arra, hogy mit csinálj akkor, amikor unatkozol!\nHa tevékenységtípus '
                         'alapján választanál, írj egy 1-est!\nHa résztvevők száma alapján választanál, '
                         'írj egy 2-est! '))
    if activity == 1:
        activitytype()
    elif activity == 2:
        activityparticipants()
    repeat = input('Újra szeretnéd futtatni? Y/N ')
    if repeat == 'Y':
        main()


def activitytype():
    activities = ['education', 'recreational', 'music', 'social', 'busywork', 'charity', 'relaxation', 'cooking', 'diy']
    for index, activity in enumerate(activities):
        print(index, activity)

    index = int(input('Válassz a fenti listából egy tevékenységet! Írd be a tevékenység számát! '))
    activity = activities[index]

    payload = {'type': activity}
    resp = requests.get(URL, params=payload)

    result = resp.json()
    print(result['activity'])


def activityparticipants():
    participants = input('Add meg a résztvevők számát 1 és 5 között! ')
    payload = {'participants': participants}
    resp = requests.get(URL, params=payload)

    result = resp.json()
    print(result['activity'])


main()
